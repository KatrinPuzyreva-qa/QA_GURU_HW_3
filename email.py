import datetime


#1 Создайте словарь email
email = {
    "subject": "Телеграмма",
    "from": "email@Company.ru",
    "to": "email@Gmail.com",
    "body": "Hello Mentors,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}


#2 Добавьте дату отправки
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date


#3 Нормализуйте e-mail адреса
email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()


#4 Извлеките логин и домен отправителя
login, domain = email["from"].split("@")


#5 Создайте сокращённую версию текста
if len(email["body"]) > 10:
    short_body = email["body"][:10] + "..."
else:
    short_body = email["body"]

email["short_body"] = short_body


#6 Списки доменов
personal_domains = list({'gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru',
                        'mail.ru','list.ru','bk.ru','inbox.ru'})
corporate_domains = list({'company.ru','corporation.com','university.edu','organization.org','company.ru',
  'business.net'})


#7 Проверьте что в списке личных и корпоративных доменов нет пересечений
intersection = set(personal_domains).intersection(corporate_domains)
assert not intersection, f"Перекрытие доменов обнаружено: {intersection}"


#8 Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domains
email ['is_corporate'] = is_corporate


#9 Соберите «чистый» текст сообщения
clean_body = email["body"].replace("\t", " ").replace("\n", " ")
email["clean_body"] = clean_body


#10 Сформируйте текст отправленного письма
sent_text = f'''Кому: {email["to"]}
От: {email["from"]}
Тема: {email["subject"]}
Дата: {email["date"]}
{email["clean_body"]}'''
email["sent_text"] = sent_text


#11 Рассчитайте количество страниц печати
pages = (len(sent_text) + 499) // 500


#12 Проверьте пустоту темы и тела письма
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()


#13 Создайте «маску» e-mail отправителя
masked_from = f'{login[:2]}***@{domain}'
email['masked_from'] = masked_from

#14 Удалите из списка личных доменов
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")


#15 # Вывод всех результатов
print("Логин:", login)
print("Домен:", domain)
print("Количество страниц:", pages)
print("Тема пустая:", is_subject_empty)
print("Тело письма пустое:", is_body_empty)
print("Маска отправителя:", email["masked_from"])
print("Корпоративный отправитель:", is_corporate)
print("\\nEmail словарь:")
print(email)