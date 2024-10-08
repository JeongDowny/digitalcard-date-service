from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])

class ProfileForm(FlaskForm):
    name = StringField('이름', validators=[DataRequired(), Length(max=100)])  # 이름
    gender = StringField('성별', validators=[DataRequired(), Length(max=10)])  # 성별
    age = IntegerField('나이', validators=[DataRequired()])  # 나이
    major = StringField('학과', validators=[DataRequired(), Length(max=100)])  # 학과
    mbti = StringField('MBTI', validators=[DataRequired(), Length(min=4, max=4)])  # MBTI, 4글자
    hobbies = TextAreaField('취미', validators=[Length(max=200)])  # 취미, 선택사항
    phone = StringField('연락처', validators=[
        DataRequired(),
        Regexp(r'^\d{3}-\d{3,4}-\d{4}$', message="올바른 연락처 형식이 아닙니다. (예: 010-1234-5678)")
    ])  # 연락처