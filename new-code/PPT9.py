import numpy as np
# Yang aku skip adalah jarak 2 bidang sejajar sama komposisi transformasi

# helper function
def tampilkanMatrix1D(v):
    print("[", end = '')
    print(", ".join(f"{x:.2f}" for x in v), end = '')
    print(']')

def displayInput3(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    P{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput2(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    E{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput8(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    T{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def tampilkanMatrix(matrix):
    for row in matrix:
        atur = ["{:.2f}".format(x) for x in row]
        print("    [" + ", ".join(atur) + "]")

def displayInput(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    V{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def degToRad(res):
    ans = res * (np.pi / 180)
    return ans

# Spesific function
def tampilkanPersamaan(matrix):
    row = len(matrix)
    col = len(matrix[0])
    variabel = col - 1
    vars = "XYZ"
    
    for i in range(row):
        left = []
        for j in range(variabel):
            coef = matrix[i][j]
            left.append(f"({coef:.2f}){vars[i]}")

        lhs = " + ".join(left)
        rhs = matrix[i][col-1]
        rhs *= -1

        print(f"    {lhs} = {rhs:.2f}")

def tampilkanPersamaan1D(matrix):
    variabel = len(matrix) - 1
    vars = "XYZ"

    left = []
    for j in range(variabel):
        coef = matrix[j]                     
        left.append(f"({coef:.2f}){vars[j]}")

    lhs = " + ".join(left)
    rhs = -matrix[-1]                        

    print(f"    {lhs} = {rhs:.2f}")

        

def persParam(P):
    print("\n=== Kamu memilih operasi hitung persamaan parametrik melalui 2 titik ===\n")
    print("Vektor input:\n")

    displayInput3(P)
    
    for i, P1 in enumerate(P):
        for j, P2 in enumerate(P):
            if j == i: continue

            print(f"Persamaan parametrik untuk garis l melalui titik P{i+1} dan P{j+1} dengan P0 di P{i+1}\n")
            print(f"    Rumus: P0P * V")
            PP = np.array(P1) - np.array(P2)
            print(f"    V = P2 - P1 =", end = ' ')
            tampilkanMatrix1D(PP)
            print()

            res = []
            vars = "XYZ"
            for k in range(3):
                res.append(f"{vars[k]} = {P1[k]:.2f} + ({PP[k]:.2f})t")

            print(f"    Hasil persamaan: " + "\n                     ".join(res))
            print()

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
                    print(f"    Iterasi ke-{step}: Tukar baris ke-{j+1} dengan baris ke-{i+1}")
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
            print(f"    Iterasi ke-{step}: Normalisasi baris ke-{j+1} / ({pivot:.2f})")
            print()
            for c in range(col): # loop tiap kolom di baris ke j (karena pivot di M[j][j])
                M[j][c] /= pivot
            tampilkanMatrix(M)
            print()
            step += 1

        # eliminasi ke semua baris di bawahnya dulu
        for r in range(j+1, row):
            if r == j or M[r][j] == 0: 
                continue 

            pengali = M[r][j]
            print(f"    Iterasi ke-{step}: Baris ke-{r+1} - ({pengali:.2f}) * Baris ke-{j+1}")
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
            print(f"    Iterasi ke-{step}: Baris ke-{r+1} - ({pengali:.2f}) * Baris ke-{j+1}")
            print()
            for c in range(col):
                M[r][c] -= pengali * M[j][c]

            tampilkanMatrix(M)
            print()
            step += 1
    
    print("    Matrix diagonal akhir:")
    print()
    tampilkanMatrix(M)
    print()
    print("    Atau persamaan:")
    tampilkanPersamaan(M)
    return M


def parametrikPotong2Bdg(E):
    print("\n=== Kamu memilih operasi hitung persamaan parametrik yang memotong 2 bidang ===\n")
    print("Input persamaan:\n")
    displayInput3(E)

    for i, E1 in enumerate(E):
        for j, E2 in enumerate(E[i+1:], start = i+1):
            ETEMP = [E1, E2]

            print(f"Persamaan yang berpotongan antara E{i+1} dengan E{j+1}:\n")
            print(f"    Rumus: X1 = X2, Y1 = Y2, Z1 = Z2\n")
            print(f"    Langkah penyelesaian dengan gauss-jordan:\n")
            SOL = iterateGaussJordan(ETEMP)
            
            res = []
            vars = "XYZ"
            for k in range(2):
                res.append(f"{vars[k]} = {SOL[k][3]:.2f} + ({-1 * SOL[k][2]:.2f})t")
            
            res.append(f"{vars[2]} = t")
            print()
            print(f"    Hasil persamaan: " + "\n                     ".join(res))

def persSimet(Simet):
    print("\n=== Kamu memilih operasi hitung persamaan simetri diketahui X, Y, Z ===\n")
    for k, S in enumerate(Simet):
        print(f"Input persamaan S{k+1}:\n")
        vars = "XYZ"
        for i in range(3):
            print(f"{vars[i]} =", end = ' ')
            tampilkanMatrix1D(S[i])
            print()

        print("Rumus: X = Y = Z\n")

        for i, S1 in enumerate(S):
            for j,S2 in enumerate(S[i+1:], start = i+1):
                print(f"    Persamaan bidang {vars[i]} dan {vars[j]} adalah:")
                koefX = S2[1]
                koefY = -1 * S1[1]
                constanta = -1 * (S1[0] * S2[1]) + S1[1] * S2[0]
                PERS = [koefX, koefY, constanta]

                tampilkanPersamaan1D(PERS)
                print()

def jrkTtkKeBdg(TITIK, BIDANG):
    print("\n=== Kamu memilih operasi hitung jarak titik ke bidang ===\n")
    print("Input titik:\n")
    displayInput8(TITIK)
    print("Input persamaan bidang:\n")
    displayInput2(BIDANG)

    print("Rumus = |ax0 + by0 + cz0 + d| / sqrt(a^2 + b^2 + c^2)\n")

    print(f"Hasil perhitungan semua kombinasi\n")
    for i, T in enumerate(TITIK):
        for j, B in enumerate(BIDANG):
            pembilang = 0.00
            abc = []
            for k in range(3):
                pembilang += (T[k] * B[k])
                abc.append(B[k])

            pembilang += B[3]

            pembilang = abs(pembilang)

            penyebut = np.linalg.norm(abc)

            res = pembilang / penyebut

            print(f"    Hasil jarak T{i+1} ke B{j+1} = {res:.2f}")

def pencerminan(Vec):
    print("\n=== Kamu memilih operasi hitung pencerminan ke sumbu dan bidang ===\n")
    print("Input vektor:\n")
    displayInput(Vec)

    for i, V in enumerate(Vec):
        print(f"Hasil pencerminan dari V{i+1}:\n")
        vars = "XYZ"
        for j in range(3):
            tmp = V[:]
            for k in range(3):
                if k == j: continue
                else:
                    tmp[k] *= -1

            print(f"    Pencerminan terhadap sumbu {vars[j]} =", end = ' ')
            tampilkanMatrix1D(tmp)

        pairs = [vars[1]+vars[2], vars[0]+vars[2], vars[0]+vars[1]]
        for j in range(2, -1, -1):
            tmp = V[:]
            tmp[j] *= -1
            print(f"    Pencerminan terhadap bidang {pairs[j]} =", end = ' ')
            tampilkanMatrix1D(tmp)

        print()

def rotasi(Vec, Deg):
    angle = degToRad(Deg)
    print("\n=== Kamu memilih operasi hitung rotasi ke sumbu ===\n")
    print("Input vektor:\n")
    displayInput(Vec)

    for i, V in enumerate(Vec):
        print(f"Hasil rotasi V{i+1} sebesar {Deg}Deg\n")
        vars = "XYZ"
        for j in range(3):
            x0, y0, z0 = V
            cs, sn = np.cos(angle), np.sin(angle)
            poros = vars[j]

            match poros:
                case 'X':
                    x = x0
                    y, z = (y0 * cs - z0 * sn), (y0 * sn + z0 * cs)
                case 'Y':
                    x, z = (x0 * cs + z0 * sn), (-x0 * sn + z0 * cs)
                    y = y0
                case 'Z':
                    x, y = (x0 * cs - y0 * sn), (x0 * sn + y0 * cs)
                    z = z0
            
            print(f"    Rotasi V{i+1} terhadap sumbu {poros} = [{x:.2f}, {y:.2f}, {z:.2f})")
        
        print()

def dilatasi(Vec, Dil):
    print("\n=== Kamu memilih operasi hitung dilatasi / kontraksi ===\n")
    print("Input vektor:\n")
    displayInput(Vec)

    for i, V in enumerate(Vec):
        for j in range(len(V)):
            V[j] *= Dil

        print(f"Hasil dilatasi V{i+1} sebesar {Dil} kali =", end = ' ')
        tampilkanMatrix1D(V)
        print()

def proyOrthogonal(Vec):
    print("\n=== Kamu memilih operasi hitung dilatasi / kontraksi ===\n")
    print("Input vektor:\n")
    displayInput(Vec)

    for i, V in enumerate(Vec):
        vars = "XYZ"
        print(f"Hasil proyeksi orthogonal V{i+1}:\n")
        for j in range(len(vars)):
            if len(V) < 3:
                for k in range(3 - len(V)):
                    V.append(0)

            x, y, z = V

            match vars[j]:
                case 'X':
                    y, z = 0, 0
                case 'Y':
                    x, z = 0, 0
                case 'Z':
                    x, y = 0, 0

            print(f"    Proyeksi orthogonal ke sumbu {vars[j]} = [{x:.2f}, {y:.2f}, {z:.2f}]")

        print()

        pairs = [vars[1]+vars[2], vars[0]+vars[2], vars[0]+vars[1]]
        for j in range(3):
            x, y, z = V

            match pairs[j]:
                case 'XY':
                    z = 0
                case 'XZ':
                    y = 0
                case 'YZ':
                    x = 0

            print(f"    Proyeksi orthogonal ke sumbu {pairs[j]} = [{x:.2f}, {y:.2f}, {z:.2f}]")
        
        print()

def main():
    opsi = 8

    P1 = [2, 4, -1]
    P2 = [5, 0, 7]
    P3 = [3, -1, 0]
    P4 = [7, 0, 8]
    PARAMETRIK = [P1, P2, P3, P4]

    E1 = [-4, 5, -7, -388]
    E2 = [9, 6, -2, 215]
    EQUATION = [E1, E2]

    X1 = [3, 4]
    Y1 = [-3, 11]
    Z1 = [7, -12]
    S1 = [X1, Y1, Z1]

    SIMETRI = [S1]

    T1 = [1, -4, -3]
    T2 = [2, 7, -8]
    TITIK = [T1, T2]

    B1 = [-2, 3, -5, -7]
    B2 = [-6, 9, -15, -18]
    B3 = [2, -3, -6, -1]
    BIDANG = [B1, B2, B3]

    V1 = [2, -3, 5]
    V2 = [5, -3, 2]
    V = [V1, V2]
    SUDUTDEG = 90
    MULTIPLY = 2

    match opsi:
        case 1:
            persParam(PARAMETRIK)
        case 2:
            parametrikPotong2Bdg(EQUATION)
        case 3:
            persSimet(SIMETRI)
        case 4:
            jrkTtkKeBdg(TITIK, BIDANG)
        case 5:
            pencerminan(V)
        case 6:
            rotasi(V, SUDUTDEG)
        case 7:
            dilatasi(V, MULTIPLY)
        case 8:
            proyOrthogonal(V)   # menerima matriks ukuran 2 <= len(V) <= 3

# main driver
if __name__ == "__main__":
    main()