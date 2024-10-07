from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///date.db'  # SQLite 데이터베이스 설정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Flash 메시지를 위한 시크릿 키 설정
db = SQLAlchemy(app)

# 데이터베이스 모델 정의
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)
    mbti = db.Column(db.String(5), nullable=False)
    hobby = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    create_date = db.Column(db.DateTime(), default=datetime.now)

# 기본 페이지 라우트 - card_form.html 렌더링
@app.route('/')
def index():
    return render_template('card_form.html')

# 데이터 제출 처리
@app.route('/submit', methods=['POST'])
def submit():
    # 폼 데이터 가져오기
    gender = request.form.get('gender')
    age = request.form.get('age')
    major = request.form.get('major')
    mbti = request.form.get('mbti')
    hobby = request.form.get('hobby')
    name = request.form.get('name')
    contact = request.form.get('contact')

    # 데이터 유효성 검사
    if not (gender and age and major and mbti and hobby and name and contact):
        flash('모든 필드를 채워 주세요.')
        return redirect(url_for('index'))

    # 데이터베이스에 새로운 프로필 데이터 저장
    try:
        new_profile = Profile(
            name=name,
            gender=gender,
            age=int(age),  # 나이를 정수형으로 변환
            major=major,
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
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    # 데이터베이스 생성
    with app.app_context():
        db.create_all()
    app.run(debug=True)
