from app import app, db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from datetime import datetime

with app.app_context():
   

    
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

  
    u1 = User(username="admin")
    u1.set_password_hash("admin123")

    u2 = User(username="john")
    u2.set_password_hash("johnpass")

    db.session.add_all([u1, u2])
    db.session.commit()


    g1 = Guest(name="Zendaya", occupation="Actress")
    g2 = Guest(name="Elon Musk", occupation="Entrepreneur")
    g3 = Guest(name="Bill Nye", occupation="Scientist")

    db.session.add_all([g1, g2, g3])
    db.session.commit()

    ep1 = Episode(date=datetime(2024, 6, 1, 22, 0), number=101)
    ep2 = Episode(date=datetime(2024, 6, 2, 22, 0), number=102)

    db.session.add_all([ep1, ep2])
    db.session.commit()

   
    a1 = Appearance(rating=5, guest_id=g1.id, episode_id=ep1.id)
    a2 = Appearance(rating=4, guest_id=g2.id, episode_id=ep1.id)
    a3 = Appearance(rating=3, guest_id=g3.id, episode_id=ep2.id)

    db.session.add_all([a1, a2, a3])
    db.session.commit()

