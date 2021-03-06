import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

app.secret_key = "lkjhdsaofh123ljh"
# Get method to take 2 parameters: Os is for using the Heroku database, sqlite is for testing the app locally:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# Turn off flask sql mofification tracker, because sqlalchemy has its own and its better:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Allows to easily add resources:
api = Api(app)

# JWT creates a new endpoint /auth:
jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
