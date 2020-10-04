from flask import Flask
from flask_restful import Api, reqparse
from flask_jwt import JWT
from resources.item import Item, ItemList

from security import authenticate, identity
from resources.user import UserRegister
from db import db
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'edmoney'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all() # create all tables if not exist


jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)