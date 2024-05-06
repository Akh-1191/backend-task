from models import database, Product


def initialize_database():
    database.connect()
    database.create_tables([Product], safe=True)
