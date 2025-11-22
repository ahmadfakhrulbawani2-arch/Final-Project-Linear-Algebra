import numpy as np

def calcDet(A):
    D = np.linalg.det(A)
    return D

def printMatrix(M):
    for row in M:
        print("   ", row)
    print()

def gaussStep(matrix3):
    n = len(matrix3)
    A = [row[:] for row in matrix3]   # copy matrix
    step = 1

    print("Process of Gauss-Jordan Elimination:\n")
    
    for i in range(n):
        pivot = A[i][i]

        # Jika pivot = 0 maka cari baris lain
        if pivot == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    print(f"Iteration-{step}: Swapping R{i+1} <-> R{k+1}")
                    A[i], A[k] = A[k], A[i]
                    printMatrix(A)
                    step += 1
                    pivot = A[i][i]
                    break

        # Jika tetap 0 maka tidak bisa ditentukan
        if pivot == 0:
            continue

        # Normalisasi pivot: yaitu jadikan 1 utama
        print(f"Iteration-{step}: Normalizing R{i+1} (divide by {pivot:.2f})")
        for c in range(len(A[0])):
            A[i][c] /= pivot
        printMatrix(A)
        step += 1

        # Eliminasi ke semua baris lain (Gauss-Jordan)
        for r in range(n):
            if r == i:
                continue
            if A[r][i] == 0:
                continue

            factor = A[r][i]
            print(f"Iteration-{step}: R{r+1} = R{r+1} - ({factor:.2f}) * R{i+1}")

            for c in range(len(A[0])):
                A[r][c] -= factor * A[i][c]

            printMatrix(A)
            step += 1

    print("Final Diagonal Matrix Form:")
    printMatrix(A)

    return A

def solveFromDiagonal(matrix3):
    row = len(matrix3)
    col = len(matrix3[0])
    vars = col - 1

    solutions = []

    for i in range(vars):
        # Jika diagonal = 0
        if abs(matrix3[i][i]) < 1e-9:
            if abs(matrix3[i][col-1]) < 1e-9:
                return None, "infinite"
            else:
                return None, "nosolution"

        solutions.append(matrix3[i][col-1])

    return solutions, "ok"

def showSol(matrix3):
    row = len(matrix3)
    col = len(matrix3[0])

    if row < col - 1:
        print("Not enough equations to determine a unique solution.\n")
        return
    
    print("The matrix is:\n")
    printMatrix(matrix3)
    print("Solution:\n")

    finalM = gaussStep(matrix3)
    sol, status = solveFromDiagonal(finalM)

    print("So the solution is:\n")

    if status == "nosolution":
        print("No solution (inconsistent equations)")
    elif status == "infinite":
        print("Infinite solutions (underdetermined system)")
    else:
        for i, val in enumerate(sol):
            print(f"x{i+1} = {val:.4f}")



# test sample
A1 = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3],
]

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

showSol(A1)
