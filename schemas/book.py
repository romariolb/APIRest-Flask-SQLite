from flask_sqlalchemy import model
from marshmallow_sqlalchemy import load_instance_mixin
from ma import ma
from models.book import BookModel

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True