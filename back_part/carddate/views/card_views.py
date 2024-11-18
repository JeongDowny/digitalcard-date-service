from flask import Blueprint, request, render_template, redirect, url_for, flash, session
import requests
from werkzeug.utils import redirect

from ..forms import ProfileForm
from ..models import Profile
from .. import db

from datetime import datetime

bp = Blueprint('card', __name__, url_prefix='/card')

@bp.route('/')
def index():
    if'user_email' in session:
        return render_template('card_form.html')
    return redirect(url_for('login.index'))

@bp.route('/create', methods=("POST", ))
def create():
    form = ProfileForm()

    if form.validate_on_submit():
        profile = Profile(
            name = form.name.data,
            gender = form.gender.data,
            major = form.major.data,
            age = form.age.data,
            mbti = form.mbti.data,
            hobby = form.hobby.data,
            contact = form.contact.data,
            create_date = datetime.now()
        )
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for())
    return render_template('card_form.html')