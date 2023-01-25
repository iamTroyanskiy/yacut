from flask import request, jsonify

from . import app, db
from .api_validators import (
    required_fields_validator,
    original_url_validator,
    short_url_validator
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def get_opinion():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    required_fields_validator(data)
    original = data['url']
    original_url_validator(original)
    short = data.get('custom_id', None)
    if short:
        short_url_validator(short)
    else:
        short = get_unique_short_id()
    data_for_model = dict(
        original=original,
        short=short
    )
    url_obj = URLMap()
    url_obj.from_dict_api(data_for_model)
    db.session.add(url_obj)
    db.session.commit()
    output_data = dict(
        url=original,
        short_link=request.url_root + short
    )
    return jsonify(output_data), 201


@app.route('/api/id/<short_id>/')
def get_original_url(short_id):
    url_obj = URLMap.query.filter_by(short=short_id).first()
    if url_obj is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    url = url_obj.original
    output_data = dict(
        url=url
    )
    return jsonify(output_data), 200
