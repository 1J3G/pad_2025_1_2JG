import streamlit as st
from ydata_profiling import ProfileReport
import pandas as pd
import os



def main():
    st.title("🌍 Visualización de Datos Demográficos - 2025")

    # Cargar el archivo CSV
    try:
        df = pd.read_csv("static/csv/data_extractor.csv")
    except FileNotFoundError:
        st.error("❌ No se encontró el archivo en 'static/csv/data_extractor.csv'.")
        return

    # Columnas deseadas
    columnas_deseadas = [
        'Country (or dependency)',
        'Population (2025)',
        'Yearly Change',
        'Net Change',
        'Density (P/Km²)',
        'Land Area (Km²)',
        'Migrants (net)',
        'Fert. Rate',
        'Median Age',
        'Urban Pop %',
        'World Share'
    ]

    # Verificar qué columnas están presentes
    columnas_disponibles = [col for col in columnas_deseadas if col in df.columns]
    columnas_faltantes = set(columnas_deseadas) - set(df.columns)

    if columnas_faltantes:
        st.warning(f"⚠️ Las siguientes columnas no se encontraron en el CSV: {columnas_faltantes}")

    # Mostrar el DataFrame filtrado
    df_filtrado = df[columnas_disponibles]
    st.subheader("📊 Datos Demográficos Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

if __name__ == "__main__":
    main()