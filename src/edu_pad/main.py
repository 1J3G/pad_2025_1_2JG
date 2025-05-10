from dataweb import DataWeb
import pandas as pd


def main():
    dw = DataWeb()
    df=pd.DataFrame()
    df=dw.obtenerDatos()
    df.to_csv("poblacion.csv")


if __name__ == "__main__":
    main()
