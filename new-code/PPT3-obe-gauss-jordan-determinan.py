import numpy as np

# Helper function
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
def gaussAlgorithm(matrix):
    swap = 0        # hitung berapa kali tukar baris
    row = len(matrix)
    M = [r[:] for r in matrix]      # copy matrix ke M, aku gk mau modif matrix awal, resiko kehilangan data awal
    step = 1

    for j in range(row): # loop tiap kolom, jadi dia bisa drive gauss (sebagai index baris) sekaligus nentuin pivot
        pivot = M[j][j]
        if pivot == 0:
            # lakukan tukar baris
            for i in range(j+1, row): # loop tiap baris, cari pivot != 0 di bagian bawah
                if M[i][j] != 0:
                    print(f"Iterasi ke-{step}: Tukar baris ke-{j+1} dengan baris ke-{i+1}")
                    print()
                    M[j], M[i] = M[i], M[j] # menukar baris
                    tampilkanMatrix(M)
                    print()
                    step += 1
                    swap += 1
                    pivot = M[j][j]
                    break
        
        # sudah ketemu pivot kita eliminasi
        for i in range(j+1, row): # loop tiap baris ke bawah, kek di bagian tukar baris
            if M[i][j] == 0: continue

            pengali = M[i][j] / pivot
            print(f"Iterasi ke-{step}: Baris ke-{i+1} = Baris ke-{i+1} - ({pengali:.2f}) * Baris ke-{j+1}")
            print()

            for c in range(row): # loop tiap kolom buat OBE. Kita pakai row juga soalnya row == col (bisa dihitung determinannya)
                M[i][c] -= pengali * M[j][c] # j adalah index baris si pivot. Karena pivotnya selalu M[j][j]

            tampilkanMatrix(M)
            print()
            step += 1

    return M, swap


def showStepGaussDeterminant(matrix):
    print(f"===Determinan matrix dengan Algoritma Gauss===")
    print()
    print("Matrix Input:")

    tampilkanMatrix(matrix)
    print()
    row = len(matrix)
    col = len(matrix[0])

    if row == col:
        print(f"Iterasi OBE gauss untuk menentukan determinan matrix {row} x {col}")
        print()
        M, swap = gaussAlgorithm(matrix)
        det = 1
        elemenDiagonal = []

        for i in range(row):
            elemenDiagonal.append(f"({M[i][i]})")
            det *= M[i][i]

        tandaSwap = pow(-1, swap)
        det *= tandaSwap
        print("Hasil determinan matrix input:")
        tampilkanMatrix(matrix)
        print()

        print("Menjadi matrix segitiga atas:")
        tampilkanMatrix(M)
        print()

        print("Determinan = " + " * ".join(elemenDiagonal))
        print(f"Hasil akhir: {det:.2f}, karena ada {swap} kali tukar baris")
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

showStepGaussDeterminant(inputMatrix)