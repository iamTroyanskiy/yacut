from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Regexp


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле!'),
            URL(message='Введите корректный URL!'),
        ]
    )
    custom_id = StringField(
        'Ваш вариант ссылки',
        validators=[
            Length(0, 16, message='Максимальная длина - 16 символов!'),
            Regexp(
                r'^[A-Za-z\d]*$',
                message='Должен содержать только цифры и латинские буквы!'
            )
        ]
    )
    submit = SubmitField('Создать')
