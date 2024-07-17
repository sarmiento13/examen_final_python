"""
crear un funcion que me retorne un diccioonario de la cantidad de vocales que aparecen en un texto pasado por parametro el diccionario debera ser credo por comprension de diccionarios
ejm:
entrada: eucalipto
salida: {e:1,u:1,a:1,i:1,o:1}
"""
def contar_vocales(texto):
    resultado = {}
    texto = texto.lower()
    vocales = "aeiou"

    for vocal in vocales:
        cantidad = texto.count(vocal)
        if cantidad > 0:
            resultado[vocal] = cantidad
    return resultado
texto = "eucalipto"
resultado = contar_vocales(texto)
print(resultado) 