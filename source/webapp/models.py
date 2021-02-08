from django.db import models

from django.db import models


class Firma(models.Model):
    full_name_ru = models.CharField(max_length=500, null=True, blank=True, verbose_name='Полное наименование ru')
    full_name_kg = models.CharField(max_length=500, null=True, blank=True, verbose_name='Полное наименование kg')
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
    founders = models.CharField(max_length=5000, null=True, blank=True, verbose_name='Учредители')
    url_minjust_site = models.CharField(max_length=220, null=True, blank=True, verbose_name='Ссылка на сайт')

    def __str__(self):
        return self.inn


# Otkrytyi budget
class OpenBudget(models.Model):
    type = models.CharField(max_length=220, null=True, blank=True, verbose_name='Тип')
    inn = models.CharField(max_length=220, null=True, blank=True, verbose_name='ИНН организации')
    docs_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер документа')
    period = models.DateField(null=True, blank=True, verbose_name='Период')
    payer = models.CharField(max_length=220, null=True, blank=True, verbose_name='Плательщик')
    purpose_of_payment = models.CharField(max_length=220, null=True, blank=True, verbose_name='Назначение платежа')
    amount = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма')

    def __str__(self):
        return f'{self.inn} {self.payer}'


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
    name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Наименование организации')
    form = models.CharField(max_length=220, null=True, blank=True, verbose_name='Форма собственности')
    city = models.CharField(max_length=220, null=True, blank=True, verbose_name='Город')
    address = models.CharField(max_length=220, null=True, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=220, null=True, blank=True, verbose_name='Телефон')
    bank = models.CharField(max_length=220, null=True, blank=True, verbose_name='Банк')
    checking_account = models.CharField(max_length=220, null=True, blank=True, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=220, null=True, blank=True, verbose_name='БИК')
    status = models.CharField(max_length=220, null=True, blank=True, verbose_name='Статус')
    reg_date = models.CharField(max_length=220, null=True, blank=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name


# Tenderi
class Tender(models.Model):
    tenders_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    org_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Название организации')
    purchases_metod = models.CharField(max_length=220, null=True, blank=True, verbose_name='Метод закупок')
    date_start = models.CharField(max_length=220, null=True, blank=True, verbose_name='Дата публикации')
    date_end = models.CharField(max_length=220, null=True, blank=True, verbose_name='Дата завершения')
    gokz = models.CharField(max_length=220, null=True, blank=True, verbose_name='Гарантийное обеспечение конкурсной заявки')
    purchases_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Наименование закупки')
    purchases_format = models.CharField(max_length=220, null=True, blank=True, verbose_name='Формат закупки')
    planned_amount = models.CharField(max_length=220, null=True, blank=True, verbose_name='Планируемая сумма')
    valuta = models.CharField(max_length=220, null=True, blank=True, verbose_name='Валюта конкурса')
    validity = models.CharField(max_length=220, null=True, blank=True, verbose_name='Срок действия конкурсных заявок')

    def __str__(self):
        return self.tenders_num


class Lot(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    lots_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Наименование лота')
    lots_amount = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма')
    address = models.CharField(max_length=220, null=True, blank=True, verbose_name='Адрес и место поставки')
    condition = models.CharField(max_length=220, null=True, blank=True, verbose_name='Условие поставки')
    timing = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сроки поставки')

    def __str__(self):
        return self.tender_num


class Submission(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lot_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма предложения')
    org_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Название организации')
    valuta = models.CharField(max_length=220, null=True, blank=True, verbose_name='Валюта')
    gokz_sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='ГОКЗ сумма')
    gokz_form = models.CharField(max_length=220, null=True, blank=True, verbose_name='ГОКЗ форма')
    tax_date = models.CharField(max_length=220, null=True, blank=True, verbose_name='Налог на')
    tax_status = models.CharField(max_length=220, null=True, blank=True, verbose_name='Налог статус')
    soc_date = models.CharField(max_length=220, null=True, blank=True, verbose_name='Соцфонд на')
    soc_status = models.CharField(max_length=220, null=True, blank=True, verbose_name='Соцфонд статус')

    def __str__(self):
        return f'{self.tender_num} / {self.org_name}'


class Product(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    okgz = models.CharField(max_length=220, null=True, blank=True, verbose_name='Класс ОКГЗ')
    measure = models.CharField(max_length=220, null=True, blank=True, verbose_name='Единица измерения')
    count = models.CharField(max_length=220, null=True, blank=True, verbose_name='Количество')
    specification = models.CharField(max_length=220, null=True, blank=True, verbose_name='Спецификация')
    file = models.CharField(max_length=220, null=True, blank=True, verbose_name='Файл')

    def __str__(self):
        return self.specification


class Winner(models.Model):
    tender_num = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер тендера')
    lots_number = models.CharField(max_length=220, null=True, blank=True, verbose_name='Номер лота')
    winner_name = models.CharField(max_length=220, null=True, blank=True, verbose_name='Название победителя')
    winner_status = models.CharField(max_length=220, null=True, blank=True, verbose_name='Статус победителя')
    winner_sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='Сумма победителя')
    canceled_reason = models.CharField(max_length=220, null=True, blank=True, verbose_name='Причина отказа')
    planned_sum = models.CharField(max_length=220, null=True, blank=True, verbose_name='Планируемая сумма')

    def __str__(self):
        return f'{self.tender_num} / {self.winner_name}'
