from flask import Flask
from models import db
from views.orders import orders_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(orders_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
