print("--------Calculador Multifuncion------")

numero1 = int(input("Ingrese el primer digito: "))
numero2 = int(input("Ingrese el segundo digito: ")) 

opcion = input("Presiona ENTER")

print("RESULTADOS:")

def suma(numero1, numero2):
    return numero1 + numero2
resultado = numero1 + numero2
print("---SUMA;", resultado)


def resta(numero1, numero2):
    return numero1 - numero2
resultado = numero1 - numero2
print("---RESTA;", resultado)


def suma(numero1, numero2):
    return numero1 * numero2
resultado = numero1 * numero2
print("---MULTIPLICACION;", resultado)


def suma(numero1, numero2):
    return numero1 / numero2
resultado = numero1 / numero2
print("---DIVISION;", resultado)




