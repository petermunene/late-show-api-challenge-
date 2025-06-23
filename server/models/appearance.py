from app import db 
from sqlalchemy.orm import validates
class Appearance (db.Model):
    __tablename__='appearances'
    id = db.Column(db.Integer , primary_key=True)
    rating=db.Column(db.Integer)
    guest_id=db.Column(db.Integer,db.ForeignKey('guests.id',ondelete='CASCADE'))
    episode_id=db.Column(db.Integer,db.ForeignKey('episodes.id',ondelete='CASCADE'))
    
    
    guest=db.relationship('Guest',back_populates='appearances')
    episode=db.relationship('Episode',back_populates='appearances')
    @validates('rating')
    def rating_validation(self,key, value ):
        if not (1<=value<=5):
            raise ValueError('invalid rating')
        return value


