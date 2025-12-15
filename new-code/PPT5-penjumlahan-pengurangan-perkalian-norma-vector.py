import numpy as np
'''
numpy yang sudah / akan digunakan:
1. np.linalg.det()
2. np.sqrt()
'''

# helper function
def tampilkanMatrix1D(v):
    print("[", end = '')
    print(", ".join(f"{x:.2f}" for x in v), end = '')
    print(']')

def displayInput(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    V{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

# spesific function
def tambah(vectors):
    print("\n=== Kamu memilih operasi tambah vektor ===\n")

    print("Vector inputnya:\n")

    displayInput(vectors)

    # cari panjang maksimum vector
    # maxLen = 0

    # for i, v in enumerate(vectors):
    #     if len(v) > maxLen:
    #         maxLen = len(v)

    maxLen = max(len(v) for v in vectors)
    
    # penjumlahan semua vector
    W = [0] * maxLen # set semua elemen W ke 0
    for v in vectors:
        for i in range(len(v)):
            W[i] += v[i] # tambah tiap ada vector ke result

    print("=== Hasil penjumlahan vektor ===\n")
    print("    W =", end=' ')
    tampilkanMatrix1D(W)
    print()

    # Warning message jika ukuran berbeda
    if len(set(len(v) for v in vectors)) > 1:
        print(f"Perhatian: ukuran vektor berbeda, elemen yang tidak ada dianggap 0.\n")

def kurangi(vectors):
    # cari panjang maksimum vector
    maxLen = 0
    maxIdx = 0

    for i, v in enumerate(vectors):
        if len(v) > maxLen:
            maxLen = len(v)
            maxIdx = i
    
    W = list(vectors[maxIdx])

    print("\n=== Kamu memilih operasi pengurangan vektor ===\n")
    print("Perhatian: sistem memilih vektor terpanjang yang akan dikurangi vektor yang lebih pendek (atau sesuai urutan input)\n")
    print("Vektor terpanjang adalah W\n")
    print("    W =", end = ' ')
    tampilkanMatrix1D(W)
    print()

    print("Akan dikurangi dengan:\n")
    for i, v in enumerate(vectors):
        if i == maxIdx: continue
        print(f"    V{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

    # operasi pengurangan
    for v in vectors:
        if len(v) == maxLen: continue
        for i in range(len(v)):
            W[i] -= v[i] # kurangi tiap ada vector ke result

    print("=== Hasil pengurangan vektor ===\n")
    print("    W =", end=' ')
    tampilkanMatrix1D(W)
    print()

    # Warning message jika ukuran berbeda
    if len(set(len(v) for v in vectors)) > 1:
        print(f"Perhatian: ukuran vektor berbeda, elemen yang tidak ada dianggap 0.\n")

def kaliSkalar(vectors, skalar):
    print("\n=== Kamu memilih operasi perkalian skalar dengan vektor ===\n")
    print("Vector inputnya:\n")

    displayInput(vectors)

    print(f"Input skalarnya: {skalar}\n")

    for v in vectors:
        for i in range(len(v)):
            v[i] *= skalar

    print("=== Hasil pengurangan vektor ===\n")

    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    V{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def normaVector(vectors):
    print("\n=== Kamu memilih operasi norma vector ===\n")
    print("Vector inputnya:\n")

    displayInput(vectors)

    norm = [0] * len(vectors)
    kalkulasi = []
    for i, v in enumerate(vectors):
        kalkulasi.append([])
        for j in range(len(v)):
            norm[i] += pow(v[j], 2)
            kalkulasi[i].append(f"({v[j]})^2")

    norm = np.sqrt(norm)

    print("=== Hasil norma vektor ===\n")
    for i in range(len(vectors)):
        print(f"    Norma V{i+1} = sqrt[" + " + ".join(kalkulasi[i]) + "]")
        print(f"    Hasil akhir = {norm[i]:.2f}")
        print()

    print("FYI: sqrt(x) = akar kuadrat dari x atau x^0.5")

def jarakVector(vectors):
    print("\n=== Kamu memilih operasi jarak vector ===\n")
    print("Vector inputnya:\n")

    displayInput(vectors)

    print("=== Hasil jarak kedua vektor masing-masing ===\n")
    for i, Uvec in enumerate(vectors):
        for j, Vvec in enumerate(vectors[i+1:], start = i+1):
            # alternatif pakai itertools ( from itertools import combinations )
            # for (i, U), (j, V) in combinations(enumerate(vectors), 2):
            U = Uvec
            V = Vvec

            maxLen = max(len(U), len(V))
            kalkulasi = []
            jarak = 0.0

            for n in range(maxLen):
                Un = U[n] if n < len(U) else 0
                Vn = V[n] if n < len(V) else 0
                jarak += pow(Un - Vn, 2)
                kalkulasi.append(f"({Un:.2f} - {Vn:.2f})^2")

            jarak = np.sqrt(jarak)
            print(f"    Jarak V{i+1} ke V{j+1} = sqrt[" + " + ".join(kalkulasi) + "]")
            print(f"    Jarak akhir = {jarak:.2f}\n")

            # Warning message jika ukuran berbeda
            if len(U) != len(V):
                print(f"    Perhatian: ukuran vektor berbeda, elemen yang tidak ada dianggap 0.\n")

# main driver-------------------------
# pilih operasi
opsi = 5
# vector input
u = [1, 2, 3]
v = [4, 5]
j = [3, 4, 5]
k = [1, 3, 0.2]
l = [0.0, 7, 6.6352, 932, 329839]

vectors = [u, v, j, k, l]

# kalo perkalian skalar
skalar = 2

# bracnch ke operasi yang dipilih
match opsi:
    case 1:
        tambah(vectors)
    case 2:
        kurangi(vectors)
    case 3: 
        kaliSkalar(vectors, skalar)
    case 4:
        normaVector(vectors)
    case 5:
        jarakVector(vectors)