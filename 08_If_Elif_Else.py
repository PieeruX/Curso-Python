# Calificación de un examen: Escribe un programa que tome la calificación de un examen (un número entre 0 y 10) como entrada y muestre "Aprobado" si la calificación es 5 o superior, y "Reprobado" si es inferior a 5.

calificacion = float(input("Ingrese la clasificación del examen: "))

if calificacion < 0:
    print("La nota no pude ser negativa")

elif 5.0 < calificacion < 6.0:
    print("Aprobado por los pelos")

elif 6.0 <= calificacion < 8.0:
    print("Aprobado")

elif 9.0 <= calificacion <= 10.0:
    print("Eres un crack, aprobadísimo")

elif calificacion < 5.0:
    print("Prueba más suerte a la próxima estudiando")

else:
    print("Esa nota no existe")

#Número par o impar: Escribe un programa que solicite al usuario ingresar un número entero y luego determine si ese número es par o impar.

numero = int(input("Dime un número entero y te ditré si es par o impar: "))

if numero % 2 == 0:
    print("Este número es par")

else:
    print("Este número es impar")

# Calculadora simple: Escribe un programa que solicite al usuario ingresar dos números y luego solicite que ingrese una operación (+, -, *, /). Realiza la operación correspondiente e imprime el resultado.

print("Dime dos números y luego la operación que quieres que le apliquemos")
entrada = input("Ingrese dos números y la operación separados por espacios (ejemplo: 5 + 3): ")

numero1, operacion, numero2 = entrada.split()

numero1 = float(numero1)
numero2 = float(numero2)

if operacion == "*":
    print(numero1 * numero2)
elif operacion == "+":
    print(numero1 + numero2)
elif operacion == "-":
    print(numero1 - numero2)
elif operacion == "/":
    if numero2 != 0:
        print(numero1 / numero2)
    else:
        print("Error, no se puede dividir por 0")
else:
    print("Esa operación no existe, por favor pon una con la que si se pueda realizar (*, +, -, /)")