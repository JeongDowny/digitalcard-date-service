from flask import Flask, request, render_template, redirect, url_for, flash
import requests
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Flash 메시지를 사용하려면 secret key가 필요

API_BASE_URL = 'https://univcert.com/api/v1'
API_KEY = '0a88c9b6-497f-4236-820c-79866b6a4e08'  # 여기에 API 키를 입력하세요

# 홈 페이지
@app.route('/')
def home():
    return render_template('index.html')

# 학교명 확인
@app.route('/check_university', methods=['POST'])
def check_university():
    school_name = request.form['school_name']

    response = requests.post(f'{API_BASE_URL}/check', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'univName': school_name
    }))
    
    result = response.json()
    if result.get('success'):
        flash('학교 확인 완료!')
        # 이메일 입력으로 넘어감
    else:
        flash('유효한 학교명이 아닙니다.')

    return redirect(url_for('home'))

# 이메일 전송
@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    school_name = request.form['school_name']

    response = requests.post(f'{API_BASE_URL}/certify', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'key': API_KEY,
        'email': email,
        'univName': school_name,
        'univ_check': True
    }))
    
    result = response.json()
    if result.get('success'):
        flash('이메일 전송 성공! 이메일에서 인증코드를 확인하세요.')
    else:
        flash('이메일 전송에 실패했습니다.')

    return redirect(url_for('home'))

# 인증번호 제출
@app.route('/verify_code', methods=['POST'])
def verify_code():
    code = request.form['code']
    email = request.form['email']
    school_name = request.form['school_name']

    response = requests.post(f'{API_BASE_URL}/certifycode', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'key': API_KEY,
        'email': email,
        'univName': school_name,
        'code': code
    }))
    
    result = response.json()
    if result.get('success'):
        flash('인증 성공! 2초 후 다음 페이지로 이동합니다.')
        return redirect(url_for('card_writing'))
    else:
        flash('인증번호가 잘못되었습니다.')

    return redirect(url_for('home'))

# 인증된 이메일 확인
@app.route('/check_status', methods=['POST'])
def check_status():
    email = request.form['email']

    response = requests.post(f'{API_BASE_URL}/status', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'key': API_KEY,
        'email': email
    }))
    
    result = response.json()
    if result.get('success'):
        flash('이메일이 인증되었습니다.')
    else:
        flash('인증되지 않은 이메일입니다.')

    return redirect(url_for('home'))

# 인증된 유저 리스트 출력
@app.route('/certified_list', methods=['GET'])
def certified_list():
    response = requests.post(f'{API_BASE_URL}/certifiedlist', headers={
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'key': API_KEY
    }))
    
    result = response.json()
    if result.get('success'):
        return render_template('certified_list.html', users=result['data'])
    else:
        flash('인증된 유저 리스트를 가져오는 데 실패했습니다.')

    return redirect(url_for('home'))

# 카드 작성 페이지 (인증 성공 후 이동할 페이지)
@app.route('/card_writing')
def card_writing():
    return render_template('card_writing.html')

if __name__ == '__main__':
    app.run(debug=True)
