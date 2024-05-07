# DjangoPetTest

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Задание проекта

На основе django и БД PostgreSQL сделать следующее:

1. Web страничка с формой (название, полигон). Например, это можно сделать в виде 2 полей (широта долгота в десятичных градусах) по нажатию на кнопку «Добавить» данные этих полей попадают в поле textarea и поле название полигона.
2. По нажатию на кнопку «Submit» данные формы отправляются на сервер и сохраняются в БД в виде PolygonField (<https://docs.djangoproject.com/en/4.2/ref/contrib/gis/model-api/#polygonfield>). Это потребует также добавить postgis расширение для postgres БД.
3. Web-табличка в которой есть все сохраненные объекты (Колонки: Название, Полигон в виде списка координат, признак пересечения антимеридиана (True/False)). Этот признак можно хранить в БД отдельным полем. Также учесть такую возможность что координаты могут пересекать антимеридиан. То есть могут быть координаты, например, [[69.3493386397765, 174.19921875000003], [69.3493386397765, 204.96093750000003], [62.103882522897884, 205.48828125000003], [62.186013857194226, 173.67187500000003]] И в данном случае нужно преобразовать выделенные координаты в [69.3493386397765, -155.1], [62.103882522897884, - 154.512] и проставить признак того что полигон проходит через антимеридиан.
4. С помощью DRF создать несколько endpoint для запросов на удаление, добавление, просмотр и редактирование.

Плюсом будет:

1. Развернуть все в Docker отдельными контейнерами.
2. Использовать gunicorn/daphne для эмуляции развертывания в рабочей среде.
3. Использовать pgAdmin для визуального отображения PostgreSQL.
4. Составить мануал для разработчика.
По версиям django, postgresql ограничений нет, все зависимости django нужно указать в файле requrements.txt и использовать утилиту виртуального окружения virtualenv. На стороне веб можно использовать bootstrap, jquery

## Предварительные настройки

* Установить пакеты

```bash
brew install postgresql
brew install postgis
brew install gdal
brew install libgeoip
```

* Создать базу, объявить пользователя, пароль и разрешения

```sql
CREATE DATABASE db_name;
CREATE USER postgres WITH PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE db_name TO postgres;

CREATE EXTENSION postgis;
```

* Дополнить settings.py

```python
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "webpolygon",
        "USER": "postgres",
        "PASSWORD": "test",
        "HOST": "localhost",
        "PORT": "",
    }
}
```