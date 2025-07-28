from core import writer
import re
import csv
from tabulate import tabulate



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

def mostrar_contactos():
    file_paht  = 'csv/data.csv'
    with open(file_paht, mode="r", newline="") as f:
        leyendo = csv.DictReader(f)
        filas = [lee for lee in leyendo]
        print(tabulate(filas, headers='keys', tablefmt='grid'))

def editar_contacto():
    file_paht  = 'csv/data.csv'
    print("Cual contacto quiere Editar?")
    with open(file_paht, mode='r', newline="") as f :
        leyendo_datos = csv.DictReader(f)
        lista_editable = [lee for lee in leyendo_datos]
        print(f" contactos editables: {tabulate(lista_editable, headers='keys', tablefmt='grid')}")
    
    editando_contacto = input("Seleccione el ID a editar: ")
    contacto_filtrado = [contacto for contacto in lista_editable if contacto['id'] == editando_contacto]
    if not contacto_filtrado:
        print("No se encuntra ningun usuario con este ID")
    else:
        print(f"Editando contacto : {tabulate(contacto_filtrado, headers='keys', tablefmt='grid')}")
        for dato in contacto_filtrado:
            editar_dato = input(f"Cual dato quiere camabiar? ({','.join(dato.keys())}): ").lower()
            if not editar_dato:
                print("Debe especificar el dato a cambiar")
            else: 
                if editar_dato in dato:
                    nuevo_dato = input(f"Ingrese el nuevo valor para {editar_dato}: ")
                    dato[editar_dato] = nuevo_dato

                    with open(file_paht, mode='w', newline='') as f:
                        campos = ['id', 'nombre', 'email', 'telefono']
                        escritor = csv.DictWriter(f, fieldnames=campos)
                        escritor.writeheader()
                        escritor.writerows(lista_editable)
                        print(f" Actualizado correctamente {tabulate(lista_editable, headers='keys', tablefmt='grid')}")

def eliminar_contacto(id):
    file_paht  = 'csv/data.csv'
    with open(file_paht, mode="r", newline="") as f:
        leyendo  = csv.DictReader(f)
        print(f"\nEste es tu id: {id}")
        contacto_encontrado = [lee for lee in leyendo if lee['id'] != id]
    
    with open(file_paht, mode='w', newline="") as f:
        
        campos = ['id', 'nombre', 'email', 'telefono']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(contacto_encontrado)
        print("Esto son los contactos restantes")
        print(f"{tabulate(contacto_encontrado, headers='keys', tablefmt='grid')}")

def buscar_contacto(id):
    file_paht  = 'csv/data.csv'
    with open(file_paht, mode="r", newline="") as f:
        leyendo  = csv.DictReader(f)
        print(f"\nEste es tu id: {id}")
        contacto_encontrado = [lee for lee in leyendo if lee['id'] == id]
        if contacto_encontrado == []:
            print("este id no exsiste")
        else:
            print(tabulate(contacto_encontrado, headers='keys', tablefmt='grid'))





