from datetime import datetime

from . import db
from .utils import get_unique_short_id


class URLMap(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    original = db.Column(
        db.Text,
        nullable=False
    )
    short = db.Column(
        db.String(16),
        unique=True,
        nullable=False,
        default=get_unique_short_id
    )
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.utcnow
    )

    def to_dict_api(self):
        return dict(
            url=self.original,
        )

    def from_dict_api(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
