from flask import Flask, request, jsonify
from amocrm.v2 import tokens
from models import Lead, Contact  # Используем кастомные классы

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/create-lead": {"origins": "https://dompluse.com"}})

tokens.default_token_manager(
    client_id="14c35dff-2124-407b-93c0-bd609f2f095b",
    client_secret="eCNZi5fvnV5F1EZhvOATck2ssfKFNFmaZpoOjCq9Aqh3gERRQrQmUmaI1klkaGL1",
    subdomain="vbr07",
    redirect_url="https://dompluse.com/",
    storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
)


@app.route('/create-lead', methods=['POST'])
def create_lead():
    try:
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        services = data.get('services')
        svoi_dom = data.get('svoi_dom')
        project = data.get('project')

        if not phone:
            return jsonify({"status": "error", "details": "Не указаны обязательное поле: phone"}), 400

        contact = Contact(name=name)
        contact.telefon = phone
        contact.email = email
        contact.create()

        if not contact.id:
            return jsonify({"status": "error", "details": "Контакт не был создан."}), 400

        lead = Lead(name=f"Сделка для {name}")
        lead.pipeline_id = 8934494
        lead.uslugi = services
        lead.svoi_dom = svoi_dom
        lead.proekty = project

        # Очищаем пустые enum-поля
        ENUM_FIELDS = [
            "prichina_otkaza", "tekhnologiia", "etazhnost", "proekt", "uchastok",
            "tip_oplaty", "period_stroitelstva", "fundament", "otdelka_vnutrenniaia",
            "istochnik_sdelki", "teplota_klienta", "tip_sdelki", "transh_poluchen",
            "pol_klienta", "kakaia_kvartira", "tsel", "sposob_oplaty", "sertifikaty"
        ]
        for field_name in ENUM_FIELDS:
            if hasattr(lead, field_name):
                value = getattr(lead, field_name)
                if value in [None, "", []]:
                    setattr(lead, field_name, None)

        lead.create()

        if not lead.id:
            return jsonify({"status": "error", "details": "Сделка не была создана."}), 400

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
