from flask import Blueprint, render_template, request, redirect, url_for, flash

from db import db
from models.category import Category

bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('/')
def index():
    categories = Category.query.all()
    return render_template('categories/index.html', categories=categories)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description')
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        flash('Category created')
        return redirect(url_for('categories.index'))
    return render_template('categories/form.html')

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        category.description = request.form.get('description')
        db.session.commit()
        flash('Category updated')
        return redirect(url_for('categories.index'))
    return render_template('categories/form.html', category=category)

@bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted')
    return redirect(url_for('categories.index'))
