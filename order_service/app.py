from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/order_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
