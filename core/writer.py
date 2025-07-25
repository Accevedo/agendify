import csv
import os

def output(registroContacto, file='csv/data.csv'):
    """
    Agrega un registro de contacto a un archivo CSV, asignando automáticamente un ID incremental.
    Si el archivo no existe, se crea junto con los directorios necesarios. Si el archivo existe,
    se calcula el próximo ID basado en los registros existentes. El registro de contacto se
    escribe en el archivo, incluyendo el nuevo ID.
    Args:
        registroContacto (dict): Diccionario con los datos del contacto. Debe contener las claves
            'nombre', 'email' y 'telefono'. El campo 'id' se agrega automáticamente.
        file (str, optional): Ruta al archivo CSV donde se almacenan los contactos.
            Por defecto es 'csv/data.csv'.
    Side Effects:
        - Crea el directorio y el archivo CSV si no existen.
        - Modifica el diccionario 'registroContacto' agregando la clave 'id'.
        - Escribe el registro en el archivo CSV.
    """
    os.makedirs(os.path.dirname(file), exist_ok=True)

    # Paso 1: Calcular el próximo ID
    if os.path.exists(file) and os.path.getsize(file) > 0:
        with open(file, mode='r', newline='') as f:
            lector = csv.DictReader(f)
            for c in lector:
                print(c)
            ids = [int(fila["id"]) for fila in lector]
            nuevo_id = max(ids) + 1 if ids else 1
    else:
        nuevo_id = 1

    # Paso 2: Agregar el ID al dict original
    registroContacto["id"] = nuevo_id

    # Paso 3: Escribir en el archivo
    with open(file, mode='a', newline='') as f:
        campos = ['id', 'nombre', 'email', 'telefono']
        escritor = csv.DictWriter(f, fieldnames=campos)
        

        if f.tell() == 0:  # si el archivo está vacío, escribe encabezados
            escritor.writeheader()

        escritor.writerow(registroContacto)
