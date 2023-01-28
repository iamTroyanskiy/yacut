<h1 align="center">
  <br>
  <img src="https://github.com/tonik350/img/blob/main/yacut.png?raw=true" width="500"></a>
</h1>

# YaCut
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Jinja2](https://img.shields.io/badge/-Jinja2-464646?style=flat&logo=Jinja&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)


Сервис укорачивания ссылок с web интерфейсом и REST API. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Ключевые возможности сервиса
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Доступны web и api интерфейсы.

## Технологии
- Python 3.10
- Flask 2.0
- Jinja2 3.0
- SQLAlchemy 1.4

## Примеры запросов

**GET** `.../api/id/{short_id}/`
*200*
```
{
  "url": "string"
}
```
*404*
```
{
  "message": "Указанный id не найден"
}
```


**POST** `.../api/id/`
```
{
  "url": "string",
  "custom_id": "string"
}
```
*201*
```
{
  "url": "string",
  "short_link": "string"
}
```
*400*
```
{
  "message": "Отсутствует тело запроса"
}
```


## Шаблон наполнения .env файла
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=SECRET
```


## Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```


