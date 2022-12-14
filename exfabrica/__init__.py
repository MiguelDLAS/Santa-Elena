from flask import flask 
from flask_sqlalchemy import SQLALCHEMY_DATABASE_URI

app = flask (__name__)

#cargar las configuraciones 
app.config.from_object('config.developmentConfig')
db = SQLAlchemy(app)

#importar vistas 
from exfabrica.views.auth import auth
app.register_blueprint(auth)

from exfabrica.views.pagina_web import pagina_web
app.register_blueprint(blog)

db.create_all()