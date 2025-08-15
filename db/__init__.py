from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models to register them with SQLAlchemy metadata
from models.category import Category  # noqa: F401
