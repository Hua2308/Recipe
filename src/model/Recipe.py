import datetime
from . import db


class Recipe(db.Model):

    # table name
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    ingredients = db.Column(db.String(4096), nullable=False)
    instructions = db.Column(db.String(4096), nullable=False)
    serving_size = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(128), nullable=False)
    notes = db.Column(db.String(4096), nullable=False)
    date_added = db.Column(db.DateTime, nullable=True)
    date_modified = db.Column(db.DateTime, nullable=True)


    def __init__(self, data):

        self.name = data.get('name')
        self.ingredients = data.get('ingredients')
        self.instructions = data.get('instructions')
        self.serving_size = data.get('serving_size')
        self.category = data.get('category')
        self.notes = data.get('notes')
        self.date_added = datetime.datetime.utcnow()
        self.date_modified = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.date_modified = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_one_recipe_by_id(id):
        return Recipe.query.get(id)

    @staticmethod
    def get_one_recipe_by_name(name):
        return Recipe.query.get(name)