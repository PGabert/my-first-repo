def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
mi_lista = [1, 2, 3, 4, 5]
resultado = suma_lista(mi_lista)
print("El resultado total:", resultado)

def multi_lista(lista):
    multi = 1  # Cambié el valor inicial a 1 para que la multiplicación funcione correctamente
    for elemento in lista:
        multi *= elemento
    return multi

mi_lista = [2, 4, 5, 7, 9, 25, 8]
resultado = multi_lista(mi_lista)
print("El resultado de toda la lista:", resultado)


