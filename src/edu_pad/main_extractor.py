from src.edu_pad.dataweb import DataWeb
import pandas as pd



def main():
    dw = DataWeb()
    df=pd.DataFrame()
    df=dw.obtenerDatos() # capa 2
    df.to_csv("src/edu_pad/static/csv/data_extractor.csv", index=False,mode="a")


if __name__ == "__main__":
    main()