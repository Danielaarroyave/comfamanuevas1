#solicitar 20 numeros (este es nuestro rango) y guardarlos en la variable numeros (se utiliza append para que quede en la lista) e imprimir lista

numeros= []
for i in range(20):
    numeros.append(input("ingrese un numero: "))


for numero in numeros:
    print(numero)