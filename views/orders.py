from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for

from models import db
from models.order import Order, OrderItem
from models.product import Product

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')


@orders_bp.route('/')
def index():
    orders = Order.query.all()
    return render_template('orders/list.html', orders=orders)


@orders_bp.route('/create', methods=['GET', 'POST'])
def create():
    products = Product.query.all()
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        order = Order(customer_name=customer_name, date=date.today())
        product_ids = request.form.getlist('product_id')
        quantities = request.form.getlist('quantity')
        for pid, qty in zip(product_ids, quantities):
            if pid:
                item = OrderItem(product_id=int(pid), quantity=int(qty))
                order.items.append(item)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('orders.index'))
    return render_template('orders/create.html', products=products)


@orders_bp.route('/<int:order_id>/edit', methods=['GET', 'POST'])
def edit(order_id):
    order = Order.query.get_or_404(order_id)
    products = Product.query.all()
    if request.method == 'POST':
        order.customer_name = request.form['customer_name']
        order.items.clear()
        product_ids = request.form.getlist('product_id')
        quantities = request.form.getlist('quantity')
        for pid, qty in zip(product_ids, quantities):
            if pid:
                item = OrderItem(product_id=int(pid), quantity=int(qty))
                order.items.append(item)
        db.session.commit()
        return redirect(url_for('orders.index'))
    return render_template('orders/edit.html', order=order, products=products)


@orders_bp.route('/<int:order_id>/delete', methods=['POST'])
def delete(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('orders.index'))
