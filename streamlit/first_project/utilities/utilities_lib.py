import sqlalchemy
import pandas as pd
import requests
import io

class utility_functions:
    def get_db_connection() -> sqlalchemy.engine.base.Connection:
        connection = sqlalchemy