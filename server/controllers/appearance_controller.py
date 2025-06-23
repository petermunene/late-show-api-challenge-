from flask import request,Blueprint,jsonify
from flask_jwt_extended import jwt_required
from app import db
from models.appearance import Appearance

appearance_bp=Blueprint('appearance', __name__)

@appearance_bp.route('/appearances',methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id=data.get("guest_id")
    episode_id=data.get('episode_id')

    a=Appearance(rating=rating,guest_id=guest_id,episode_id=episode_id)
    db.session.add(a)
    db.session.commit()

    return jsonify({
        'id':a.id,
        'rating':a.rating,
        'guest_id':a.guest_id,
        'episode_id':a.episode_id
    }),201