
while True: 
    opcion=int(input("Ingrese la opcion que quiere realizar: "))
    if opcion == 1:
        print("Su saldo actual es: $3.000.000")
    continuar=print("Desea elegir otra opcion SI NO: ")
    if continuar == "no":
        continuar.lower()
        break
