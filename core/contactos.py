from core import writer
import re
import csv



def guardar_contacto():
    """
    Solicita al usuario que ingrese su nombre, número de teléfono y correo electrónico,
    valida los datos ingresados y, si son válidos, registra el contacto.
    El número de teléfono debe tener el formato 'xxx-xxx-xxxx'.
    El correo electrónico debe tener un formato válido.
    No se permiten campos vacíos.
    Returns:
        El resultado de la función writer.output(resgistar_contacto) si los datos son válidos.
        Si hay errores de validación, muestra mensajes por consola y no retorna nada.
    """
    nombre  = input(" Coloque su nombre para proceder con el registro: ").lower().strip()
    
    telefono = input(" Ahora Proceda con su numero de telefono Nota(los numeros van separados por guiones): ")
    
    email  = input(" Por ultimo proceda con su email: ").lower().strip()

    match_telefono = re.search(r"(\d{3})-(\d{3})-(\d{4})", telefono)

    match_email = re.search(r"([\w\.-]+)@([\w\.-]+)\.(\w+)", email)

    if not nombre or not email or not telefono:
        print("No pueden exisitir campos vacios")
    elif match_telefono.group() != telefono:
        print("Recuerde que el patron valido es xxx-xxx-xxxx")
    elif match_email.group() != email:
        print("No es un correo valido")
    else:
        resgistar_contacto = {
                            
                            "nombre": nombre,
                            "email": email,
                            "telefono": telefono 
                          }
    return writer.output(resgistar_contacto)

def buscar_contacto(id):
    file_paht  = 'csv/data.csv'
    with open(file_paht, mode="r", newline="") as f:
        leyendo  = csv.DictReader(f)
        print(f"\nEste es tu id: {id}")
        contacto_encontrado = [lee for lee in leyendo if lee['id'] == id]
        if contacto_encontrado == []:
            print("este id no exsiste")
        else:
            print(contacto_encontrado)