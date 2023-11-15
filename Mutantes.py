def isMutant(dna):
    num_filas = len(dna)
    num_columnas = len(dna[0])
    contador = 0

    #Chequea la matriz de forma horizontal y vertical
    for fila in dna:
        for i in range(num_columnas -3):
            if fila [i] == fila [i + 1] == fila [i + 2] == fila [i + 3]:
                contador += 1

    for i in range(num_columnas):
        columna = ''
        for fila in dna:
            columna += fila[i]

        for j in range(num_filas -3):
            if columna[j] == columna[j + 1] == columna[j + 2] == columna[j + 3]:
                contador += 1

    #Chequea la matriz de forma diagonal, izquierda a derecha
    for i in range(num_filas -3):
        for j in range(num_columnas -3):
            if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                contador += 1

    #Chequea la matriz de forma diagonal, derecha a izquierda
    for i in range(num_filas -3):
        for j in range(num_columnas - 1, 2, -1):
            if dna[i][j] == dna[i + 1][j - 1] == dna[i + 2][j - 2] == dna[i + 3][j - 3]:
                contador += 1

    #Si el contador cuenta más de 1 caso, devuelve un True para el caso mutante
    return contador > 1

print("Ingrese las filas para la matriz de mutantes")
dna = []
for i in range(6):
    input_fila = input("Ingrese la fila N°" + str(i + 1) + ": ")
    dna.append(input_fila)

print("-----------------------------------------------")
print("RESULTADO:")
print(" ")

if isMutant(dna):
    print("Es un mutante.")
else:
    print("No es un mutante.")

print(" ")
print("Fin del programa.")
