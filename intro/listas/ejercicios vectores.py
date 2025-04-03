posiciones_pares = []
posiciones_impares = []

for i, num in enumerate(vector):
    if num % 2 == 0:  # Si el número es par
        posiciones_pares.append(i)
    else:  # Si el número es impar
        posiciones_impares.append(i)

# Mostrar posiciones
print("Posiciones de números pares:", posiciones_pares)
print("Posiciones de números impares:", posiciones_impares)