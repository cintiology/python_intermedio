#Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
def buscar_mascota(*mascotas):
  
  mascota_buscar = input("Ingresá un nombre: ")
  encontrada = mascota_buscar in mascotas  

  resultado = f"El nombre de '{mascota_buscar}' {'fue encontrado' if encontrada else 'no fue encontrado'} en la lista de mascotas."
  return resultado


resultado_busqueda = buscar_mascota("rosita", "lila", "esme", "oli")
print(resultado_busqueda)

