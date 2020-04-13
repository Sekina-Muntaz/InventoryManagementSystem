class Config():
    DEBUG=True
    SECRET_KEY='secret'

class Development(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:root@localhost:5432/inventory_management_system'

class Production(Config):
    pass