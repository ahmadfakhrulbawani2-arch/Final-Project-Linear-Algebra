import numpy as np

def hitungDet(matrix):
    det = np.linalg.det(matrix)
    return det

def invalidInputMessageDeterminan(r, c):
    print(f"Determinan tidak dapat ditentukan untuk matrix berukuran {r} x {c}")
    print("Hanya dapat menghitung matrix persegi (n x n)")
    print()

def tampilkanMatrix(matrix):
    for row in matrix:
        atur = ["{:.2f}".format(x) for x in row]
        print("     [" + ", ".join(atur) + "]")

# Spesific function
def minorMatrix(matrix, row, col):
    minor = []

    for i in range(len(matrix)):
        if i == row:
            continue

        newBaris = []

        for j in range(len(matrix[i])):
            if j == col:
                continue

            newBaris.append(matrix[i][j])
        
        minor.append(newBaris)

    return minor

def showStep(matrix):
    print("=== Determinan Menggunakan Ekspansi Kofaktor Baris kesatu ===")
    print("Matrix input:")
    tampilkanMatrix(matrix)
    print()
    row = len(matrix)
    col = len(matrix[0])

    if row == col:
        print(f"Determinan dari matrix input ukuran {row} x {col}:")
        det = 0
        kalkulasi = []
        for j in range (row):
            tanda = pow(-1, j)
            elemen = matrix[0][j]
            print(f"Elemen ke-{j+1}: {elemen}")
            if tanda > 0: 
                print("Tanda: Positif")
            else:
                print("Tanda: Negatif")
            
            print("Minornya:")
            minor = minorMatrix(matrix, 0, j)
            tampilkanMatrix(minor)
            print(f"Determinan minornya: {hitungDet(minor):.2f}")
            print()

            kalkulasi.append(f"{tanda} * {elemen} * det(Minor[0][{j}])")
            det += tanda * elemen * hitungDet(minor)

        print("Hasil perhitungan lengkap determinannya:")
        print("Determinan = " + " + ".join(kalkulasi))
        print()
        print(f"Hasil akhir determinan = {det:.2f}")
        print()
    else:
        invalidInputMessageDeterminan(row, col)


# main driver
inputMatrix = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3],
    [2, 4, 1, 3]
]

showStep(inputMatrix)


