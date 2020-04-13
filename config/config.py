class Config():
    DEBUG=True
SECRET_KEY='secret'

class Development():
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:root@localhost:5432/inventory_management_system'

class Production():
    pass