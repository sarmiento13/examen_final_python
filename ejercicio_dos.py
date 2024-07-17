"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
def filtrar_primos(lista):
    """Función que filtra los números primos de una lista."""
    return list(filter(es_primo, lista))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = filtrar_primos(numeros)
print(primos)