import requests
import datetime
import pymorphy2
import time
from . import func_db

exceptionss = [",", ".", "!", "?", ":", "-", "+", "=", ")"]


### PARSING ###

def _Parcing(domain, new_time):  # Функция получения всех данных с группы фудшеринга
    token = "1310b4b31310b4b31310b4b3591362059b113101310b4b34dfda7ad3dd06b226e378da4"  # токен api vk
    version = 5.92
    all_post = []

    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': 100
                            })
    data = response.json()['response']['items']
    data_of_scoping = datetime.datetime.now().strftime('%Y-%m-%d')

    for i in range(len(data)):  # отсеивание старых постов группы
        if datetime.datetime.fromtimestamp(data[i].get('date')).strftime(  # проверка "свежести" по сегодняшнему дню
                '%Y-%m-%d') == data_of_scoping and data[i].get('marked_as_ads') == 0:
            if datetime.datetime.fromtimestamp(data[i].get('date')).strftime(
                    "%H:%M") >= new_time:  # проверка по времени
                all_post.append(data[i])

    return all_post


### FOOD ###

def _Food(data, users_categories,
          cities):  # функция парсинга текста поста группы на наличие той или иной категории еды пользователя
    morph = pymorphy2.MorphAnalyzer()
    categories = {
        "Овощи": func_db.select_category("Овощи"),
        "Фрукты": func_db.select_category("Фрукты"),
        "Сдобное": func_db.select_category("Сдобное"),
        "Сладости": func_db.select_category("Сладости"),
        "Напитки": func_db.select_category("Напитки"),
        "Мясо": func_db.select_category("Мясо")
    }
    data_with_request = {}
    for wanted_food in users_categories:
        category = categories[wanted_food]
        data_with_request[wanted_food] = []
        data_with_request["Город"] = []
        for i in data:  # Парсинг постов
            text = i.get('text').split()
            try:
                for j in text:  # Парсинг текста поста
                    if j[-1] in exceptionss:
                        j = j[:-1]

                    if morph.parse(j.rstrip().lower())[
                        0].normal_form in category:  # проверка на сходимость каждого слова с библиотекой категорий
                        data_with_request[wanted_food].append(
                            "https://vk.com/wall-" + str(i.get('owner_id'))[1:] + "_" + str(i.get('id')))

                        for h in text:  # проверка на сходимость каждого слова с библиотекой городов
                            if h[-1] in exceptionss:
                                h = h[:-1]
                            if morph.parse(h.rstrip().lower())[0].normal_form in cities:
                                data_with_request["Город"].append(morph.parse(h.rstrip().lower())[0].normal_form)
                                break
                        else:
                            data_with_request["Город"].append("all")

                        break

            except NameError:
                continue
            except IndexError:
                pass
    return data_with_request
