import random
from flask import Blueprint, render_template, jsonify, request
from ..models import Profile
from .. import db
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('random', __name__, url_prefix='/random')

@bp.route('/', methods=['GET'])
def index():
    return render_template('randomOpen.html')

@bp.route('/open', methods=['GET'])
def get_random_profile():
    # Profile 모델에서 모든 데이터를 조회
    profiles = Profile.query.all()

    # 프로필이 2개 이상일 경우, 랜덤으로 2개를 선택
    if len(profiles) >= 2:
        random_profiles = random.sample(profiles, 2)  # 랜덤으로 2개 선택

        # 선택한 프로필들을 JSON 형식으로 변환하여 반환
        profiles_data = [{
            'id':profile.id,
            'gender': profile.gender,
            'name': profile.name,
            'age': profile.age,
            'major': profile.major,
            'mbti': profile.mbti,
            'hobby': profile.hobby,
            'contact': profile.contact
        } for profile in random_profiles]

        return jsonify(profiles_data)
    else:
        return jsonify({'error': '2개 이상의 프로필이 존재하지 않습니다.'}), 400

@bp.route('/confirm', methods=['POST'])
def delete_confirmed_profile():
    try:
        # 클라이언트에서 전달된 JSON 데이터에서 id 추출
        data = request.get_json()
        profile_id = data.get('id')

        if not profile_id:
            return jsonify({'error': 'ID is required'}), 400

        # 데이터베이스에서 해당 id의 프로필을 검색
        profile = Profile.query.get(profile_id)
        if not profile:
            return jsonify({'error': 'Profile not found'}), 404

        # 프로필 삭제
        db.session.delete(profile)
        db.session.commit()

        return jsonify({'message': f'Profile with ID {profile_id} has been deleted successfully!'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()  # 에러 발생 시 롤백
        return jsonify({'error': f'Database error: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

