import streamlit as st
import pandas as pd
import sqlalchemy

DATA_PATH = '.data/'
df_nazioni = pd.read_csv(DATA_PATH + 'elenco_nazioni.csv')
elenco_nazioni = df_nazioni['nazione'].tolist() 

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
        
        st.selectbox('Stato', options = elenco_nazioni, index=None, key='dropdown_stato')

        st.text_input('Indirizzo', value='', max_chars=None, key='textinput_indirizzo', placeholder='Es: Via Roma, 1 Roma')