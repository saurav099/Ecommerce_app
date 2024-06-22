from flask import request, jsonify
from app import app, db
from models import Order

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'], total_price=data['total_price'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order created successfully!"}), 201

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    if order:
        return jsonify({"id": order.id, "user_id": order.user_id, "product_id": order.product_id, "quantity": order.quantity, "total_price": order.total_price}), 200
    return jsonify({"message": "Order not found"}), 404
