import streamlit as st   
import pandas as pd  
import uuid  
import os

file_csv = 'cargas.csv'

def crear_csv():
    if not os.path.isfile(file_csv):
        df = pd.DataFrame(columns=['id', 'Fecha', 'SAE', 'Producto', 'Destino', 'Cantidad', 'Camion', 'Semi', 'Precintos', 'Contenedor'])
        df.to_csv(file_csv, index=False)
def agregar_data(fecha, sae, producto, destino, cantidad, camion, semi, precintos, contenedor):
    nuevo_id = str(uuid.uuid4())
    df_fecha = pd.to_datetime(fecha).date()
    nuevo_dato = pd.DataFrame([[nuevo_id, df_fecha, sae, producto, destino, cantidad, camion, semi, precintos, contenedor]],
                              columns=['id', 'Fecha', 'SAE', 'Producto', 'Destino', 'Cantidad', 'Camion', 'Semi', 'Precintos', 'Contenedor'])
    df_existente = pd.read_csv(file_csv)
    df_actualizado = pd.concat([df_existente, nuevo_dato], ignore_index=True)
    df_actualizado.to_csv(file_csv, index=False)
def cargar_datos(nuevos_datos=None):
    if os.path.isfile(file_csv):
        df_existente = pd.read_csv(file_csv)
    else:
        return pd.DataFrame(columns=['id', 'Fecha', 'SAE', 'Producto', 'Destino', 'Cantidad', 'Camion', 'Semi', 'Precintos', 'Contenedor'])
    # Si se proporcionan nuevos datos, añadirlos al DataFrame existente
    if nuevos_datos is not None:
        df_existente = pd.concat([df_existente, nuevos_datos], ignore_index=True)
    return df_existente