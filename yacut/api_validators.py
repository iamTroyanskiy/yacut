import re

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
