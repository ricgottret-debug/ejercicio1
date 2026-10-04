# Calculadora simple
print("Selecciona una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Introduce el número de la operación (1/2/3/4): ")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if opcion == '1':
    print(f"Resultado: {num1 + num2}")
elif opcion == '2':
    print(f"Resultado: {num1 - num2}")
elif opcion == '3':
    print(f"Resultado: {num1 * num2}")
elif opcion == '4':
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida.")
