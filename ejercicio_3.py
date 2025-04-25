#Escribe un programa que intente acceder a una clave que no existe en un
#diccionario. Si se produce una excepción KeyError, captura la excepción y muestra un mensaje de error al usuario.


def acceder_clave_inexistente(diccionario, clave):
  
  try:
    valor = diccionario[clave]
    print(f"La clave '{clave}' es: {valor}")
  except KeyError:
    print(f"¡Error! La clave '{clave}' no existe")

# Ejemplo de uso:
mi_diccionario = {"nombre": "Cin", "edad": 37, "ciudad": "Glew"}

acceder_clave_inexistente(mi_diccionario, "nombre")
acceder_clave_inexistente(mi_diccionario, "profesion")
acceder_clave_inexistente(mi_diccionario, "edad")