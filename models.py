import uuid
from peewee import *


database = SqliteDatabase('products.db')


class Product(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)  
    name = CharField()
    description = TextField()
    price = DecimalField(decimal_places=2)
    category = CharField()
    availability = BooleanField()
    stock_quantity = IntegerField()

    class Meta:
        database = database
        constraints = [
            Check('name IS NOT NULL'),
            Check('price IS NOT NULL'),
            Check('availability IS NOT NULL'),
            Check('stock_quantity IS NOT NULL')
        ]
