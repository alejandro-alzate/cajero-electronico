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

        if opcion == 2:
            cantidad = int(input("Ingresa la cantidad a retirar "))
            if cantidad > saldo:
                print("No tienes suficiente saldo")
            elif cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
            else:
                saldo -= cantidad
                print(f"su nuevo saldo es {saldo}")
        if opcion == 3:
            consignar()
        if opcion == 4:
            cambiar_clave()
            
        
        if opcion == 5:
            print("Cerrando Sesion...")
            break

def cambiar_clave():

  # Solicitar la clave actual
  clave_actual = input("Ingrese su clave actual: ")

  # Validar la clave actual
  if clave_actual != "1234":
    print("Clave incorrecta. Intente nuevamente.")
    return

  # Solicitar la nueva clave
  nueva_clave = input("Ingrese su nueva clave: ")

  # Solicitar confirmación de la nueva clave
  nueva_clave_confirmada = input("Confirme su nueva clave: ")

  # Validar la confirmación de la clave
  if nueva_clave != nueva_clave_confirmada:
    print("Las claves no coinciden. Intente nuevamente.")
    return

  # Simular la actualización de la clave
  print("Clave actualizada exitosamente.")

def consignar():
    saldo=3000000
    cantidad= int(input("Cuanto quiere consignar? $"))
    cuenta= int(input("Cuenta a consignar "))
    tipo=int(input("Tipo de cuenta: \n1. Ahorros\n2. Corriente\n"))
    if tipo==1:
        tipo= "Ahorros"
    elif tipo==2:
        tipo= "Corriente"


    if cantidad > saldo:
        print("No tienes suficiente saldo")
    elif cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
    else:
        saldo -= cantidad
        print(f"Consignacion realizada...!\nCuenta: {cuenta}\nTipo: {tipo}\nSu nuevo saldo es ${saldo}\n")
        return

menu()

