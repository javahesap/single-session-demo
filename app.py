from flask import Flask

from db import db
from views.categories import bp as categories_bp
from views.products import bp as products_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'dev'
    db.init_app(app)

    app.register_blueprint(categories_bp)
    app.register_blueprint(products_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
