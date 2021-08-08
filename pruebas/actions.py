print("hola")

def ordenar():
    lista = []
    count = 1
    while (count == 1):
        numero = input('agrega un numero entero: ')
        lista.append(numero)
        print (lista)
        count = int(input('¿quieres continuar agregando?  si=1/no=0 :'))
    lista.sort()
    print (lista)
    return lista
valor = ordenar()
if valor[0] > valor[1]:
    print("mal")
else:
    print("funciona")
diccionarios=[
    {'nombre':'juan','edad':8},
    {'nombre':'toño','edad':10},
    {'nombre':'ana','edad':5},
    {'nombre':'sofia','edad':19},
    {'nombre':'erick','edad':22},
]
def diccionario(diccionario):
    count = 0
    for lista in diccionario:
        print(lista['nombre'])
        if lista['edad'] >=18:
            count = count +1
    print(count)
    #return count
diccionario(diccionarios)