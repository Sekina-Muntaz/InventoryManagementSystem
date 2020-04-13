from app import db
class salesModel(db.Model):
    __tablename__="new_sales"

    id=db.Column(db.Integer,primary_key=True)
    quantity=db.Column(db.Integer,nullable=False)
    inv_id=db.Column(db.Integer,nullable=False)
    created_at=db.Column(db.DateTime,nullable=False)