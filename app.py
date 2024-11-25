from flask import Flask, request, jsonify
from amocrm.v2 import tokens
from models import Lead, Contact  # Используем кастомные классы

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/create-lead": {"origins": "https://dompluse.com"}})

tokens.default_token_manager(
    client_id="156ab0a4-8bfa-4c09-a3a0-5b1e70df309c",
    client_secret="9GszZ6BMU1XtNPHiep671tdAXikfGAmB7RQNPZ8Cwqhu8Re4h26toBmEoVq5DEWi",
    subdomain="vbr07",
    redirect_url="https://dompluse.com",
    storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
)

@app.route('/create-lead', methods=['POST'])
def create_lead():
    try:
        # Получение данных из запроса
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        services = data.get('services')  # Новое поле "Услуги"
        svoi_dom = data.get('svoi_dom')
        project = data.get('project')

        if not phone:
            return jsonify({"status": "error", "details": "Не указаны обязательное поле: phone"}), 400

        # Создание контакта
        contact = Contact(name=name)
        contact.telefon = phone
        contact.email = email
        contact.create()

        # Проверка создания контакта
        if not contact.id:
            return jsonify({"status": "error", "details": "Контакт не был создан."}), 400

        # Создание сделки
        lead = Lead(name=f"Сделка для {name}")
        lead.uslugi = services  # Устанавливаем значение в кастомное поле "Услуги"
        lead.svoi_dom = svoi_dom
        lead.proekty = project
        lead.create()

        # Проверка создания сделки
        if not lead.id:
            return jsonify({"status": "error", "details": "Сделка не была создана."}), 400

        # Привязка контакта к сделке
        lead = Lead.objects.get(object_id=lead.id)
        lead.contacts.append(contact)
        lead.save()

        return jsonify({
            "status": "success",
            "message": "Сделка и контакт успешно созданы",
            "lead": {
                "id": lead.id,
                "name": lead.name,
                "contacts": [{"id": contact.id, "name": contact.name, "phone": phone, "email": email}],
                "services": services,
                "svoi_dom": svoi_dom,
                "project": project,
            }
        })

    except Exception as e:
        print("Error during lead creation:", str(e))
        return jsonify({"status": "error", "details": str(e)}), 500


if __name__ == '__main__':
    app.run()
