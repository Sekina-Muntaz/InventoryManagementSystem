from app import db
from datetime import datetime
class StocksModel(db.Model):
    __tablename__="new_stocks"
    id=db.Column(db.Integer,primary_key=True)
    quantity=db.Column(db.Integer)
    inv_id=db.Column(db.Integer, db.ForeignKey("new_inventories.id"))
    created_at=db.Column(db.DateTime,default=datetime.utcnow )
    
