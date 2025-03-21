#Ejercicio 1
def saludar():#Funcion que nos imprimr el mensaje, esta funcion no necesita parametros
    print("Hola,bienvenido a Python")

saludar()#aqui estamos llamando la funcion para mostrar el mensaje

#Ejercicio 2
print("Ejercicio de la Suma")

def sumar(a,b):#Esta funcion ocupamos los parametros a y b que ingreso el usuario
    suma=a+b#aqui realiza la operacion
    return suma#returna el resultado de la suma

#Le pide al usuario los numeros
a=int(input("Ingrese el numero A: "))
b=int(input("Ingrese el numero B: "))


print(f"El resultado es: {sumar(a,b)}")#Imprime el resultado

#Ejercicio 3
print("Ejercicio de la Suma")

def multi(a,b):#Esta funcion ocupamos los parametros a y b que ingreso el usuario
    multi=a*b#aqui realiza la operacion
    return multi#returna el resultado de la multiplicacion

#Le pide al usuario los numeros
a=int(input("Ingrese el numero A:"))
b=int(input("Ingrese el numero B: "))


print(f"El resultado es: {multi(a,b)}")#Imprime el resultado

#Ejercicio 4
def verificar_edad():#funcion que ayuda para verificar la edad
        if edad>=18:#Si la edad es mayor o igual a 18
            print("Eres mayor de edad")
        else:#Si la edad es menor que 18
            print("Eres menor de edad")

edad=int(input("Escriba tu edad: "))#El usuario ingresa su edad

verificar_edad()#llamamos la funcion he imprime los mensaje

#Ejercicio 5
Lista=[50,30,45,10]#la lista de las notas

def calcular_promedio(Lista):#la funcion para calcular el promedio
#El promedio se realiza mediante se suma todos los elementos de la lista y se divide con la cantidad que tiene la lista para eso utilizamos len()
    promedio=sum(Lista)/len(Lista)
    return promedio#returna el promedio

print(f"El promedio de las notas es: {calcular_promedio(Lista)}")#imprimimos el promedio