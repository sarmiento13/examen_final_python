"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""

def encontrar_menor_y_mayor(lista):
    if not lista: 
        return {}  
    menor = lista[0]  
    mayor = lista[0]  
    
    for numero in lista:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
    
    resultado = {
        'menor': menor,
        'mayor': mayor
    }
    
    return resultado

lista_numeros = [4, 7, 8, 2, 10, 4, 1, 0]
resultado = encontrar_menor_y_mayor(lista_numeros)
print(resultado)