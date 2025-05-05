
import os
import pandas as pd
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


# Obtener variables de entorno
archivo_excel = os.getenv('ARCHIVO_EXCEL')
url_api = os.getenv('URL_API')
api_key = os.getenv('API_KEY')
headers = {
    #'Content-Type': 'application/json',
    'api_key': api_key  # Si tu API necesita autenticación
}


# Leer archivo Excel
df = pd.read_excel(archivo_excel)


#print(df)

# Recorrer filas y enviar POST
for index, fila in df.iterrows():
    data = {
        'rbd': fila['rbd'],
        'nombreestablecimiento': fila['nombreestablecimiento'],
        'email': fila['email'],
        'marca': fila['marca'],
        'modelo': fila['modelo'],
        'serie': fila['serie']
        # Agrega más campos según tus necesidades
    }

    respuesta = requests.post(url_api, json=data, headers=headers)

    if respuesta.status_code == 200:
        print(f"Fila {index} insertada correctamente.")
    else:
        print(f"Error al insertar fila {index}: {respuesta.status_code} - {respuesta.text}")