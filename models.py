from app import db

class Advertisement(db.Model):
    
    __tablename__ = 'advertisements'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)
