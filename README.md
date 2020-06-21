# free-food 
## FreeFood - фудшеринг чат-бот 
Этот чат-бот создан, чтобы «спасать» пригодную для употребления пищу. Бот для социальной сети «ВКонтакте» помогает найти бесплатные продукты заданной пользователем категории или категорий и отправляет ему релевантные сообщения. Переходя по объявлениям прямо в сообщениях, человек сможет первым зарезервировать эти продукты для себя. Пользователь имеет возможность указывать конкретные сообщества и получать актуальные записи в режиме реального времени.
Стек решений:
- vk_api
- Python
- SQLite
- pymorphy2
	
Уникальность: Возможность указания конкретных сообществ, рассылка актуальных объявлений в режиме реального времени, приятный интерфейс.

## Инструкция по запуску
- [ ] Запустите модуль create_db.py, чтобы создать/обновить базу данных.
- [ ] Запустите модуль main.py.
- [ ] Profit!

## Инструкция по пользованию
- [ ] Перейдите по ссылке к чат боту [FreeFood](https://vk.com/freefood_app), авторизируйтесь в "Вконтакте" и перейдите в диалог с ботом.
- [ ] Введите ваш город, который будет использоваться для тщательной фильтрации объявлений.
- [ ] Введите ссылки на группу/группы с фудшеринговой тематикой.
- [ ] Выберите категории для поиска нужных Вам видов продуктов и начните поиск.
- [ ] Бот проверяет новые записи и уведомляет пользователей о нахождении подходящих им объявлений.
- [ ] Путем нажатия на кнопку "Остановить поиск", бот прекращает уведомлять о релевантных для Вас объявлениях.

## Используемые библиотеки в Python 
- requests
- re
- sqlite3
- pymorphy2
- datetime
- os
- json
- vk_api
- random
- time
