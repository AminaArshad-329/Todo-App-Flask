from flask import Flask,request ,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    'Amina': generate_password_hash('admin'),
    'Zoya': generate_password_hash('ZoyaAhmad'),
    'Sidra': generate_password_hash('sidra'),
}


basedir = os.path.abspath(os.path.dirname(__file__))

# Database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')
    
    
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/create_product', methods=['POST'])
@auth.login_required
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']
    
    product = Product(name, description, price, quantity)
    db.session.add(product)
    db.session.commit()
    
    return product_schema.jsonify(product)

@app.route('/all_products', methods=['GET'])
@auth.login_required
def get_products():
    all_pro = Product.query.all()
    res = products_schema.dump(all_pro)
    return jsonify(res) 



@app.route('/single_product/<id>', methods=['GET'])
@auth.login_required
def get_single_product(id):
    pro = Product.query.get(id)
    return product_schema.jsonify(pro)


@app.route('/update_product/<id>', methods=['PUT'])
@auth.login_required
def update_product(id):
    product = Product.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']
    
    product.name = name

    product.description = description

    product.price = price

    product.quantity = quantity

    db.session.commit()
    
    return product_schema.jsonify(product)


@app.route('/delete_product/<id>', methods=['DELETE'])
@auth.login_required
def delete_product(id):
    pro = Product.query.get(id)
    db.session.delete(pro)
    db.session.commit()
    return product_schema.jsonify(pro)


if __name__ == '__main__':
    app.run(debug=True)