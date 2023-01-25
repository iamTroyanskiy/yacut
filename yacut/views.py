from flask import render_template, request, flash, redirect
from . import app, db
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET'])
def index_view():
    form = URLForm()
    return render_template('index.html', form=form)


@app.route('/', methods=['POST'])
def index_post_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        if custom_id:
            if URLMap.query.filter_by(short=custom_id).first():
                flash(f'Имя {custom_id} уже занято!', 'custom-id')
                return render_template('index.html', form=form)
            url_obj = URLMap(
                original=original_link,
                short=custom_id
            )
        else:
            url_obj = URLMap(
                original=original_link
            )
        db.session.add(url_obj)
        db.session.commit()
        custom_url = request.url_root + url_obj.short
        return render_template('index.html', custom_url=custom_url, form=form)
    return render_template('index.html', form=form)


@app.route('/<string:custom_id>', methods=['GET'])
def redirect_to_original_url_view(custom_id):
    url_obj = URLMap.query.filter_by(short=custom_id).first_or_404()
    original_link = url_obj.original
    return redirect(original_link)
