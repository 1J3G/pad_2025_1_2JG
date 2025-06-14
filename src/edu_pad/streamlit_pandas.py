import streamlit as st
from ydata_profiling import ProfileReport
import pandas as pd
import os



def main():


    

    df = pd.read_csv("src/edu_pad/static/csv/data_extractor.csv")
    columnas = ["Country (ordependency)","Population(2025)","Density(P/Km²)","Fert.Rate","MedianAge","UrbanPop %","WorldShare"]
    df_2 = df[columnas]
    profile = ProfileReport(df_2, title="Dashboard Población Mundial")
    st.title("Análisis de Datos")
    #st.write(profile.to_html(),unsafe_allow_html=True)
    st.components.v1.html(profile.to_html(), height=600, scrolling=True)


if __name__ == "__main__":
    main()
