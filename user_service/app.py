from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/user_db'
app.config['JWT_SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
