from flask import Blueprint, Flask, render_template, request, flash, redirect, session, url_for

from webapp.utils import get_redirect_target


blueprint = Blueprint('cont', __name__, url_prefix='/cont')


@blueprint.route('/<city_id>')
def city_content(city_id):
    session.pop("city", None)
    session["city"] = city_id
    return redirect(get_redirect_target())

@blueprint.route('/about')
def about_dg():
    title = "Узнай больше о диск-гольфе"
    return render_template('cont/about.html', page_title=title)

@blueprint.route('/mclass')
def mclass():
    title = "Попробуй поиграть в диск-гольф"
    return render_template('cont/mclass.html', page_title=title)

@blueprint.route('/where')
def where():
    title = "Где можно поиграть в диск-гольфа"
    return render_template('cont/where.html', page_title=title)

@blueprint.route('/beginner')
def beginner():
    title = "Попробуй посоревноваться"
    return render_template('cont/beginner.html', page_title=title)

@blueprint.route('/protour')
def protour():
    title = "Зарубись с профессионалами диск-гольфа"
    return render_template('cont/protour.html', page_title=title)

@blueprint.route('/sponsorship')
def sponsor():
    title = "Поддержи развитие диск-гольфа"
    return render_template('cont/sponsorship.html', page_title=title)

@blueprint.route('/tobuy')
def tobuy():
    title = "Где купить диски и корзины"
    return render_template('cont/tobuy.html', page_title=title)

@blueprint.route('/corp')
def corp():
    title = "Провести праздник диск-гольфа"
    return render_template('cont/corp.html', page_title=title)
