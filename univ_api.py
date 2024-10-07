from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import requests
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key' # 세션 관리를 위한 비밀 키 추가

API_BASE_URL = 'https://univcert.com/api/v1'
API_KEY = '0a88c9b6-497f-4236-820c-79866b6a4e08'  # 여기에 API 키를 입력하세요


# 학교명 확인
@app.route('/check_university', methods=['POST'])
def check_university():
    school_name = request.json['univName']

    response = requests.post(f'{API_BASE_URL}/check', headers={
        'Content-Type': 'application/json'
    }, json={'univName': school_name})  
    
    result = response.json()
    if result.get('success'):
        return jsonify({'success': True, 'message': '학교 확인 완료!'})
    else:
        return jsonify({'success': False, 'message': '유효한 학교명이 아닙니다.'})


# 이메일 전송
@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.json['email']
    school_name = request.json['univName']

    response = requests.post(f'{API_BASE_URL}/certify', headers={
        'Content-Type': 'application/json'
    }, json=({
        'key': API_KEY,
        'email': email,
        'univName': school_name,
        'univ_check': True
    }))
    
    result = response.json()
    if result.get('success'):
        return jsonify({'success': True, 'message': '이메일 전송 성공! 이메일에서 인증코드를 확인하세요.'})
    else:
        return jsonify({'success': False, 'message': '이메일 전송에 실패했습니다.'})

    
# 인증번호 제출
@app.route('/verify_code', methods=['POST'])
def verify_code():
    code = request.json['code']
    email = request.json['email']
    school_name = request.json['univName']

    response = requests.post(f'{API_BASE_URL}/certifycode', headers={
        'Content-Type': 'application/json'
    }, json={
        'key': API_KEY,
        'email': email,
        'univName': school_name,
        'code': code
    })
    
    result = response.json()
    if result.get('success'):
        return jsonify({'success': True, 'message': '인증 성공!'})
    else:
        return jsonify({'success': False, 'message': '인증번호가 잘못되었습니다.'})

    

# 인증된 이메일 확인
@app.route('/check_status', methods=['POST'])
def check_status():
    email = request.json['email']

    response = requests.post(f'{API_BASE_URL}/status', headers={
        'Content-Type': 'application/json'
    }, json={'key': API_KEY, 'email': email})
    
    
    result = response.json()
    if result.get('success'):
        return jsonify({'success': True, 'message': '이메일이 인증되었습니다.'})
    else:
        return jsonify({'success': False, 'message': '인증되지 않은 이메일입니다.'})

    

# 인증된 유저 리스트 출력
@app.route('/certified_list', methods=['GET'])
def certified_list():
    response = requests.post(f'{API_BASE_URL}/certifiedlist', headers={
        'Content-Type': 'application/json'
    }, json={'key': API_KEY})
    
    result = response.json()
    if result.get('success'):
        return render_template('certified_list.html', users=result['data'])
    else:
        flash('인증된 유저 리스트를 가져오는 데 실패했습니다.')
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
