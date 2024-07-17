"""
crear un diccionario que tenga dos registros de un alumno
1. crear un funcion que me imprima los registro,
2. crear una funcion que me permita editar uno de los campos del registro
"""
alumno = {
    'nombre': 'Juan',
    'edad': 20,
    'apellidos':'ramos'
}
{
    'nombre': 'luz',
    'edad': 20,
    'apellidos':'rojas'
}

def imprimir_registros():
    print("Registros del alumno:")
    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")

def editar_registro(campo, nuevo_valor):
    if campo in alumno:
        alumno[campo] = nuevo_valor
        print(f"Campo '{campo}' actualizado correctamente.")
    else:
        print(f"El campo '{campo}' no existe en los registros.")

imprimir_registros()
editar_registro('edad', 22)
imprimir_registros()
