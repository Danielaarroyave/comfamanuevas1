opcion=100
print("empanadas el machetico")
print("**********************?\n")

print("1. registar empanadas")
print("2. ver empanada")
print("0. salir")

empanadas=[]

while opcion != 0:
    opcion=int (input("digita una opcion: "))
    if opcion==1:
       empanada=input("escriba el nombre de la empanada: ")
       empanadas.append(empanada)
    elif opcion==2:
        for empanada in empanadas:
            print(f"la empanada es: {empanada}")

    
    elif opcion==0:
        break
    else:
        print("selecciona una opcion valida...")


