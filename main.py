from core import contactos

while True:
    print("\nAgendify")
    print("1. Agregar un nuevo contacto")
    print("2. Buscar contacto exisitente")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contactos")
    print("5. Editar contactos")
    print("6. salir")

    opcion = input("Escoja una opción: ")

    if opcion == '1':
        print("Agregando un nuevo contaccto:")
        contactos.guardar_contacto()
    elif opcion == '2':
        print("Buscando Contacto exsitente")
        pedir_id = input("coloque el id que quiere buscar: ")
        contactos.buscar_contacto(pedir_id)
    elif opcion == '3':
        print("Mostrnado todos los contactos:")
        contactos.mostrar_contactos()
    elif opcion == '4':
        print("Aqui eliminaremos un contacto")
        pedir_id = input("coloque el id que quiere buscar: ")
        contactos.eliminar_contacto(pedir_id)
        pass
    elif opcion == '5':
        while True:
            contactos.editar_contacto()
            if input("Desea seguir editando algun contacto? s/n").lower() != "s":
                break

    elif opcion == '6':
        print("saliendo de la app")
        break 