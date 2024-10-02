import streamlit as st

from serviços import ServiçoAcesso
from base_de_dados import session

st.title("Dashboard Projeto Integrado")

st.header('Acessos:')
st.table(ServiçoAcesso.listar_formatado(session))