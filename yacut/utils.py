import random
import string

from .settings import MAX_URL_SIZE


ALLOWED = string.ascii_letters + string.digits


def get_unique_short_id():
    short_id = ''.join(random.choices(ALLOWED, k=MAX_URL_SIZE))
    from .models import URLMap
    if URLMap.query.filter_by(short=short_id).first():
        return get_unique_short_id()
    return short_id
