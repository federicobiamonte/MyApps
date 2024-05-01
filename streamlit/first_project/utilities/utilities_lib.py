import sqlalchemy
import pandas as pd

class utility_functions:
    def get_db_connection():
        connection = sqlalchemy.create_engine('sqlite:///db.sqlite')
        return connection