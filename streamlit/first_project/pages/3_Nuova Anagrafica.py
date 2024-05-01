import streamlit as st
import pandas as pd
import sqlalchemy
from utilities.utilities_lib import utility_functions as uf


DATA_URL ='https://github.com/federicobiamonte/MyApps/blob/main/streamlit/first_project/data'

df_nazioni = uf.get_data_from_url(DATA_URL, 'stati', 'csv', ',')
elenco_nazioni = df_nazioni['nazione'].unique().tolist()

df_regioni = uf.get_data_from_url(DATA_URL, 'regioni', 'csv', ';')
elenco_regioni = df_regioni['denominazione_regione'].unique().tolist()

df_province = uf.get_data_from_url(DATA_URL, 'province', 'csv', ';')
df_comuni = uf.get_data_from_url(DATA_URL, 'comuni', 'csv', ';')

st.title('Modulo Inserimento Anagrafiche', anchor='left')

df_anagrafica_persone = pd.DataFrame()
df_anagrafica_aziende = pd.DataFrame()

with st.form(key='form_inserimento_anagrafica'):
    tipologia = st.selectbox('Tipologia Anagrafica', options=['Persona', 'Società', 'Altro'], index=None, placeholder='Seleziona il tipo di anagrafica da inserire', key='dropdown_tipologia_anagrafica')

    if tipologia == 'Persona':
        tipo_persona = st.selectbox('Selezionare Categoria', options=['Cliente', 'Dipendente'], index=None, key='dropdown_categoria_persona', placeholder='Seleziona la categoria di persona da inserire')

        if tipo_persona == 'Cliente':
            col1, col2 = st.columns(2)
            with col1:
                nome = st.text_input('Nome', value='', max_chars=None, key='textinput_nome', placeholder='')
            with col2:
                cognome = st.text_input('Cognome', value='', max_chars=None, key='textinput_cognome')

            stato = st.selectbox('Stato', options=elenco_nazioni, index=None, key='dropdown_stato')
            if stato == 'Italia':
                col3, col4, col5 = st.columns(3)
                with col3:
                    regione = st.selectbox('Regione', options=elenco_regioni, index=None, key='dropdown_regione', placeholder='Seleziona la regione')
                    if regione:
                        codice_regione = df_regioni['codice_regione'][df_regioni['denominazione_regione'] == regione].values[0]
                        with col4:
                            provincia = st.selectbox('Provincia', options=df_province['denominazione_provincia'][df_province['codice_regione'] == codice_regione].unique().tolist(), index=None, key='dropdown_provincia', placeholder='Seleziona la provincia')
                            if provincia:
                                sigla_provincia = df_province['sigla_provincia'][df_province['denominazione_provincia'] == provincia].values[0]
                                if provincia:
                                    with col5:
                                        comune = st.selectbox('Comune', options=df_comuni['denominazione_ita'][df_comuni['sigla_provincia'] == sigla_provincia].unique().tolist(), index=None, key='dropdown_comune', placeholder='Seleziona il comune')

                if regione and provincia and comune:
                    col6, col7 = st.columns(2)
                    with col6:
                        indirizzo = st.text_input('Indirizzo', value='', max_chars=None, key='textinput_indirizzo', placeholder='Es: Via Roma 43')
                    with col7:
                        cap = st.text_input('CAP', value='', max_chars=None, key='textinput_cap', placeholder='Es: 00100')
                        if cap:
                            if not cap.isdigit():
                                st.error('Il CAP deve essere un numero')
                            elif len(cap) != 5:
                                st.error('Il CAP deve essere di 5 cifre')

        # Add a submit button
        submit_button = st.form_submit_button(label='Submit')
    


            



    


