from app import db
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True)
    password_hash=db.Column(db.String)

    def set_password_hash(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password_hash(self,password):
        return check_password_hash(self.password_hash,password)