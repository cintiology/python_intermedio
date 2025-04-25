#Escribe un un programa que intente abrir un archivo que no existe.
# Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje 
# de error al usuario. Sin embargo, también intenta crear el archivo si no existe.
nombre_archivo = "un_archivo.txt"  

try:
    with open(nombre_archivo, "r") as f:
        print(f.read())
except FileNotFoundError:
    print(f"El archivo que intentas abrir:'{nombre_archivo}' no existe. Intentando crear el archivo...")
    with open(nombre_archivo, "w") as f:
        f.write("este es un nuevo archivo.")
finally:  
    print("Operación exitosa!.")
