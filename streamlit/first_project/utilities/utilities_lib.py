import sqlalchemy
import pandas as pd
import requests
import io

class utility_functions:
    def get_db_connection() -> sqlalchemy.engine.base.Connection:
        connection = sqlalchemy.create_engine('sqlite:///db.sqlite')
        return connection

    def get_data_from_url(ROOT: str, filename:str, format: str) -> pd.DataFrame:
        URL = f'{ROOT}/{filename}.{format}?raw=true'
        response = requests.get(URL)
        if response.status_code == 200:
            dati = requests.get(URL).content
            dati_raw = pd.read_csv(io.StringIO(dati.decode('utf-8')))
            return dati_raw
        else:
            print('Errore nel caricamento dei dati')   
