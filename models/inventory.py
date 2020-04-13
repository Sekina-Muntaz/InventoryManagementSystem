
from app import db
class inventoryModel(db.Model):
    __tablename__='new_inventories'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100), nullable=False,unique=True)
    inv_type=db.Column(db.String(10),nullable=False)
    buying_price=db.Column(db.Float)
    selling_price=db.Column(db.Float)
    sales=db.relationship('SalesModel',backref='inventories', lazy=True)
    stocks=db.relationship('StocksModel',backref='inventories', lazy=True)

    '''
     We also need to declare a relationship between the models.
         - To do that, we introduce a db.relationship() - A function that signifies the relationship between two models
        - we also describe the relationship using
            1. the Model the parent is related to
            2. how the child will call the parent
            3. how to load the data
        - it is always advisable to place the relationship() inside the parent model for easy reference

    '''
    