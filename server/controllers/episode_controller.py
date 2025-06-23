from flask import Blueprint,request,jsonify
from server import db
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance

episode_bp=Blueprint('episode',__name__)

@episode_bp.route('/episodes',methods=['GET'])
def get_episodes():
    episodes= Episode.query.all()
    if episodes:
        return jsonify([{"id":e.id,"date":e.date.isoformat(),"number":e.number} for e in episodes]),200

@episode_bp.route('/episodes/<int:id>',methods=['GET'])
def get_episode_by_id(id):
    e=Episode.query.filter(Episode.id==id).first()
    appearances=Appearance.query.filter(Appearance.episode_id==id).all()
    if not e:
        return jsonify({'error':'episode does not exist'}),404
    data={
        'id':e.id,
        'date':e.date.isoformat(),
        'number':e.number,
        "appearances":[{
            'id':a.id,
            'rating':a.rating,
            'guest_id':a.guest_id,
            'episode_id':a.episode_id
        }for a in appearances ]
    }
    return jsonify(data)

@episode_bp.route('/episodes/<int:id>',methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    e=Episode.query.get(id)
    if e:
        db.session.delete(e)
        db.session.commit()
        return "",204
    else:
        return jsonify({'error':'episode does not exist'}),404
