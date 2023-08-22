# Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena.
# Pautas de evalucion:
# +Solo esta permitido utilizar la funcion, input(), print() y las creadas por uno mismo
#  Aclaracion:
#  Si recibe "Qué lindo día que hace hoy" debe devolver: {'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}


#Se necesita instalar pip install unidecode
from unidecode import unidecode

def sacar_acentos_y_convertir_minusculas(texto):
    aux=unidecode(texto).lower()
    return aux

def separar_palabras(texto, palabras=None):
    if palabras is None:
        palabras=[]

    if " " in texto:
        index = texto.index(" ")
        palabras.append(texto[:index])
        return separar_palabras(texto[index+1:], palabras)
    else:
        palabras.append(texto)
        return palabras

def contar_palabras_en_la_lista(lista):
    diccionarioDePalabras={}
    for palabra in lista:
        if (palabra in diccionarioDePalabras):
            diccionarioDePalabras[palabra] += 1
        else:
            diccionarioDePalabras[palabra] = 1
    return diccionarioDePalabras

def contar_palabras():
    texto=input("Ingrese una frase:\n")
    aux=sacar_acentos_y_convertir_minusculas(texto)
    palabras_separadas=separar_palabras(aux)
    diccionario=contar_palabras_en_la_lista(palabras_separadas)
    return diccionario


print(contar_palabras())
