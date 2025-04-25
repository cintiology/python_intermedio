#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
#captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario

def dividirTres (numerador, denominador):
    try:
        resultado = int(numerador) / int(denominador)

    except ZeroDivisionError:
        resultado = "Error, no se puede dividir por cero"
    except ValueError:
        resultado = "Error en el numerador o el denominador"

    return resultado
    
print(dividirTres(7, 3))
print(dividirTres(7, 0))
print(dividirTres("C", 3))