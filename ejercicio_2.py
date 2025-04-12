#Escribe un programa que intente sumar un número y una cadena. 
#Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.


def sumar_numero_cadena(numero, cadena):
  
  try:
    resultado = numero + cadena
    print(f"El resultado de sumar {numero} y '{cadena}' es: {resultado}")
  except TypeError:
    print("¡Error! No se puede sumar un número y una cadena")

# Ejemplo de uso:
numero = 10
cadena = "Hola"
flotante = 3.14

sumar_numero_cadena(numero, cadena)
sumar_numero_cadena(flotante, cadena)
sumar_numero_cadena(numero, 5)