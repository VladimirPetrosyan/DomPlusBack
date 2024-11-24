
from amocrm.v2 import Contact as _Contact
from amocrm.v2 import Company as _Company
from amocrm.v2 import Lead as _Lead
from amocrm.v2 import tokens, custom_field


tokens.default_token_manager(
    client_secret="mXmG993n4j4J0MImvLhLHU6TWM7Tct5r0iQVkAPrO3AvNxWlh6Ir20T9EqQYrSTk",
    client_id="df712b12-041e-4922-9f5c-0856ec5f7739",
    subdomain="tkskubidu",
    redirect_url="https://test-amo-widget-server.loca.lt/auth",
    storage=tokens.FileTokensStorage(),
)
# code = ...
# if code:
#     tokens.default_token_manager.init(code, skip_error=True)



class Contact(_Contact):
    dolzhnost = custom_field.TextCustomField("Должность", field_id=610919, code="POSITION")
    telefon = custom_field.ContactPhoneField("Телефон", field_id=610921, code="PHONE")
    email = custom_field.ContactEmailField("Email", field_id=610923, code="EMAIL")
    polzovatelskoe_soglashenie = custom_field.CheckboxCustomField("Пользовательское соглашение", field_id=611089, code="USER_AGREEMENT")


class Company(_Company):
    telefon = custom_field.ContactPhoneField("Телефон", field_id=610921, code="PHONE")
    email = custom_field.ContactEmailField("Email", field_id=610923, code="EMAIL")
    web = custom_field.UrlCustomField("Web", field_id=610925, code="WEB")
    adres = custom_field.TextAreaCustomField("Адрес", field_id=610927, code="ADDRESS")


class Lead(_Lead):
    utm_content = custom_field.BaseCustomField("utm_content", field_id=610929, code="UTM_CONTENT")
    utm_medium = custom_field.BaseCustomField("utm_medium", field_id=610931, code="UTM_MEDIUM")
    utm_campaign = custom_field.BaseCustomField("utm_campaign", field_id=610933, code="UTM_CAMPAIGN")
    utm_source = custom_field.BaseCustomField("utm_source", field_id=610935, code="UTM_SOURCE")
    utm_term = custom_field.BaseCustomField("utm_term", field_id=610937, code="UTM_TERM")
    utm_referrer = custom_field.BaseCustomField("utm_referrer", field_id=610939, code="UTM_REFERRER")
    roistat = custom_field.BaseCustomField("roistat", field_id=610941, code="ROISTAT")
    referrer = custom_field.BaseCustomField("referrer", field_id=610943, code="REFERRER")
    openstat_service = custom_field.BaseCustomField("openstat_service", field_id=610945, code="OPENSTAT_SERVICE")
    openstat_campaign = custom_field.BaseCustomField("openstat_campaign", field_id=610947, code="OPENSTAT_CAMPAIGN")
    openstat_ad = custom_field.BaseCustomField("openstat_ad", field_id=610949, code="OPENSTAT_AD")
    openstat_source = custom_field.BaseCustomField("openstat_source", field_id=610951, code="OPENSTAT_SOURCE")
    from_field = custom_field.BaseCustomField("from", field_id=610953, code="FROM")
    gclientid = custom_field.BaseCustomField("gclientid", field_id=610955, code="GCLIENTID")
    ym_uid = custom_field.BaseCustomField("_ym_uid", field_id=610957, code="_YM_UID")
    ym_counter = custom_field.BaseCustomField("_ym_counter", field_id=610959, code="_YM_COUNTER")
    gclid = custom_field.BaseCustomField("gclid", field_id=610961, code="GCLID")
    yclid = custom_field.BaseCustomField("yclid", field_id=610963, code="YCLID")
    fbclid = custom_field.BaseCustomField("fbclid", field_id=610965, code="FBCLID")
    uslugi = custom_field.TextCustomField("Услуги", field_id=634797)
    svoi_dom = custom_field.TextCustomField("Свой Дом", field_id=634799)
    proekty = custom_field.TextAreaCustomField("Проекты", field_id=655711)
