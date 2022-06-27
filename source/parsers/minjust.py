import datetime
import multiprocessing
import time

import requests
# import telebot
from bs4 import BeautifulSoup

from webapp.models import Firma

# bot = telebot.TeleBot('5390689400:AAHJ7w8vJsY9zxpPd8BsF4BRUvTrbeY5mPM')
# для нового пользователя
# 659261315 акыл
# @bot.message_handler(commands=['start'])
# def start(message):
#     print(message.chat.id)
#     bot.send_message(659261315, 'It works!')
# bot.polling()
# для отправки

# bot = telebot.TeleBot('1872481226:AAGh_k5eWvDIA05V9AsMpOlylvyuYHZ78yQ')
# # bot.send_message(659261315, 'It works!')
#
# bot.send_message(659261315, f'Начал парсинг минюста - {datetime.datetime.now()}')
# bot = telebot.TeleBot("1872481226:AAGh_k5eWvDIA05V9AsMpOlylvyuYHZ78yQ")


def load_link(link):
    load_count = 0
    try:
        page = requests.get(link, timeout=100)
    except:
        # print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        # bot.send_message(659261315, f'Мин юст - ошибка в загрузке страницы {link}')
        time.sleep(10)
        if load_count < 30:
            page = load_link(link)
        else:
            page = False
    return page


def get_data(html, text, error_text):
    try:
        title = html.find("span", text=text)
        sibling_text_elem = (
            title.find_parent().find_parent().find_next_sibling().find_next_sibling()
        )
        if sibling_text_elem:
            sibling_text = sibling_text_elem.text.replace("\xa0", "")
        else:
            sibling_text = ""
    except:
        # bot.send_message(659261315, 'Мин юст - ' + error_text)
        sibling_text = ""
    return sibling_text


def compare(obj, obj_field, field_name, old_value, new_value):
    if obj_field == "founders":
        if len(old_value) == len(new_value):
            for i in range(len(old_value)):
                old_value[i] = old_value[i].replace('"', "")
            for value in new_value:
                value = value.replace("'", "").replace('"', "")
                if value not in old_value:
                    # bot.send_message(659261315, f'есть изменения в {obj.inn} - {field_name} - {old_value} - {new_value}')
                    # print(
                    #     f"!!!есть изменения в {obj.inn} - {field_name} - {old_value} - {new_value}"
                    # )
                    obj.history.create(
                        firm=obj,
                        field_name=field_name,
                        old_data=old_value,
                        new_data=str(new_value).replace("\xa0", ""),
                    )
                    setattr(obj, obj_field, str(new_value))
                    obj.save()
                    break
        elif old_value == [""] and new_value == []:
            pass
        else:
            # bot.send_message(659261315, f'есть изменения в {obj.inn} - {field_name} - {old_value} - {new_value}')
            # print(
            #     f"!!!есть изменения в {obj.inn} - {field_name} - {old_value} - {new_value}"
            # )
            obj.history.create(
                firm=obj,
                field_name=field_name,
                old_data=old_value,
                new_data=str(new_value),
            )
            setattr(obj, obj_field, str(new_value))
            obj.save()
    else:
        if old_value != new_value:
            if old_value is not None and new_value.strip(" ") != "":
                # print(
                #     f"!!!есть изменения в {obj.inn} - {field_name} - {old_value} - {new_value}"
                # )
                # bot.send_message(659261315, f'есть изменения в {obj.inn} - {field_name} - {old_value} - {new_value}')
                obj.history.create(
                    firm=obj,
                    field_name=field_name,
                    old_data=old_value,
                    new_data=new_value,
                )
                setattr(obj, obj_field, new_value)
                obj.save()


# def parse_minjust(count_start, end):
def parse_minjust():
    count_start = 0

    print('started!!!!!!!')
    to_count = load_link(
        "https://register.minjust.gov.kg/register/SearchAction.seam?firstResult=50"
    )
    bs_to_count = BeautifulSoup(to_count.text, "html.parser")
    count_div = bs_to_count.find("div", {"class": "rich-panel-header"})
    # print(count_div.text)
    count = int(count_div.text.split("(")[1].strip(" )"))

    # bot = telebot.TeleBot("1872481226:AAGh_k5eWvDIA05V9AsMpOlylvyuYHZ78yQ")
    # bot.send_message(659261315, 'It works!')

    # bot.send_message(659261315, f"Начал парсинг минюста - {datetime.datetime.now()}")
    try:
        while True:
            print(count_start)
            if count_start >= count:
                # print(f"Мин юст - закончил до {end}")
                # bot.send_message(659261315, f"Мин юст - закончил 10к до {end}")
                break
            main = load_link(
                f"https://register.minjust.gov.kg/register/SearchAction.seam?firstResult={count_start}&logic=and&cid=4738576"
            )
            count_start += 25
            bs_html = BeautifulSoup(main.text, "html.parser")
            table_div = bs_html.find("div", {"class": "results"})
            if not table_div:
                continue
            trs = table_div.find("tbody").findAll("tr")
            for tr in trs:
                link = tr.find("a")
                href = link.get("href")
                print(href)
                # print("https://register.minjust.gov.kg/" + href)
                detail = load_link("https://register.minjust.gov.kg/" + href)
                # print(detail)
                if not detail:
                    # tr_error = True
                    # bot.send_message(659261315, f'Мин юст - нет детейла на {href}, иду дальше')
                    continue
                detail_html = BeautifulSoup(detail.text, "html.parser")
                full_name_kg = get_data(
                    detail_html,
                    "1. Полное наименование(на государственном языке)",
                    "ошибка в full_name_kg",
                )
                full_name_ru = get_data(
                    detail_html,
                    "2. Полное наименование на официальном языке",
                    "ошибка в full_name_ru",
                )
                short_name_kg = get_data(
                    detail_html,
                    "3. Сокрашенное наименование(на государственном языке)",
                    f"ошибка в short_name_kg в {full_name_ru}",
                )
                short_name_ru = get_data(
                    detail_html,
                    "4. Сокрашенное наименование(на официальном языке)",
                    f"ошибка в short_name_ru в {full_name_ru}",
                )
                org_form = get_data(
                    detail_html,
                    "5. Организационно-правовая форма",
                    f"ошибка в org_form в {full_name_ru}",
                )
                foreign_founders = get_data(
                    detail_html,
                    "6. Есть ли иностранное участие",
                    f"ошибка в foreign_founders в {full_name_ru}",
                )
                registration_number = get_data(
                    detail_html,
                    "7. Регистрационный номер",
                    f"ошибка в registration_number в {full_name_ru}",
                )
                try:
                    sibling_okpo_cod = detail_html.find("span", text="8. Код ОКПО")
                    okpo_cod_siblings = (
                        sibling_okpo_cod.find_parent()
                        .find_parent()
                        .find_parent()
                        .find_next_sibling()
                        .findChildren(recursive=False)
                    )
                    okpo_cod = okpo_cod_siblings[2].text.replace("\xa0", "")
                except:
                    # bot.send_message(659261315, f'Мин юст - ошибка в okpo_cod  в {full_name_ru}')
                    okpo_cod = ""

                inn = get_data(detail_html, "9. ИНН", f"ошибка в inn в {full_name_ru}")
                address_region = get_data(
                    detail_html,
                    "10. Область",
                    f"ошибка в address_region в {full_name_ru}",
                )
                address_district = get_data(
                    detail_html,
                    "11. Район",
                    f"ошибка в address_district в {full_name_ru}",
                )
                address_city = get_data(
                    detail_html,
                    "12. Город/село/поселок",
                    f"ошибка в address_city в {full_name_ru}",
                )
                address_microdistrict = get_data(
                    detail_html,
                    "13. Микрорайон",
                    f"ошибка в address_microdistrict в {full_name_ru}",
                )
                address_street = get_data(
                    detail_html,
                    "14. Улица (проспект, бульвар, переулок и т.п.)",
                    f"ошибка в address_street в {full_name_ru}",
                )
                house_number = get_data(
                    detail_html, "15. № дома", f"ошибка в house_number в {full_name_ru}"
                )
                apartment_number = get_data(
                    detail_html,
                    "16. № квартиры (офиса, комнаты и т.п.)",
                    f"ошибка в apartment_number в {full_name_ru}",
                )
                phone = get_data(
                    detail_html, "17. Телефон", f"ошибка в phone в {full_name_ru}"
                )
                fax = get_data(
                    detail_html, "18. Факс", f"ошибка в fax в {full_name_ru}"
                )
                email = get_data(
                    detail_html,
                    "19. Электронный адрес",
                    f"ошибка в email в {full_name_ru}",
                )
                reg_or_rereg = get_data(
                    detail_html,
                    "20. Государственная (учетная) регистрация или перерегистрация",
                    f"ошибка в reg_or_rereg в {full_name_ru}",
                )
                order_date = get_data(
                    detail_html,
                    "21. Дата приказа",
                    f"ошибка в order_date в {full_name_ru}",
                )
                first_reg_date = get_data(
                    detail_html,
                    "22. Дата первичной регистрации (в случае государственной перерегистрации)",
                    f"ошибка в order_date в {full_name_ru}",
                )
                creation_method = get_data(
                    detail_html,
                    "23. Способ создания",
                    f"ошибка в creation_method в {full_name_ru}",
                )
                type_of_ownership = get_data(
                    detail_html,
                    "24. Форма собственности",
                    f"ошибка в type_of_ownership в {full_name_ru}",
                )
                director = get_data(
                    detail_html,
                    "25. Фамилия, имя, отчество",
                    f"ошибка в director в {full_name_ru}",
                )
                main_activity = get_data(
                    detail_html,
                    "26. Основной вид деятельности",
                    f"ошибка в main_activity в {full_name_ru}",
                )
                try:
                    sibling_economic_activity_code = detail_html.find(
                        "span", text="27. Код экономической деятельности"
                    )
                    economic_activity_code = (
                        sibling_economic_activity_code.find_parent()
                        .find_parent()
                        .find_parent()
                        .find_previous_sibling()
                        .findChildren(recursive=False)[1]
                    )
                    economic_activity_code = economic_activity_code.text.replace(
                        "\xa0", ""
                    )
                except:
                    # bot.send_message(659261315, f'ошибка в economic_activity_code в {full_name_ru}')
                    economic_activity_code = ""
                count_of_founders_ind = get_data(
                    detail_html,
                    "28. Количество учредителей (участников) - физических лиц",
                    f"ошибка в count_of_founders_ind в {full_name_ru}",
                )
                count_of_founders_legal = get_data(
                    detail_html,
                    "29. Количество учредителей (участников) - юридических лиц",
                    f"ошибка в count_of_founders_legal в {full_name_ru}",
                )
                total_count_of_founders = get_data(
                    detail_html,
                    "30. Общее количество учредителей (участников)",
                    f"ошибка в total_count_of_founders в {full_name_ru}",
                )
                sibling_founders = detail_html.findAll(
                    "span", text="Учредитель (участник)"
                )
                founders = []
                if sibling_founders:
                    for sibling_founder in sibling_founders:
                        founder = (
                            sibling_founder.find_parent()
                            .find_parent()
                            .find_next_sibling()
                            .find_next_sibling()
                        )
                        founders.append(founder.text.replace("\xa0", ""))
                url_minjust_site = "https://register.minjust.gov.kg/" + href
                new_data = {
                    "full_name_ru": full_name_ru,
                    "full_name_kg": full_name_kg,
                    "short_name_ru": short_name_ru,
                    "short_name_kg": short_name_kg,
                    "org_form": org_form,
                    "foreign_founders": foreign_founders,
                    "registration_number": registration_number,
                    "okpo_cod": okpo_cod,
                    "inn": inn,
                    "address_region": address_region,
                    "address_district": address_district,
                    "address_microdistrict": address_microdistrict,
                    "address_street": address_street,
                    "address_city": address_city,
                    "house_number": house_number,
                    "apartment_number": apartment_number,
                    "phone": phone,
                    "fax": fax,
                    "email": email,
                    "reg_or_rereg": reg_or_rereg,
                    "order_date": order_date,
                    "first_reg_date": first_reg_date,
                    "creation_method": creation_method,
                    "type_of_ownership": type_of_ownership,
                    "director": director,
                    "main_activity": main_activity,
                    "economic_activity_code": economic_activity_code,
                    "count_of_founders_ind": count_of_founders_ind,
                    "count_of_founders_legal": count_of_founders_legal,
                    "total_count_of_founders": total_count_of_founders,
                    "founders": founders,
                    "url_minjust_site": url_minjust_site,
                }
                # print(new_data)
                # with open('minjust.csv', 'a+', newline='') as file:
                #     writer = csv.writer(file, delimiter='|')
                #     writer.writerow(firm_info)
                try:
                    # print(inn)
                    firma = Firma.objects.get(
                        inn=inn,
                        okpo_cod=okpo_cod,
                        registration_number=registration_number,
                    )
                    print('FIRMA FOUNDED!!!!!!!!!!!')
                    for field in Firma._meta.get_fields():
                        if (
                            field.name != "history"
                            and field.name != "id"
                            and field.name != "url_minjust_site"
                        ):
                            # print(field.name)
                            # print(firma, ' - ', field.name, ' - ', field.verbose_name, ' - ', field.value_from_object(firma), ' - ', new_data[field.name])
                            # bot.send_message(659261315, f'{field.name} - {field.verbose_name} - {field.value} - {new_data[field.name]}')

                            old_value = field.value_from_object(firma)
                            if field.name == "founders":
                                founders_striped = old_value.strip(" []")
                                founders_striped = founders_striped.replace("', '", "|")
                                founders_striped = founders_striped.replace("\xa0", "")
                                founders_striped = founders_striped.replace("'", "")
                                # print(founders_striped)
                                old_value = founders_striped.split("|")

                            compare(
                                firma,
                                field.name,
                                field.verbose_name,
                                old_value,
                                new_data[field.name],
                            )
                            detail_html.decompose()
                except Firma.MultipleObjectsReturned:
                    detail_html.decompose()
                    pass
                except Firma.DoesNotExist:
                    # print(f"!!!Сохраняю новый - {inn}")
                    Firma.objects.create(**new_data)
                    print('NEW CREATED')
                    detail_html.decompose()
            bs_html.decompose()
    except:
        pass
        # bot.send_message(659261315, f"ошибка в вайл на {count_start} и вышел ")


# count = 148000


def cron_parse():
    print('started!!!!!!!')
    to_count = load_link(
        "https://register.minjust.gov.kg/register/SearchAction.seam?firstResult=50"
    )
    bs_to_count = BeautifulSoup(to_count.text, "html.parser")
    count_div = bs_to_count.find("div", {"class": "rich-panel-header"})
    # print(count_div.text)
    count = int(count_div.text.split("(")[1].strip(" )"))
    count_devided = int(count / 20000)

    for i in range(count_devided + 1):
        t = multiprocessing.Process(
            target=parse_minjust, args=(20000 * i, 20000 * i + 20000)
        )
        t.start()


# bot.send_message(659261315, f'Закончил парсинг минюста - {datetime.datetime.now()}')