from flask import request, jsonify
from app import app, db
from models import Product

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price, "stock": p.stock} for p in products]), 200

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully!"}), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get(id)
    if product:
        if product.version == data['version']:
            product.name = data['name']
            product.price = data['price']
            product.stock = data['stock']
            product.version += 1
            db.session.commit()
            return jsonify({"message": "Product updated successfully!"}), 200
        else:
            return jsonify({"message": "Version conflict"}), 409
    return jsonify({"message": "Product not found"}), 404
