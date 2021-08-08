
def ordenar():
    lista = [5,6,5,1,2,3]
    count = 1
    #while (count == 1):
       # numero = input('agrega un numero entero: ')
      #  lista.append(numero)
     #   print (lista)
    #    count = int(input('¿quieres continuar agregando?  si=1/no=0 :'))
    lista.sort()
    valorF = ""
    if lista[0] < lista[1]:
        valorF = "correcto"
    return valorF
def diccionario(diccionario):
    count = 0
    for lista in diccionario:
        print(lista['nombre'])
        if lista['edad'] >=18:
            count = count +1
    print(count)
    return count
