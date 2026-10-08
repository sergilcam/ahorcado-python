# Ruta del fichero
ruta = "/home/sergilcam/python/frases.txt"

# 1. Crear el fichero si no existe
# El modo "a" crea el fichero en caso de que no exista
with open(ruta, mode="a", encoding="utf-8"):
    pass

# 2. Leer y mostrar por pantalla el contenido actual
print("Contenido actual del fichero:")
with open(ruta, mode="r", encoding="utf-8") as fichero:
    print(fichero.read())

# 3. Pedir cinco frases y agregarlas a las existentes
for i in range(0, 5):
    frase = input("Dime una frase:")
    with open(ruta, mode="a", encoding="utf-8") as fichero:
        print(frase, file=fichero)

# 4. Mostrar el contenido final para comprobar que se han agregado
print("Contenido final del fichero:")
with open(ruta, mode="r", encoding="utf-8") as fichero:
    print(fichero.read())
