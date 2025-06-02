import pandas as pd
from database import Database


def main():

    db=Database()
    df=pd.read_csv("src/edu_pad/static/csv/data_extractor.csv")
    df_db=db.guardar_df(df)
    df_db2=db.obtener_datos() # capa 3
    #df.to_csv("poblacion.csv")
    df_db2.to_csv("src/edu_pad/static/csv/data_db.csv", index=False)


if __name__ == "__main__":
    main()