print("CALCULADORA DE FACU")
num1 = int(input("Ingrese el primer digito: "))
num2 = int(input("Ingrese el segundo digito: "))

opcion = int(input("Elije una opcion [1, 2, 3, 4]"))

if opcion == 1:
    print("Resultado", num1 + num2)
elif opcion == 2:
    print("Resultado", num1 - num2)
elif opcion == 3:
    print("Resultado", num1 * num2)
elif opcion == 4:
    print("Resultado", num1 / num2)