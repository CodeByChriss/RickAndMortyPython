# 🚀 ¿Cómo puedo ejecutarlo?

1. Creamos el entorno virtual (doy por hecho que ya está instalado python)

```bash
python -m venv venv
```

2. Accedemos al entorno virtual

```bash
.\venv\Scripts\activate
```

3. Instalamos las dependencias

```bash
pip install requests
```

4. Ejecutamos el fichero main.py
```bash
python main.py
```

Si queremos salir del entorno virtual:

```bash
deactivate
```

# ✏️ Enunciado
1. OBJETIVO DEL PROYECTO

El objetivo de este proyecto es desarrollar una aplicación en Python que integre los principales contenidos trabajados durante el curso, haciendo especial hincapié en la Programación Orientada a Objetos (RA6) y el manejo de ficheros JSON (RA5).

El proyecto consistirá en la creación de un programa que:

Obtenga datos en formato JSON desde una API REST pública.
Procese y gestione esos datos utilizando clases y objetos.
Almacene y recupere información mediante ficheros JSON.
Trabaje con estructuras de datos y funciones de forma organizada.
 
2. TEMÁTICA DEL PROYECTO

La temática es libre, pero debe basarse en el consumo de una API REST que devuelva datos en formato JSON.

La API elegida debe ser pública y no requerir autenticación compleja.

 
3. REQUISITOS OBLIGATORIOS

Uso de Programación Orientada a Objetos (RA6). El programa debe:

Definir al menos una clase principal relacionada con la temática elegida.
Crear y gestionar varios objetos de dicha clase.
 
Uso de API REST y JSON (RA5). El programa debe:

Conectarse a una API REST.
Obtener datos en formato JSON.
Convertir los datos recibidos en estructuras de Python.
Crear objetos a partir de los datos de la API.
Guardar los datos procesados en uno o varios ficheros JSON locales.
Leer dichos ficheros JSON cuando sea necesario.
Manejo de estructuras de datos (RA4).

Organización del programa en funciones con un main que controle el flujo (RA3). 

Interacción básica con el usuario.