import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime



class DataWeb:
    def __init__(self):
        self.url = "https://www.worldometers.info/world-population/population-by-country/"
    

    def obtenerDatos(self):
        try:
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            respuesta=requests.get(self.url, headers=headers)
            if respuesta.status_code != 200:
                print("Error en la url, la pagina no existe o no se puede acceder")

            soup=BeautifulSoup(respuesta.text,"html.parser")

            tabla=soup.find("table",{"class":"datatable"})

            encabezado=[]
            for x in tabla.find_all("tr"):
                for y in x.find_all("th"):
                    encabezado.append(y.text.strip())

            tabla_valores=[]
            for x in tabla.find_all("tr")[1:]:
                td_columna=x.find_all("td")
                td_valores=[y.text for y in td_columna]
                tabla_valores.append(td_valores)
               

            df=pd.DataFrame(tabla_valores,columns=encabezado)
            #df.to_excel("poblacion.xlsx",index=False)
            return df




        except Exception as err:
            print(f"Error al obtener los datos: {err}")
            df=pd.DataFrame
