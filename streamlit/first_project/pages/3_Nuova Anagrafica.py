import streamlit as st
import pandas as pd
import sqlalchemy
import requests
import io
from utilities.utilities_lib import utility_functions as uf

#leggi i dati dal seguente path: 'https://github.com/federicobiamonte/MyApps/blob/main/streamlit/first_project/data/stati.csv?raw=true'

DATA_URL ='https://github.com/federicobiamonte/MyApps/blob/main/streamlit/first_project/data/stati.csv?raw=true'

df_nazioni = uf.get_data_from_url(DATA_URL, 'stati', 'csv')
elenco_nazioni = df_nazioni['nome'].unique().tolist()

df_regioni = uf.get_data_from_url(DATA_URL, 'regioni', 'csv')
elenco_regioni = df_regioni['denominazione_regione'].unique().tolist()

st.write(df_regioni)

st.title('Modulo Inserimento Anagrafiche', anchor='left')

df_anagrafica_persone = pd.DataFrame()
df_anagrafica_aziende = pd.DataFrame()

tipologia = st.selectbox('Tipologia Anagrafica', options = ['Persona', 'Società', 'Altro'], index=None, placeholder='Seleziona il tipo di anagrafica da inserire', key='dropdown_tipologia_anagrafica')

if tipologia == 'Persona':
    tipo_persona = st.selectbox('Selezionare Categoria', options = ['Cliente', 'Dipendente'], index=None, key='dropdown_categoria_persona', placeholder='Seleziona la categoria di persona da inserire')

    if tipo_persona == 'Cliente':
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input('Nome', value='', max_chars=None, key='textinput_nome', placeholder='')
        with col2:
            cognome = st.text_input('Cognome', value='', max_chars=None, key='textinput_cognome')
        


        stato = st.selectbox('Stato', options = elenco_nazioni, index=None, key='dropdown_stato')
        if stato == 'Italia':
            col3, col4, col5 = st.columns(3)
            with col3:
                regione = st.selectbox('Regione', options = elenco_regioni)

    






        st.text_input('Indirizzo', value='', max_chars=None, key='textinput_indirizzo', placeholder='Es: Via Roma, 1 Roma')


