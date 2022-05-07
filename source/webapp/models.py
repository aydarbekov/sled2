from django.db import models

from django.db import models


class Firma(models.Model):
    full_name_ru = models.CharField(max_length=500, null=True, blank=True, verbose_name='Полное наименование ru')
    full_name_kg = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Полное наименование kg')
    short_name_ru = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сокращенное наименование ru')
    short_name_kg = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сокращенное наименование kg')
    org_form = models.CharField(max_length=220, null=True, blank=True, verbose_name='Организационно правовая форма')
    foreign_founders = models.CharField(max_length=50, null=True, blank=True, verbose_name='Иностранное участие')
    registration_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Регистрационный номер')
    okpo_cod = models.CharField(max_length=220, null=True, blank=True, verbose_name='ОКПО код')
    inn = models.CharField(max_length=220, null=True, blank=True, verbose_name='ИНН организации')
    address_region = models.CharField(max_length=220, null=True, blank=True, verbose_name='Адрес область')
    address_district = models.CharField(max_length=220, null=True, blank=True, verbose_name='Адрес район')
    address_city = models.CharField(max_length=220, null=True, blank=True, verbose_name="Адрес город/село/поселок")
    address_microdistrict = models.CharField(max_length=220, null=True, blank=True, verbose_name='Адрес микрорайон')
    address_street = models.CharField(max_length=220, null=True, blank=True, verbose_name='Адрес улица')
    house_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер дома')
    apartment_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер квартиры')
    phone = models.CharField(max_length=220, null=True, blank=True, verbose_name='Телефон')
    fax = models.CharField(max_length=220, null=True, blank=True, verbose_name="Факс")
    email = models.CharField(max_length=220, null=True, blank=True, verbose_name='Электронная почта')
    reg_or_rereg = models.CharField(max_length=220, null=True, blank=True,
                                    verbose_name='Гос регистрация или перерегистрация')
    order_date = models.CharField(max_length=220, null=True, blank=True, verbose_name='Дата приказа')
    first_reg_date = models.CharField(max_length=220, null=True, blank=True, verbose_name='Дата первичной регистрации')
    creation_method = models.CharField(max_length=220, null=True, blank=True, verbose_name='Способ создания')
    type_of_ownership = models.CharField(max_length=220, null=True, blank=True, verbose_name='Форма собственности')
    director = models.CharField(max_length=220, null=True, blank=True, verbose_name='Директор')
    main_activity = models.CharField(max_length=220, null=True, blank=True, verbose_name='Основной вид деятельности')
    economic_activity_code = models.CharField(max_length=220, null=True, blank=True,
                                              verbose_name='Код экономической деятельности')
    count_of_founders_ind = models.CharField(max_length=220, null=True, blank=True,
                                             verbose_name='Количество учредителей физических лиц')
    count_of_founders_legal = models.CharField(max_length=220, null=True, blank=True,
                                               verbose_name='Количество учредителей юридических лиц')
    total_count_of_founders = models.CharField(max_length=220, null=True, blank=True,
                                               verbose_name='Общее количество учредителей')
    founders = models.TextField(max_length=10000, null=True, blank=True, verbose_name='Учредители')
    url_minjust_site = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Ссылка на сайт')

    def __str__(self):
        return self.full_name_kg


# Otkrytyi budget
class OpenBudget(models.Model):
    type = models.CharField(max_length=220, null=True, blank=True, verbose_name='Тип')
    inn = models.CharField(max_length=220, null=True, blank=True, verbose_name='ИНН организации')
    docs_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер документа')
    period = models.CharField(max_length=220, null=True, blank=True, verbose_name='Период')
    payer = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Плательщик')
    purpose_of_payment = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Назначение платежа')
    amount = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма')

    def __str__(self):
        return self.inn


# Tizme
class People(models.Model):
    inn = models.CharField(max_length=220, null=True, blank=True, verbose_name='ИНН')
    last_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Фамилие')
    first_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Отчество')
    address = models.CharField(max_length=220, null=True, blank=True, verbose_name='Адрес')
    uik = models.CharField(max_length=220, null=True, blank=True, verbose_name='УИК')
    tik = models.CharField(max_length=220, null=True, blank=True, verbose_name='ТИК')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


# Postavshiki s gos zakupok
class Supliers(models.Model):
    inn = models.CharField(max_length=220, null=True, blank=True, verbose_name='ИНН организации')
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name='Наименование организации')
    form = models.CharField(max_length=500, null=True, blank=True, verbose_name='Форма собственности')
    city = models.CharField(max_length=500, null=True, blank=True, verbose_name='Город')
    address = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=220, null=True, blank=True, verbose_name='Телефон')
    bank = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Банк')
    checking_account = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=220, null=True, blank=True, verbose_name='БИК')
    status = models.CharField(max_length=220, null=True, blank=True, verbose_name='Статус')
    reg_date = models.CharField(max_length=500, null=True, blank=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name


# Tenderi
class Tender(models.Model):
    tenders_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    org_name = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Название организации')
    purchases_metod = models.CharField(max_length=220, null=True, blank=True, verbose_name='Метод закупок')
    date_start = models.CharField(max_length=220, null=True, blank=True, verbose_name='Дата публикации')
    date_end = models.CharField(max_length=220, null=True, blank=True, verbose_name='Дата завершения')
    gokz = models.CharField(max_length=220, null=True, blank=True, verbose_name='Гарантийное обеспечение конкурсной заявки')
    purchases_name = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Наименование закупки')
    purchases_format = models.CharField(max_length=220, null=True, blank=True, verbose_name='Формат закупки')
    planned_amount = models.CharField(max_length=220, null=True, blank=True, verbose_name='Планируемая сумма')
    valuta = models.CharField(max_length=220, null=True, blank=True, verbose_name='Валюта конкурса')
    validity = models.CharField(max_length=220, null=True, blank=True, verbose_name='Срок действия конкурсных заявок')
    count_of_lots = models.CharField(max_length=220, null=True, blank=True, verbose_name='Количество лотов')

    def __str__(self):
        return self.tenders_num


class Lot(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    lots_name = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Наименование лота')
    lots_amount = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма')
    address = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Адрес и место поставки')
    condition = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Условие поставки')
    timing = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Сроки поставки')

    def __str__(self):
        return self.tender_num


class Submission(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lot_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма предложения')
    org_name = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Название организации')
    valuta = models.CharField(max_length=220, null=True, blank=True, verbose_name='Валюта')
    gokz_sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='ГОКЗ сумма')
    gokz_form = models.CharField(max_length=220, null=True, blank=True, verbose_name='ГОКЗ форма')
    tax_date = models.CharField(max_length=220, null=True, blank=True, verbose_name='Налог на')
    tax_status = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Налог статус')
    soc_date = models.CharField(max_length=220, null=True, blank=True, verbose_name='Соцфонд на')
    soc_status = models.CharField(max_length=220, null=True, blank=True, verbose_name='Соцфонд статус')

    def __str__(self):
        return f'{self.tender_num} / {self.org_name}'


class Product(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    okgz = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Класс ОКГЗ')
    measure = models.CharField(max_length=220, null=True, blank=True, verbose_name='Единица измерения')
    count = models.CharField(max_length=220, null=True, blank=True, verbose_name='Количество')
    specification = models.TextField(max_length=5000, null=True, blank=True, verbose_name='Спецификация')
    file = models.CharField(max_length=220, null=True, blank=True, verbose_name='Файл')

    def __str__(self):
        return self.specification


class Winner(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    winner_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Название победителя')
    winner_status = models.CharField(max_length=220, null=True, blank=True, verbose_name='Статус победителя')
    winner_sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма победителя')
    canceled_reason = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Причина отказа')
    planned_sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='Планируемая сумма')

    def __str__(self):
        return f'{self.tender_num} / {self.winner_name}'


class WinnerDetailed(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name="Номер тендера")
    zak_org = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Закупающая организация")
    start = models.CharField(max_length=220, null=True, blank=True, verbose_name="Дата начала")
    finish = models.CharField(max_length=220, null=True, blank=True, verbose_name="Дата конца")
    tender_name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название тендера")
    tender_summ = models.CharField(max_length=220, null=True, blank=True, verbose_name="Сумма тендера")
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name="Номер лота")
    lots_name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название лота")
    winner_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Название победителя")
    winner_place = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Занятое место")
    winner_summ = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Предложенная сумма")
    reason = models.CharField(max_length=220, null=True, blank=True, verbose_name="причина отказы")
    planned_summ = models.CharField(max_length=220, null=True, blank=True, verbose_name="Планируемая сумма")

    def __str__(self):
        return f"{self.tender_num} / {self.winner_name}"


class Tizme(models.Model):
    last_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Фамилия")
    first_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Имя")
    middle_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Отчество")
    uik = models.CharField(max_length=1000, null=True, blank=True, verbose_name="УИК")
    tik = models.CharField(max_length=1000, null=True, blank=True, verbose_name="ТИК")
    oblast = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Область")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        indexes = [
            models.Index(fields=["last_name", "first_name", "middle_name"]),
        ]


class SupplierDetailed(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name="Номер тендера")
    zak_org = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Закупающая организация")
    start = models.CharField(max_length=220, null=True, blank=True, verbose_name="Дата начала")
    finish = models.CharField(max_length=220, null=True, blank=True, verbose_name="Дата конца")
    tender_name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название тендера")
    tender_summ = models.CharField(max_length=220, null=True, blank=True, verbose_name="Сумма тендера")
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name="Номер лота")
    lots_name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название лота")
    supplier_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Название победителя")
    gokz = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Гокз")
    gokz_form = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Форма когз")
    proposed_summ = models.CharField(max_length=220, null=True, blank=True, verbose_name="Предложенная сумма")
    planned_summ = models.CharField(max_length=220, null=True, blank=True, verbose_name="Планируемая сумма")

    def __str__(self):
        return f"{self.tender_num} / {self.supplier_name}"


class Gkpen(models.Model):
    license_number = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Номер лицензии и срок")
    object_name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название обьекта")
    firm = models.CharField(max_length=1220, null=True, blank=True, verbose_name="недропользователь")
    inn_okpo = models.CharField(max_length=1220, null=True, blank=True, verbose_name="инн окпо")
    place = models.CharField(max_length=3220, null=True, blank=True, verbose_name="местоположение")
    contract = models.CharField(max_length=1220, null=True, blank=True, verbose_name="контракт")
    kind_of_material = models.CharField(max_length=1220, null=True, blank=True, verbose_name="вид материала")
    type_of_use = models.CharField(max_length=1220, null=True, blank=True, verbose_name="вид недропользования")
    resource = models.CharField(max_length=1000, null=True, blank=True, verbose_name="ресурс")
    square = models.CharField(max_length=1000, null=True, blank=True, verbose_name="площадь")
    contacts = models.CharField(max_length=1000, null=True, blank=True, verbose_name="контакты")
    glf = models.CharField(max_length=1220, null=True, blank=True, verbose_name="глф")
    coordinates = models.CharField(max_length=1220, null=True, blank=True, verbose_name="координаты")

    def __str__(self):
        return f"{self.license_number} / {self.firm}"


class TenderBlackList(models.Model):
    inn = models.CharField(max_length=1220, null=True, blank=True, verbose_name="инн")
    name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название фирмы")
    start = models.DateTimeField(null=True, blank=True, verbose_name="Начало")
    finish = models.DateTimeField(null=True, blank=True, verbose_name="конец")
    justification = models.CharField(max_length=3220, null=True, blank=True, verbose_name="обоснование")

    def __str__(self):
        return f"{self.name} / {self.start}"


class Smi(models.Model):
    name_ru = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название на русском")
    name_ky = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Название на кыргызском")
    head = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Руководитель")
    ownership = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Собственность")
    max_volume = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Максимальный объем")
    periodicity = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Периодичность")
    postal_ddress = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Почтовый адрес")
    propagation_area = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Место распространения")
    phones = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Телефон")

    def __str__(self):
        return f"{self.name_ru}"


class MinjustHistory(models.Model):
    firm = models.ForeignKey("webapp.Firma", on_delete=models.CASCADE, related_name="history")
    field_name = models.CharField(max_length=1220, verbose_name="Название поля")
    old_data = models.CharField(max_length=10220, null=True, blank=True, verbose_name="Старое значение")
    new_data = models.CharField(max_length=10220, null=True, blank=True, verbose_name="Новое значение")
    update_date = models.DateField(auto_now_add=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.firm.short_name_ru} - {self.field_name}"


class Farm(models.Model):
    inn = models.CharField(max_length=1220, null=True, blank=True, verbose_name="ИНН")
    okpo = models.CharField(max_length=1220, null=True, blank=True, verbose_name="ОКПО")
    name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Наименование")
    series = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Серия")
    reg_number = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Рег. номер")
    reciept = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Квитанция №")
    sum = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Сумма")
    from_date = models.CharField(max_length=1220, null=True, blank=True, verbose_name="От")
    reg_certificate = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Свидетельства о гос. рег.")
    issue_date = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Дата выдачи")
    issued_by = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Кем выдан")
    activity_kind = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Вид деятельности")
    director = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Руководитель")
    foreigners = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Иноcтранцы")
    person_private = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Частное лицо")
    pharmacy_number = models.CharField(max_length=1220, null=True, blank=True, verbose_name="№ Аптеки")
    head_office = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Головное")
    object = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Объект")
    obl = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Область")
    district = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Район")
    city = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Город/Село")
    address = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Адрес")
    telephone = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Телефон")
    spesialists = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Специалисты")
    speciality = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Специальность")
    diploma_data = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Данные диплома")
    sertificate = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Сертификат")
    date_of_issue = models.CharField(max_length=1220, null=True, blank=True, verbose_name="ДатаВыдачиЛиц" )
    prikaz_number = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Номер приказа")
    prikaz_date = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Дата приказа")
    far = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Отдаленный")

    def __str__(self):
        return f"{self.name}"


class Bankrupt(models.Model):
    status = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Статус")
    tin = models.CharField(max_length=1220, null=True, blank=True, verbose_name="ИНН")
    address = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Адрес")
    name = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Наименование")
    bankrot_type = models.CharField(max_length=1220, null=True, blank=True, verbose_name="Категория")

    def __str__(self):
        return f"{self.name}"


class TenderBuyers(models.Model):
    inn = models.CharField(max_length=220, null=True, blank=True, verbose_name="ИНН организации")
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name="Наименование организации")
    form = models.CharField(max_length=500, null=True, blank=True, verbose_name="Форма собственности")
    city = models.CharField(max_length=500, null=True, blank=True, verbose_name="Город")
    address = models.CharField(max_length=2000, null=True, blank=True, verbose_name="Адрес")
    phone = models.CharField(max_length=220, null=True, blank=True, verbose_name="Телефон")
    bank = models.CharField(max_length=2000, null=True, blank=True, verbose_name="Банк")
    checking_account = models.CharField(max_length=2000, null=True, blank=True, verbose_name="Расчетный счет")
    bik = models.CharField(max_length=220, null=True, blank=True, verbose_name="БИК")
    worker_name = models.CharField(max_length=220, null=True, blank=True, verbose_name="ФИО пользователя")
    position = models.CharField(max_length=500, null=True, blank=True, verbose_name="Должность")
    role = models.CharField(max_length=500, null=True, blank=True, verbose_name="Роль")

    def __str__(self):
        return self.name