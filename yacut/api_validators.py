import re
from http import HTTPStatus

from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap

URL_PATTERN = (
    '^https?:\\/{1,2}(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}'
    '\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$'
)

SHORT_URL_PATTERN = r'^[a-zA-Z\d]+$'


def required_fields_validator(data):
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')


def original_url_validator(value):
    match = re.match(URL_PATTERN, value)
    if not match:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')


def short_url_validator(value):
    if len(value) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    match = re.match(SHORT_URL_PATTERN, value)
    if not match:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=value).first() is not None:
        raise InvalidAPIUsage(f'Имя "{value}" уже занято.')


def get_url_obj_validator(short_id):
    url_obj = URLMap.query.filter_by(short=short_id).first()
    if url_obj is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return url_obj


def get_data_in_request_validator(request):
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    return data
