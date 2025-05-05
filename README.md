# insertInEduslep

# Envío de datos de impresoras a API

Este proyecto lee un archivo de Excel con información de impresoras y envía cada fila como una solicitud `POST` a una API.

## 📁 Estructura esperada
├── main.py
├── .env
├── impresoras_test.xlsx
├── requirements.txt
└── .gitignore

## ⚙️ Requisitos

- Python 3.x
- `pip`


## 📦 Instalación de dependencias
pip install -r requirements.txt

## 🚀 Uso

python main.py

##  Ejemplo de salida

Fila 0 insertada correctamente.
Fila 1 insertada correctamente.
Error al insertar fila 2: 400 - {"detalle": "Campo 'modelo' es obligatorio"}