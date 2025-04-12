#Escribe un programa que intente dividir dos números.
#Si el segundo número es cero,captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.



def dividir_numeros(num1, num2):
  try:
    resultado = num1 / num2
    print(f"El resultado de {num1} dividido por {num2} es: {resultado}")
  except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")

dividendo1 = 10
divisor1 = 2
dividir_numeros(dividendo1, divisor1)

dividendo1 = 10
divisor1 = 0
dividir_numeros(dividendo1, divisor1)
