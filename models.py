
from amocrm.v2 import Contact as _Contact
from amocrm.v2 import Company as _Company
from amocrm.v2 import Lead as _Lead
from amocrm.v2 import tokens, custom_field


tokens.default_token_manager(
    client_secret="zOhTj6XoslAyImr6FXCD2FdU6Z4XsdVyMApa6wfFWesEvkhqSeCWcuV1sYkvFZJ8",
    client_id="f639cd4f-10fb-45d4-85e8-69287eb8ce60",
    subdomain="vbr07",
    redirect_url="https://dompluse.com/",
    storage=tokens.FileTokensStorage(directory_path="D:\job\DomPlusBack"),
)
# code = ...
# if code:
#     tokens.default_token_manager.init(code, skip_error=True)



class Contact(_Contact):
    dolzhnost = custom_field.TextCustomField("Должность", field_id=285151, code="POSITION")
    telefon = custom_field.ContactPhoneField("Телефон", field_id=285153, code="PHONE")
    email = custom_field.ContactEmailField("Email", field_id=285155, code="EMAIL")
    polzovatelskoe_soglashenie = custom_field.CheckboxCustomField("Пользовательское соглашение", field_id=862203, code="USER_AGREEMENT")


class Company(_Company):
    telefon = custom_field.ContactPhoneField("Телефон", field_id=285153, code="PHONE")
    email = custom_field.ContactEmailField("Email", field_id=285155, code="EMAIL")
    web = custom_field.UrlCustomField("Web", field_id=285157, code="WEB")
    adres = custom_field.TextAreaCustomField("Адрес", field_id=285159, code="ADDRESS")


class Lead(_Lead):
    utm_content = custom_field.BaseCustomField("utm_content", field_id=285161, code="UTM_CONTENT")
    utm_medium = custom_field.BaseCustomField("utm_medium", field_id=285163, code="UTM_MEDIUM")
    utm_campaign = custom_field.BaseCustomField("utm_campaign", field_id=285165, code="UTM_CAMPAIGN")
    utm_source = custom_field.BaseCustomField("utm_source", field_id=285167, code="UTM_SOURCE")
    utm_term = custom_field.BaseCustomField("utm_term", field_id=285169, code="UTM_TERM")
    utm_referrer = custom_field.BaseCustomField("utm_referrer", field_id=285171, code="UTM_REFERRER")
    roistat = custom_field.BaseCustomField("roistat", field_id=285173, code="ROISTAT")
    referrer = custom_field.BaseCustomField("referrer", field_id=285175, code="REFERRER")
    openstat_service = custom_field.BaseCustomField("openstat_service", field_id=285177, code="OPENSTAT_SERVICE")
    openstat_campaign = custom_field.BaseCustomField("openstat_campaign", field_id=285179, code="OPENSTAT_CAMPAIGN")
    openstat_ad = custom_field.BaseCustomField("openstat_ad", field_id=285181, code="OPENSTAT_AD")
    openstat_source = custom_field.BaseCustomField("openstat_source", field_id=285183, code="OPENSTAT_SOURCE")
    from = custom_field.BaseCustomField("from", field_id=285185, code="FROM")
    gclientid = custom_field.BaseCustomField("gclientid", field_id=285187, code="GCLIENTID")
    ym_uid = custom_field.BaseCustomField("_ym_uid", field_id=285189, code="_YM_UID")
    ym_counter = custom_field.BaseCustomField("_ym_counter", field_id=285191, code="_YM_COUNTER")
    gclid = custom_field.BaseCustomField("gclid", field_id=285193, code="GCLID")
    yclid = custom_field.BaseCustomField("yclid", field_id=285195, code="YCLID")
    fbclid = custom_field.BaseCustomField("fbclid", field_id=285197, code="FBCLID")

    class PRICHINA_OTKAZA_ENUMS:
        net_biudzheta = custom_field.SelectValue(id=500821, value='Нет бюджета')
        vybrali_drugikh = custom_field.SelectValue(id=500823, value='Выбрали других')
        otlozhili = custom_field.SelectValue(id=500825, value='Отложили')
        sami_poteriali = custom_field.SelectValue(id=500827, value='Сами потеряли')
        neadekvatnyi_klient = custom_field.SelectValue(id=500829, value='Неадекватный клиент')
        spam = custom_field.SelectValue(id=500831, value='Спам')
        ne_vyshel_na = custom_field.SelectValue(id=500833, value='Не вышел на связь')
    prichina_otkaza = custom_field.SelectCustomField("Причина отказа", field_id=285199, enums=PRICHINA_OTKAZA_ENUMS)

    class TEKHNOLOGIIA_ENUMS:
        karkasnyi = custom_field.SelectValue(id=500835, value='Каркасный')
        kirpichnyi_kirpich = custom_field.SelectValue(id=500837, value='Кирпичный-Кирпич')
        gazoblok_kirpich = custom_field.SelectValue(id=500839, value='Газоблок-Кирпич')
        sip_paneli = custom_field.SelectValue(id=500843, value='СИП панели')
        modulnyi = custom_field.SelectValue(id=942711, value='Модульный')
        rekonstruktsiia = custom_field.SelectValue(id=942713, value='Реконструкция')
    tekhnologiia = custom_field.SelectCustomField("Технология", field_id=285201, enums=TEKHNOLOGIIA_ENUMS)
    ploshchad_mtwo = custom_field.NumericCustomField("Площадь (м2.)", field_id=285205)

    class ETAZHNOST_ENUMS:
        one = custom_field.SelectValue(id=500851, value='1')
        one_five = custom_field.SelectValue(id=500853, value='1,5')
        two = custom_field.SelectValue(id=500855, value='2')
        three = custom_field.SelectValue(id=500857, value='3')
    etazhnost = custom_field.MultiSelectCustomField("Этажность", field_id=285207, enums=ETAZHNOST_ENUMS)

    class PROEKT_ENUMS:
        est = custom_field.SelectValue(id=500859, value='Есть')
        standartnyi = custom_field.SelectValue(id=500861, value='Стандартный')
        razrabotka = custom_field.SelectValue(id=942721, value='Разработка')
    proekt = custom_field.SelectCustomField("Проект", field_id=285209, enums=PROEKT_ENUMS)

    class UCHASTOK_ENUMS:
        est = custom_field.SelectValue(id=500863, value='Есть')
        net_uchastka_sami = custom_field.SelectValue(id=500865, value='Нет участка, сами найдем')
        nuzhen_poisk = custom_field.SelectValue(id=942729, value='Нужен поиск')
    uchastok = custom_field.SelectCustomField("Участок", field_id=285211, enums=UCHASTOK_ENUMS)

    class TIP_OPLATY_ENUMS:
        nalichnyi_raschet = custom_field.SelectValue(id=500867, value='Наличный расчёт')
        ipoteka = custom_field.SelectValue(id=500871, value='Ипотека')
        kredit = custom_field.SelectValue(id=500873, value='Кредит')
        snachala_prodat = custom_field.SelectValue(id=942731, value='Сначала продать - потом купить')
    tip_oplaty = custom_field.SelectCustomField("Тип оплаты", field_id=285213, enums=TIP_OPLATY_ENUMS)

    class PERIOD_STROITELSTVA_ENUMS:
        one_kvartal_goda_ia_f_m = custom_field.SelectValue(id=500877, value='1 квартал года(я.ф.м)')
        two_kvartal_goda_a_m_i = custom_field.SelectValue(id=500879, value='2 квартал года(а.м.и)')
        three_kvartal_goda_i_a_s = custom_field.SelectValue(id=942733, value='3 квартал года(и.а.с)')
        four_kvartal_goda_o_n_d = custom_field.SelectValue(id=942735, value='4 квартал года(о.н.д)')
    period_stroitelstva = custom_field.MultiSelectCustomField("Период строительства", field_id=285215, enums=PERIOD_STROITELSTVA_ENUMS)
    data_nachala_stroitelstva = custom_field.DateCustomField("Дата начала строительства", field_id=285217)

    class FUNDAMENT_ENUMS:
        plitnyi = custom_field.SelectValue(id=500887, value='Плитный')
        vintovye_svai = custom_field.SelectValue(id=500889, value='Винтовые сваи')
        lentochnyi = custom_field.SelectValue(id=500891, value='Ленточный')
        stolbchatyi = custom_field.SelectValue(id=500893, value='Столбчатый')
    fundament = custom_field.SelectCustomField("Фундамент", field_id=285219, enums=FUNDAMENT_ENUMS)

    class OTDELKA_VNUTRENNIAIA_ENUMS:
        net = custom_field.SelectValue(id=500895, value='Нет')
        white_box = custom_field.SelectValue(id=500903, value='White Box')
    otdelka_vnutrenniaia = custom_field.MultiSelectCustomField("Отделка внутренняя", field_id=285221, enums=OTDELKA_VNUTRENNIAIA_ENUMS)
    akt_na_fundament_podpisan = custom_field.CheckboxCustomField("Акт на фундамент подписан", field_id=285225)
    akt_na_steny_podpisan = custom_field.CheckboxCustomField("Акт на стены подписан", field_id=285227)
    akt_na_krovliu_podpisan = custom_field.CheckboxCustomField("Акт на кровлю подписан", field_id=285229)
    akt_sdachi_podpisan = custom_field.CheckboxCustomField("Акт сдачи подписан", field_id=285231)

    class ISTOCHNIK_SDELKI_ENUMS:
        avito = custom_field.SelectValue(id=500919, value='Авито')
        vkontakte = custom_field.SelectValue(id=500921, value='ВКонтакте')
        instagram = custom_field.SelectValue(id=500923, value='Instagram')
        sait = custom_field.SelectValue(id=500925, value='Сайт')
        vystavki = custom_field.SelectValue(id=500927, value='Выставки')
        rekomendatsii_sarafan = custom_field.SelectValue(id=500929, value='Рекомендации-сарафан')
        youtube = custom_field.SelectValue(id=500931, value='YouTube')
    istochnik_sdelki = custom_field.SelectCustomField("Источник сделки", field_id=285233, enums=ISTOCHNIK_SDELKI_ENUMS)

    class TEPLOTA_KLIENTA_ENUMS:
        goriachii = custom_field.SelectValue(id=500933, value='Горячий')
        teplyi = custom_field.SelectValue(id=500935, value='Теплый')
        kholodnyi = custom_field.SelectValue(id=500937, value='Холодный')
    teplota_klienta = custom_field.SelectCustomField("Теплота клиента", field_id=285239, enums=TEPLOTA_KLIENTA_ENUMS)

    class TIP_SDELKI_ENUMS:
        novostroika = custom_field.SelectValue(id=500939, value='Новостройка')
        individualnoe_stroitelstvo = custom_field.SelectValue(id=500941, value='Индивидуальное строительство')
        kommercheskoe_pomeshchenie = custom_field.SelectValue(id=500943, value='Коммерческое помещение')
        vtorichka_pokupka = custom_field.SelectValue(id=942699, value='Вторичка покупка')
        vtorichka_prodazha = custom_field.SelectValue(id=942701, value='Вторичка продажа')
    tip_sdelki = custom_field.SelectCustomField("Тип сделки", field_id=285241, enums=TIP_SDELKI_ENUMS)

    class TRANSH_POLUCHEN_ENUMS:
        one_transh = custom_field.SelectValue(id=942745, value='1 транш')
        two_transh = custom_field.SelectValue(id=942747, value='2 транш')
        three_transh = custom_field.SelectValue(id=942749, value='3 транш')
        four_transh = custom_field.SelectValue(id=942751, value='4 транш')
    transh_poluchen = custom_field.MultiSelectCustomField("Транш получен", field_id=828165, enums=TRANSH_POLUCHEN_ENUMS)
    kakoi_zhk = custom_field.TextCustomField("Какой ЖК", field_id=828167)

    class POL_KLIENTA_ENUMS:
        muzhchina = custom_field.SelectValue(id=943989, value='Мужчина')
        zhenshchina = custom_field.SelectValue(id=943991, value='Женщина')
    pol_klienta = custom_field.SelectCustomField("Пол клиента", field_id=829657, enums=POL_KLIENTA_ENUMS)
    den_rozhdeniia = custom_field.BaseCustomField("День рождения", field_id=829659)
    nomer_linii_bilain = custom_field.TextCustomField("Номер линии билайн:", field_id=833623)

    class KAKAIA_KVARTIRA_ENUMS:
        st = custom_field.SelectValue(id=963623, value='ст')
        onek = custom_field.SelectValue(id=963625, value='1к')
        etwo = custom_field.SelectValue(id=963627, value='е2')
        twok = custom_field.SelectValue(id=963629, value='2к')
        ethree = custom_field.SelectValue(id=963631, value='е3')
        threek = custom_field.SelectValue(id=963633, value='3к')
        efour = custom_field.SelectValue(id=963635, value='е4')
        fourk = custom_field.SelectValue(id=963637, value='4к')
        efour = custom_field.SelectValue(id=963639, value='е4+')
    kakaia_kvartira = custom_field.MultiSelectCustomField("Какая квартира?", field_id=834751, enums=KAKAIA_KVARTIRA_ENUMS)
    vstrecha_naznachena = custom_field.DateTimeCustomField("Встреча назначена", field_id=834753)
    pokaz_naznachen = custom_field.DateTimeCustomField("Показ назначен", field_id=834755)
    biudzhet = custom_field.NumericCustomField("Бюджет", field_id=834757)

    class TSEL_ENUMS:
        dlia_sebia = custom_field.SelectValue(id=963847, value='Для себя')
        detiam = custom_field.SelectValue(id=963849, value='Детям')
        na_budushchee_investitsiia = custom_field.SelectValue(id=963851, value='На будущее\инвестиция')
    tsel = custom_field.MultiSelectCustomField("Цель", field_id=834759, enums=TSEL_ENUMS)

    class SPOSOB_OPLATY_ENUMS:
        ipoteka = custom_field.SelectValue(id=963853, value='Ипотека')
        nalichnye_sredstva = custom_field.SelectValue(id=963855, value='Наличные средства')
        kredit = custom_field.SelectValue(id=963857, value='Кредит')
    sposob_oplaty = custom_field.MultiSelectCustomField("Способ оплаты", field_id=834761, enums=SPOSOB_OPLATY_ENUMS)

    class SERTIFIKATY_ENUMS:
        net = custom_field.SelectValue(id=963859, value='нет')
        khersonskii = custom_field.SelectValue(id=963861, value='Херсонский')
        azhp = custom_field.SelectValue(id=963863, value='АЖП')
        matkap = custom_field.SelectValue(id=963865, value='МатКап')
        zemelnyi = custom_field.SelectValue(id=963867, value='Земельный')
        bolshe_twokh = custom_field.SelectValue(id=963869, value='Больше 2х')
    sertifikaty = custom_field.MultiSelectCustomField("Сертификаты", field_id=834763, enums=SERTIFIKATY_ENUMS)
    p_vznos = custom_field.TextCustomField("П. Взнос", field_id=834765)

    class TIP_SDELKI_ENUMS:
        kupit_novostroiku = custom_field.SelectValue(id=963871, value='купить Новостройку')
        remont_v_novostroike = custom_field.SelectValue(id=963873, value='ремонт в Новостройке')
    tip_sdelki = custom_field.MultiSelectCustomField("Тип сделки", field_id=834767, enums=TIP_SDELKI_ENUMS)
    obiavlenie = custom_field.TextCustomField("Объявление", field_id=857755)
    url_obiavleniia = custom_field.UrlCustomField("URL объявления", field_id=857757)
    uslugi = custom_field.TextCustomField("Услуги", field_id=881825)
    svoi_dom = custom_field.TextCustomField("Свой дом", field_id=881827)
    proekty = custom_field.TextCustomField("Проекты", field_id=881831)
    kakoi_zhk = custom_field.TextCustomField("Какой ЖК?", field_id=885771)
    ploshchad_kvartiry = custom_field.TextCustomField("Площадь квартиры", field_id=885773)
    remont_pod_kliuch_chastichnyi = custom_field.TextCustomField("Ремонт под ключ/частичный", field_id=885775)
    kolichestvo_komnat = custom_field.TextCustomField("Количество комнат?", field_id=885777)
    novostroika_vtorichka = custom_field.TextCustomField("Новостройка/Вторичка?", field_id=885779)
    bron = custom_field.TextCustomField("Бронь", field_id=888013)
