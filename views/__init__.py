"""Application views."""

from flask import Flask

from .products import bp as products_bp


def register(app: Flask) -> None:
    """Register blueprints with the Flask app."""
    app.register_blueprint(products_bp)
