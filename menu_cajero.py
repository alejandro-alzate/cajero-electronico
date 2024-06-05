import util
import os


def menu_inicio():
    while True:
        opcion = int(input("Menu_inicio...\n1.reqistrar \n2.ingresar \n3. salir"))

        if opcion == 3:
            break


def menu():
    saldo=3000000    
    while True:
        opcion = int(input("Menu...\n1. Consultar saldo\n2. Retirar saldo\n3. Consignar\n4. Cambiar clave\n5. Salir\n"))
        #os.system('cls')
        util.limpiarPantalla()
        
        if opcion == 1:
            print(f"Su saldo actual es: ${saldo}")
        elif opcion == 2:
            cantidad = float(input("Ingresa la cantidad a retirar"))
            if cantidad > saldo:
                print("No tienes suficiente saldo")
            elif cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
            else:
                saldo -= cantidad
                print(f"su nuevo saldo es {saldo}")
        elif opcion == 3:
            cantidad = float(input("Ingresa la cantidad a consignar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
            else:
                saldo += cantidad
                print(f"Su nuevo saldo es: ${saldo}")
        else:
            print("Opción no válida")

            
        
        if opcion == 5:
            print("Cerrando Sesion...")
            break




#que pa mi codigo que?
menu()