from flask import request,Blueprint,jsonify
from flask_jwt_extended import create_access_token
from server import db
from server.models.user import User

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['POST'])
def register ():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter(User.username==username).first()
    if user:
        return jsonify({"error":"username already exists"}),400
    user=User(username=username)
    user.set_password_hash(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'username':user.username
    }),201

@auth_bp.route('/login',methods=['POST'])
def login ():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter(User.username==username).first()
    if not user or not user.check_password_hash(password):
            return jsonify({'error':'Incorrect login credentials'}),400
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token':access_token}),200
