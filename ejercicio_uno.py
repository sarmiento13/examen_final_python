"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
lista=[4,7,10,4,1,0]
def encontrar_min_y_max(lista):
    if not lista:
        return{}
    minimo = min(lista)
    maximo = max (lista)
    return{"minimo":minimo,"maximo":maximo}
#resultado = encontrar_min_y_max(lista)
#print(resultado)

print(encontrar_min_y_max([5,2,7,8,9,5]))
