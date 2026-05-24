class config:
    DEBUG = True
    TESTING = True

    #configuracion de base de datos
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/blog_db"

class productionconfig(config):
    debug = False

class developmentconfig(config):
    SECRET_KEY = "dev"
    DEBUG = True
    TESTING = True

    