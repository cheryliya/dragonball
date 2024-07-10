import csv
import random
luchadores=('vegeta','goku','trunks','krilin','gohan')
lista=[]
l=[]
for x in luchadores:
    l=[x]
    lista.append(l)
def asignar():
    asignar_ki=random.randint(1000,100000)
    return asignar_ki
def categoria(ki):
    if ki>=1000 and ki<=10000:
        cat="Terricola"
    if ki>=10001 and ki<=50000:
        cat="Luchador"
    if ki>=50001 and ki<=100000:
        cat="Titan"
    return cat
def imprimir(lista):
    print("TERRICOLAS")
    for x in lista:
        if x[2]=="Terricola":
            print(x)
    print("LUCHADORES")        
    for x in lista:
        if x[2]=="Luchador":
            print(x)
    print("TITANES")
    for x in lista:
        if x[2]=="Titan":
            print(x)
def promedio(lista):
    acum=0
    cantidad=len(lista)
    for x in lista:
        acum=acum+x[1]
        prom=acum/cantidad
    return prom
def mayor(lista):
    acum1=0
    for x in lista:
        if x[1]>acum1:
            acum1=x[1]
    return acum1
def menor(lista):
    acum2=100000
    for x in lista:
        if x[1]<acum2:
            acum2=x[1]
    return acum2
def patriarca(lista):
    for x in lista:
        ki_aumentado=x[1]*1.25
        x.append(ki_aumentado)
    return ki_aumentado    
estado_ki=False
while True:
    print("MENU")
    print("1- asigsnr ki")
    print("2.- imiprimir y ordenar luchadores")
    print("3.- estadistica")
    print("4.- generar bbdd")
    print("6.- salir")
    print("----------")

    op=int(input("ingrese una opcion:"))

    if op==1:
        print(".-. ASIGNAR KI.-.-")
        if estado_ki==False:
            for x in lista:
                ki_asignado=asignar()
                cat_ki=categoria(ki_asignado)
                x.append(ki_asignado)
                x.append(cat_ki)
            print("ki asignado")
            estado_ki=True
        else:
            print("El ki ya fue asignado")
            print("-------")
    elif op==2:
        print("imprimir y ordenar luchadores")
        imprimir(lista)
        print("------")
    elif op==3:
        print("estadisticas")
        prom_ki=promedio(lista)
        maximo=mayor(lista)
        minimo=menor(lista)
        print(f"El promedio es:{prom_ki}")
        print(f"El mayor es:{maximo}")
        print(f"El menor es:{minimo}")
        print("---------")
    elif op==4:
        print("generar bbdd")
        with open("luchadores.csv",'w',newline="")as luchadores:
            escribircsv=csv.writer(luchadores)
            escribircsv.writerow(["nombre","ki","categoria"])
            escribircsv.writerows(lista)
            print("archivo generado")
    elif op==5:
        print("llamando al patriarca")
        patriarca(lista)
        print("---------")
    elif op==6:
        print("Saliendo....")
        break
    else:
        print("ingrese una opcion valida")
           
