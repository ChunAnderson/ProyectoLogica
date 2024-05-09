#ciclos en python

'''
El ciclo for está diseñado para realizar una tarea un determinado número de veces.
(predefinido)
El ciclo while se utiliza cuando no se sabe cuántas veces se va a repetir una tarea.


#Ciclo four
for variable in range(1,11):
    print(variable)

#Ciclo while
respuesta = 0
while True:
    respuesta=input('desaea agregar un valor (s/n):' )
    if respuesta=='s':
        nombre=input('Nombre:')
        correo=input('Correo')
        tel=input('Telefono')
    else:
        break

print(nombre, correo, tel)'''


numero = 0
numero2 = 1
resultado = 1

while True:
    numero = int(input('Ingrese un número (ingrese 0 para salir): '))
    
    if numero == 0:
        break
    
    resultado = 1
    numero2 = 1
    
    while numero2 <= numero:
        resultado = resultado * numero2
        numero2 += 1
    
    print("El factorial de", numero, "es:", resultado)

        
print("¡Hasta luego!")

        