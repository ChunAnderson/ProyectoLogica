def area_circunferencia():
    radio=float(input("Ingrese el radio de la circunferencia: "))
    return 3.1416*radio**2
    

def area_rectangulo():
    base=float(input("Ingrese la base del rectángulo: "))
    altura=float(input("Ingrese la altura del rectángulo: "))
    return base*altura
     
# ---------- còdigo principal ----------
opcion=input("area circunferencia ingrese 1, area rectangulo ingrese 2: ")
if opcion=="1":
    area_recibida=area_circunferencia()
elif opcion=="2":
    area_recibida=area_rectangulo()
else:
    print("Opción incorrecta")
    area_recibida=0
print("El área es: ", area_recibida)





