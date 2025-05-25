from dataweb import DataWeb
import pandas as pd
from database import Database


def main():
    dw = DataWeb()
    db=Database()
    df=pd.DataFrame()
    df=dw.obtenerDatos()
    df_db=db.guardar_df(df)
    df_db2=db.obtener_datos()
    #df.to_csv("poblacion.csv")
    df_db2.to_csv("src/edu_pad/static/csv/data_webdb.csv", index=False)


if __name__ == "__main__":
    main()
