import streamlit as st
import pandas as pd


st.title("Listar Todas as Incursões")


# upload do arquivo
df = pd.read_excel('lista_das_incursoes.xlsx')

st.write('Conteúdo da Planilha')
st.dataframe(df)


