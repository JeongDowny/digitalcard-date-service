from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from ..models import Profile
from .. import db
from datetime import datetime

bp = Blueprint('card', __name__, url_prefix='/card')


@bp.route('/')
def index():
    return render_template('card_form.html')


@bp.route('/submit', methods=['POST'])
def create():
    try:
        print("Received request")  # 디버깅용
        data = request.get_json()
        print("Received data:", data)  # 디버깅용

        # 새 프로필 생성
        profile = Profile(
            gender=data.get('gender', ''),
            name=data.get('name', ''),
            major=data.get('major', ''),
            age=data.get('age', ''),
            mbti=data.get('mbti', ''),
            hobby=data.get('hobby', ''),
            contact=data.get('contact', ''),
            create_date=datetime.now()
        )

        # 데이터베이스에 저장
        db.session.add(profile)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': '프로필이 저장되었습니다.'
        })

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # 디버깅용
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500