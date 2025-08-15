from flask import Blueprint, render_template

from models.category import Category

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/create')
def create():
    categories = Category.query.all()
    return render_template('products/form.html', categories=categories)
