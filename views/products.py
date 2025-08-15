"""Product CRUD views."""

from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy.orm import Session

from db import SessionLocal
from models.product import Product

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/")
def list():
    """List all products."""
    session: Session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return render_template("products/list.html", products=products)


@bp.route("/create", methods=["GET", "POST"])
def create():
    """Create a new product."""
    session: Session = SessionLocal()
    if request.method == "POST":
        product = Product(
            name=request.form["name"],
            price=float(request.form["price"] or 0),
            category_id=int(request.form.get("category_id") or 0),
        )
        session.add(product)
        session.commit()
        session.close()
        return redirect(url_for("products.list"))
    session.close()
    return render_template("products/create.html")


@bp.route("/<int:product_id>/edit", methods=["GET", "POST"])
def edit(product_id: int):
    """Edit an existing product."""
    session: Session = SessionLocal()
    product = session.get(Product, product_id)
    if request.method == "POST":
        product.name = request.form["name"]
        product.price = float(request.form["price"] or 0)
        product.category_id = int(request.form.get("category_id") or 0)
        session.commit()
        session.close()
        return redirect(url_for("products.list"))
    session.expunge(product)
    session.close()
    return render_template("products/edit.html", product=product)


@bp.route("/<int:product_id>/delete", methods=["POST"])
def delete(product_id: int):
    """Delete a product."""
    session: Session = SessionLocal()
    product = session.get(Product, product_id)
    if product:
        session.delete(product)
        session.commit()
    session.close()
    return redirect(url_for("products.list"))
