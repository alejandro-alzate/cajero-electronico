def menu_inicio():
    while True:
        opcion = int(input("Menu_inicio...\n1.reqistrar \n2.ingresar \n3. salir"))

        if opcion == 3:
            break

def menu():
    while True:
        opcion = int(input("Menu...\n1. Consultar saldo\n2. Retirar saldo\n3. Consignar\n4. Cambiar clave\n5. Salir\n"))

        if opcion == 5:
            break


menu()