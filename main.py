
import pandas as pd
import requests



archivo_excel = 'impresoras_test.xlsx'  # Ruta a tu archivo Excel

url_api = 'https://eduslepbm.andestic.io/backend/api_modelos/dynamic/2/impresoras/'  # URL del endpoint de la API
headers = {
    #'Content-Type': 'application/json',
    'api_key': '4KffXnS9iJ-ZnQxrMPzAP-T'  # Si tu API necesita autenticación
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