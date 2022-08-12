class config:
    debug = True
    testing = True

    #configuracion de base de datos 
    SQLALCHEMY_TRACK_MODIFICATIONS = false
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/pagina_web"

class pruductionConfig(config):
      DEBUG = False

class Developmenconfig(config):
      SECRET_KEY = 'dev'
      DEBUG = True
