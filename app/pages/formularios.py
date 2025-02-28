import streamlit as st
import pandas as pd  
from data import agregar_data, cargar_datos



st.markdown("<h3 style='text-align:center;'>Ingresos de SAEs según DDJJ de cargas</h3>", unsafe_allow_html=True)
def formulario_carga():
    # Formulario para agregar datos
    with st.form(key='my_form', clear_on_submit=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fecha = st.date_input("Fecha")
            sae = st.text_input("SAE")
        with col2:
            producto = st.text_input("Producto")
            destino = st.text_input("Destino")
        with col3:
            cantidad = st.number_input("Cantidad", min_value=0)
            camion = st.text_input("Camión")
        with col4:
            precintos = st.text_input("Precintos")
            semi = st.text_input("Semi")
            contenedor = st.text_input("Contenedor")
        
        submit_button = st.form_submit_button(label='Guardar')
        
        # Aquí manejamos la lógica después de que se presione el botón
        if submit_button:
            # Llamar a agregar_data con los datos del formulario
            agregar_data(fecha, sae, producto, destino, cantidad, camion, semi, precintos, contenedor)
            st.success("Datos guardados correctamente.")
        
        # Cargar el DataFrame después de que se haya enviado el formulario
        df_actual = cargar_datos()
        
        # Eliminar la columna 'id' antes de mostrar el DataFrame
        df_actual = df_actual.drop(columns=['id'], errors='ignore')
        
        # Capitalizar la primera letra de las columnas 'Producto' y 'Destino'
        df_actual['Producto'] = df_actual['Producto'].str.capitalize()
        df_actual['Destino'] = df_actual['Destino'].str.capitalize()
        
        # Asegurarse de que la columna 'Fecha' sea de tipo datetime
        df_actual['Fecha'] = pd.to_datetime(df_actual['Fecha'], errors='coerce', dayfirst=True)
        
        # Eliminar filas donde 'Fecha' no se pudo convertir
        df_actual = df_actual.dropna(subset=['Fecha'])
        
        # Extraer solo la parte de la fecha (sin hora)
        df_actual['Fecha'] = df_actual['Fecha'].dt.date
        
        # Ordenar el DataFrame por 'Fecha' en orden descendente
        df_actual = df_actual.sort_values(by='Fecha', ascending=False)
        
        # Mostrar el DataFrame actualizado
        # st.dataframe(df_actual)