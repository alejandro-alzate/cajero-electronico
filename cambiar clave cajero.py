def cambiar_clave():
  """Función para cambiar la clave del usuario."""

  


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


#esta es una modificacion

# Función principal para iniciar el programa
def main():
  """Función principal para ejecutar el simulador del cajero automático."""

  print("Bienvenido al simulador de cajero automático.")

  # Presentar las opciones del menú
  print("\nSeleccione una opción:")
  print("1. Cambiar clave")
  print("2. Salir")

  # Obtener la opción seleccionada
  opcion = input("Opción: ")

  # Evaluar la opción seleccionada
  if opcion == "1":
    cambiar_clave()
  elif opcion == "2":
    print("Gracias por usar el simulador. ¡Hasta luego!")
  else:
    print("Opción inválida. Intente nuevamente.")

# Ejecutar la función principal
if __name__ == "__main__":
  main()
