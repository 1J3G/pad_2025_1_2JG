import pandas as pd
import sqlite3
import os

class Database:
    def __init__(self):
        self.rutadb="src/edu_pad/static/db/poblacion_analisis.db"

    
    def guardar_df(self,df=pd.DataFrame()):
        df=df.copy()
        try:
            conn=sqlite3.connect(self.rutadb)
            df["Create_Date"]="2025-05-23"
            df["Update_Date"]="2025-05-23"
            df.to_sql("poblacion_analisis",conn,if_exists="replace",index=False)
            print("*******************************************************")
            print("Datos Almacenados en la base de datos")
            print("*******************************************************")
            print("Datos guardados en la base de datos: {})}".format(df.shape))
            return df

        except Exception as errores:
            print("Error al guardar en la base de datos: {}".format(df.shape))
            return None


    def obtener_datos(self,nombre_tabla="poblacion_analisis"):
        try:
            conn=sqlite3.connect(self.rutadb)
            consulta="select * from {}".format(nombre_tabla)
            df=pd.read_sql_query(consulta,conn)
            print("*******************************************************")
            print("Se obtuvieron los datos correctamente")
            print("*******************************************************")
            print("Cantidad de registros en base de datos: {}".format(df.shape))

            return df

        except Exception as errores:
            return None
            print(f"Error al obtener los datos de la tabla: {str(nombre_tabla)} en la base de datos: {str(errores)}")
       
    

