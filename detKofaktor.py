import numpy as np

def calcDet(A):
    D = np.linalg.det(A)
    return D


def printMatrix(M):
    for row in M:
        print("   ", row)
    print()


def minor(matrix, row, col):
    m = []
    
    for i in range(len(matrix)):
        if i == row:
            continue  

        new_row = []  

        for j in range(len(matrix)):
            if j == col:
                continue  

            new_row.append(matrix[i][j])

        m.append(new_row)

    return m



def showStep(matrix):
    n = len(matrix)
    c = len(matrix[0])

    # Cetak matriks awal
    print("Matriks A:")
    printMatrix(matrix)

    if(n == c):
        print(f"Ekspansi Kofaktor untuk matriks A {n}x{n}:\n")

        print("Ekspansi sepanjang baris pertama (row 0):\n")

        terms = []
        det = 0

        for j in range(n):
            sign = pow(-1, (0 + j))
            a = matrix[0][j]

            print(f"Elemen a[0][{j}] = {a}")
            if(sign > 0):
                print("Sign: positive")
            else:
                print("Sign = negative")

            # Minor
            M = minor(matrix, 0, j)
            print(f"Minor M_0{j}:")
            printMatrix(M)

            terms.append(f"({sign} * {a} * det(M_0{j}))")
            detTmp = sign * a * calcDet(M)
            det += detTmp

        print("Ekspansi lengkap determinan:\n")
        print("det(A) = " + " + ".join(terms))
        print()
        print(f"Determinant of A = {det:.2f}")
        print()
    else:
        print(f"Mohon maaf, tidak ada determinan untuk matrix A {n} x {c}")
        print("Mohon hanya inputkan matrix berordo n x n")
        print()


# === test sample ===
A = [
    [2, 3, 1, 4],
    [1, 0, -1, 2],
    [3, 1, 2, 0],
    [2, 4, 1, 3]
]

B = [
    [2,  3,  1],
    [4, -1,  2],
    [5,  0,  3]
]

C = [
    [2, 3],
    [4, 5]
]

# undefine determinant handling

D = [
    [1, 3, 2],
    [4, 6, 5]
]

showStep(A)
# showStep(B)
