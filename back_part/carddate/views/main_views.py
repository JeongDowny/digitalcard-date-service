from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from carddate.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'