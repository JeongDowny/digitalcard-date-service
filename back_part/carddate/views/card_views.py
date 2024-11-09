from flask import Blueprint, request, render_template, redirect, url_for, flash

from carddate.forms import ProfileForm
from carddate.models import Profile

bp = Blueprint('card', __name__, url_prefix='/card')

@bp.route('/')
def index():
    return render_template('card_form.html')

@bp.route('/sumbit', method=("POST", ))
def submit():
    # 폼 데이터 가져오기
    name = request.form('name')
    gender = request.form('gender')
    major = request.form('major')
    age = request.form('age')
    mbti = request.form('mbti')
    hobby = request.form('hobby')
    contact = request.form('contact')

    # 데이터 유효성 검사
    if not (gender and age and major and mbti and hobby and name and contact):
        flash('모든 필드를 채워 주세요.')
        return redirect(url_for('card.index'))

    # 데이터베이스에 새로운 프로필 데이터 저장
    try:
        new_profile = Profile(
            gender=gender,
            name=name,
            major=major,
            age=age, 
            mbti=mbti,
            hobby=hobby,
            contact=contact
        )
        db.session.add(new_profile)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # 오류 발생 시 롤백
        flash(f'오류가 발생했습니다: {str(e)}')
        return redirect(url_for('index'))

    # 리다이렉트와 플래시 메시지
    flash('제출해 주셔서 감사합니다!')
    return redirect(url_for('card.thank_you'))
