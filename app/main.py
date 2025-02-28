import streamlit as st   
from data import *
from pages.formularios import *


def main():

    with st.sidebar:
      st.page_link("main.py",label="🏠 Inicio")
      st.page_link("pages/formularios.py",label="📋 Carga de SAEs")

    #crear_csv()
    formulario_carga()
   
if __name__ == '__main__':
    main()
    