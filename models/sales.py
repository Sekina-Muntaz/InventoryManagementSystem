from app import db
from datetime import datetime
class SalesModel(db.Model):
    __tablename__="new_sales"
    id=db.Column(db.Integer,primary_key=True)
    quantity=db.Column(db.Integer)
    inv_id=db.Column(db.Integer,db.ForeignKey("new_inventories.id"))
    created_at=db.Column(db.DateTime,default=datetime.utcnow)


    def add_quantity(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getSalesById(cls, inv_id):
        return cls.query.filter_by(inv_id=inv_id).all()


    '''in the child model:
        - we store the FK and describe it (tablename and which column)
        '''


