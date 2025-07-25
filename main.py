from core import contactos

while True:
    print("\nAgendify")
    print("1. Agregar un nuevo contacto")
    print("2. Buscar contacto exisitente")

    opcion = input("Escoja una opción: ")

    if opcion == '1':
        contactos.guardar_contacto()
    elif opcion == '2':
        pedir_id = input("coloque el id que quiere buscar: ")
        contactos.buscar_contacto(pedir_id)
    elif opcion == '3':
        break