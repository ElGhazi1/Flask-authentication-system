from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # Add the secret key
    app.config['SECRET_KEY'] = 'fjdkslkdjf qsmeizeoiuez qaputqsmapht sapzeirusksjf'


    # Configuration de la base de données MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'flaskapp1_db'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_UNIX_SOCKET'] = None
    app.config['MYSQL_CONNECT_TIMEOUT'] = 10
    app.config['MYSQL_READ_DEFAULT_FILE'] = None
    app.config['MYSQL_READ_DEFAULT_GROUP'] = None
    app.config['MYSQL_CLIENT_FLAGS'] = None
    app.config['MYSQL_CHARSET'] = None
    app.config['MYSQL_USE_UNICODE'] = True
    app.config['MYSQL_SQL_MODE'] = None
    app.config['MYSQL_CURSORCLASS'] = None
    app.config['MYSQL_SSL_KEY'] = None
    app.config['MYSQL_SSL_CERT'] = None
    app.config['MYSQL_SSL_CA'] = None
    app.config['MYSQL_SSL_CAPATH'] = None
    app.config['MYSQL_SSL_CIPHER'] = None

    mysql.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
