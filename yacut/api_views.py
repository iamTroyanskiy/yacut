from http import HTTPStatus

from flask import request, jsonify
from sqlalchemy import exc

from . import app, db
from .api_validators import (
    required_fields_validator,
    original_url_validator,
    short_url_validator,
    get_url_obj_validator,
    get_data_in_request_validator,
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def get_opinion():
    data = get_data_in_request_validator(request)
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
    try:
        db.session.add(url_obj)
        db.session.commit()
    except exc.SQLAlchemyError:
        raise InvalidAPIUsage('Введены невалидные данные')
    output_data = dict(
        url=original,
        short_link=request.url_root + short
    )
    return jsonify(output_data), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/')
def get_original_url(short_id):
    url_obj = get_url_obj_validator(short_id)
    url = url_obj.original
    output_data = dict(
        url=url
    )
    return jsonify(output_data), HTTPStatus.OK
