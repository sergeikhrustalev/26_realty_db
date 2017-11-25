from app import db


class Advertisement(db.Model):

    __tablename__ = 'advertisements'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=False,
        index=True
    )
    
    settlement = db.Column(db.String(127))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    oblast_district = db.Column(db.String(127), index=True)
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(255))
    construction_year = db.Column(db.Integer)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean, default=True)
