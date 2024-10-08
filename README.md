﻿# Пульт охраны банка

Данный проект реализован для предотвращения финансовых потерь,а именно внимательно следить за сотрудниками и их операциями.
Реализована возможность отслеживания взиитов пользователей,время их пребывания и выход из хранилища.


## Необходимые условия

Перед запуском проекта убедитесь, что у вас установлены следующие компоненты:

- Python ~3.11.* и выше.
- pip (менеджер пакетов Python)

## Как установить

Используйте `pip` для установки зависимостей:
```python
pip install -r requirements.txt
```

## Настройка проекта

Создайте файл .env там, где находится manage.py и добавьте туда следующие переменные окружения:

SECRET_KEY: Секретный ключ вашего Django проекта.

DEBUG: Установите True для разработки и False для продакшена.

DB_ENGINE: Движок базы данных (например, django.db.backends.postgresql_psycopg2 для PostgreSQL).

DB_HOST: Хост базы данных.

DB_PORT: Порт, на котором работает база данных.

DB_NAME: Название базы данных.

DB_USER: Имя пользователя базы данных.

DB_PASSWORD: Пароль для базы данных.

ALLOWED_HOSTS: Список разрешённых хостов, разделённый запятыми (например, 127.0.0.1).

## Команда запуска

- Для запуска проекта выполните следующую команду в терминале:

```python
python manage.py runserver 127.0.0.1:8000
```

- После запуска, в терминале появится сервер разработки:

![Терминал](https://i.postimg.cc/Zq38ck6Q/image.jpg)

- Переходим по нему и попадаем на наш сайт:

![Сайт](https://i.postimg.cc/c4grYRR9/image.jpg)


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
