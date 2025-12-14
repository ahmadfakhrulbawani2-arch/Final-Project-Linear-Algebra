# Helper function
def invalidInputMessageDeterminan(r, c):
    print(f"Determinan tidak dapat ditentukan untuk matrix berukuran {r} x {c}")
    print("Hanya dapat menghitung matrix persegi (n x n)")
    print()

def tampilkanMatrix(matrix):
    for row in matrix:
        atur = ["{:.2f}".format(x) for x in row]
        print("     [" + ", ".join(atur) + "]")


# spesific function
def usingGaussJordanInversion(M, I):
    row = len(M)
    col = len(M[0])
    step = 1
    swap = 0

    print("Proses OBE")
    print()

    for j in range(row):
        pivot = M[j][j]

        if pivot == 0:
            for i in range(j+1, row):
                if M[i][j] != 0:
                    print(f"Iterasi ke-{step}: Tukar baris ke-{j+1} dengan baris ke-{i+1}")
                    M[i], M[j] = M[j], M[i]
                    I[i], I[j] = I[j], I[i]
                    print("Matrix menjadi: ")
                    aug = []
                    for baris in range(row):
                        aug.append(M[baris] + I[baris])

                    tampilkanMatrix(aug)
                    print()
            
        if pivot == 0: continue # jaga2 kalo masih 0 kita continue ke kolom berikutnya bro

        # normalisasi pivot menjadi 1 utama
        if pivot != 1:
            print(f"Iterasi ke-{step}: Normalisasi baris ke-{j+1} / ({pivot:.2f})")
            print()
            for c in range(row): # loop tiap kolom di baris ke j (karena pivot di M[j][j])
                M[j][c] /= pivot
                I[j][c] /= pivot

            aug = []
            for baris in range(row):
                aug.append(M[baris] + I[baris])

            tampilkanMatrix(aug)
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
                I[r][c] -= pengali * I[j][c]

            aug = []
            for baris in range(row):
                aug.append(M[baris] + I[baris])

            tampilkanMatrix(aug)
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
                I[r][c] -= pengali * I[j][c]

            aug = []
            for baris in range(row):
                aug.append(M[baris] + I[baris])

            tampilkanMatrix(aug)
            print()
            step += 1
    
    return M, I, swap




def showStepGaussJordanInversion(matrix):
    print(f"===Invers Matrix Menggunakan Gauss Jordan")
    print()
    print("Input matrixnya:")
    tampilkanMatrix(matrix)
    print()

    row = len(matrix)
    col = len(matrix[0])

    M = [r[:] for r in matrix]
    I = [] # buat matrix identitas

    if row != col: 
        print("Tidak dapat ditentukan inversnya")
        invalidInputMessageDeterminan(row, col)
        return
    else:
        for i in range(row):
            I.append([])
            for j in range(col):
                if j == i:
                    I[i].append(1)
                else:
                    I[i].append(0)
    
    M , I, swap = usingGaussJordanInversion(M, I)

    print("Matrix awal:")
    tampilkanMatrix(matrix)
    print()
    print("Menjadi identitas:")
    tampilkanMatrix(M)
    print()
    print("Matrix inversnya:")
    tampilkanMatrix(I)
    print()
    print(f"Telah dilakukan {swap} kali tukar baris")


# main driver
inputMatrix = [
    [1, 1, 1],
    [1, 2, 3],
    [1, 4, 9],
]

showStepGaussJordanInversion(inputMatrix)