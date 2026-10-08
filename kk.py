#pedir las frases
for i in range(0,5):
    frase = input("Dime una frase:")
#guardar las frases
    ruta = "/home/sergilcam/python/frases.txt" 
    with open(ruta, mode="a", encoding="utf-8") as fichero: 
        print(frase, file=fichero) 
