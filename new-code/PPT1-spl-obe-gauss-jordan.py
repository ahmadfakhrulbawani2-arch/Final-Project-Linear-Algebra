# Helper function

def tampilkanMatrix(matrix):
    for row in matrix:
        atur = ["{:.2f}".format(x) for x in row]
        print("     [" + ", ".join(atur) + "]")

# Spesific function
def tampilkanPersamaan(matrix):
    row = len(matrix)
    col = len(matrix[0])
    variabel = col - 1

    for i in range(row):
        left = []
        for j in range(variabel):
            coef = matrix[i][j]
            left.append(f"{coef:.2f}X{j+1}")

        lhs = " + ".join(left)
        rhs = matrix[i][col-1]

        print(f"{lhs} = {rhs:.2f}")


def iterateGaussJordan(matrix):
    swap = 0        # hitung berapa kali tukar baris
    row = len(matrix)
    col = len(matrix[0])
    M = [r[:] for r in matrix]      # copy matrix ke M, aku gk mau modif matrix awal, resiko kehilangan data awal
    step = 1

    for j in range(row): # loop tiap kolom, jadi dia bisa drive gauss (sebagai index baris) sekaligus nentuin pivot. Perhatikan bahwa loop ini berhenti sampai row-1 karena kolom paling kanan tidak di-normalisasi
        pivot = M[j][j]
        if pivot == 0:
            # lakukan tukar baris
            for i in range(j+1, row): # loop tiap baris, cari pivot != 0 di bagian bawah
                if M[i][j] != 0:
                    print(f"Iterasi ke-{step}: Tukar baris ke-{j+1} dengan baris ke-{i+1}")
                    M[j], M[i] = M[i], M[j] # menukar baris
                    tampilkanMatrix(M)
                    print()
                    step += 1
                    swap += 1
                    pivot = M[j][j]
                    break
        
        if pivot == 0: continue # jaga2 kalo masih 0 kita continue ke kolom berikutnya bro

        # normalisasi pivot menjadi 1 utama
        if pivot != 1:
            print(f"Iterasi ke-{step}: Normalisasi baris ke-{j+1} / ({pivot:.2f})")
            print()
            for c in range(row): # loop tiap kolom di baris ke j (karena pivot di M[j][j])
                M[j][c] /= pivot
            tampilkanMatrix(M)
            print()
            step += 1

        # eliminasi ke semua baris di bawahnya dulu
        for r in range(j+1, row):
            if r == j or M[r][j] == 0: 
                continue 

            pengali = M[r][j]
            print(f"Iterasi ke-{step}: Baris ke-{r+1} - ({pengali:.2f}) * Baris ke-{j+1}")
            print()
            for c in range(col):
                M[r][c] -= pengali * M[j][c]

            tampilkanMatrix(M)
            print()
            step += 1

    for j in range(row-1, -1, -1):
        pivot = M[j][j]
        # skip normalisasi karena sudah dinormalisasi langsung ke eliminasi
        for r in range(j-1, -1, -1):
            if r == j or M[r][j] == 0: 
                continue 

            pengali = M[r][j]
            print(f"Iterasi ke-{step}: Baris ke-{r+1} - ({pengali:.2f}) * Baris ke-{j+1}")
            print()
            for c in range(col):
                M[r][c] -= pengali * M[j][c]

            tampilkanMatrix(M)
            print()
            step += 1
    
    print("Matrix diagonal akhir:")
    print()
    tampilkanMatrix(M)
    print()
    print("Atau persamaan:")
    tampilkanPersamaan(M)
    return M

def ambilSolusi(matrix):
    col = len(matrix[0])
    variabel = col - 1

    solusi = []

    for i in range(variabel):
        if abs(matrix[i][i]) < 1e-9: # cek apakah diagonal mendekati 0
            if abs(matrix[i][col-1]) < 1e-9: # cek apakah konstanta mendekati 0
                return None, "Gak terhingga"
            else:
                return None, "Gak onk"
        
        solusi.append(matrix[i][col-1])

    return solusi, "wes onk, aman"

def showStepGaussJordanElimination(matrix):
    print(f"===Penyelesaian SPL menggunakan OBE Gauss-Jordan===")
    print()
    print("Input matrixnya:")
    tampilkanMatrix(matrix)
    print()
    print("Atau persamaan:")
    tampilkanPersamaan(matrix)
    print()
    row = len(matrix)
    col = len(matrix[0])

    if row < col - 1: # kondisi variabel bebas
        print(f"Jumlah persamaan tidak cukup, akan ada {col - row - 1} variabel bebas")
        return

    M = iterateGaussJordan(matrix)
    solusi, status = ambilSolusi(M)

    if status == "Gak onk":
        print("Tidak ada solusi (persamaan tidak konsisten)")
    elif status == "Gak terhingga":
        print("Solusi tak hingga (sistem memiliki variabel nol semua / ada variabel bebas)")
    else:
        print()
        print("Solusinya:")
        for i, res in enumerate(solusi):
            print(f"X{i+1} = {res:.2f}")


# main driver
inputMatrix = [
    [1, 1, 1, 1],
    [1, 2, 3, 1],
    [1, 4, 9, 1],
]

showStepGaussJordanElimination(inputMatrix)