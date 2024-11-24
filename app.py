from flask import Flask, request, jsonify
from amocrm.v2 import tokens
from models import Lead, Contact  # Используем кастомные классы

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/create-lead": {"origins": "http://localhost:5173"}})

# Устанавливаем менеджер токенов
tokens.default_token_manager(
    client_id="df712b12-041e-4922-9f5c-0856ec5f7739",
    client_secret="mXmG993n4j4J0MImvLhLHU6TWM7Tct5r0iQVkAPrO3AvNxWlh6Ir20T9EqQYrSTk",
    subdomain="tkskubidu",
    redirect_url="https://test-amo-widget-server.loca.lt/auth",
    storage=tokens.FileTokensStorage(),  # Токены хранятся в файле
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
