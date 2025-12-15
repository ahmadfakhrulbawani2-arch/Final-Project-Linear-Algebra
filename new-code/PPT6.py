import numpy as np
'''
numpy yang sudah / akan digunakan:
1. np.linalg.det()
2. np.sqrt()
3. np.dot()
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

def displayInput2(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    E{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput3(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    P{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput4(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    r+t[{i+1}] =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput5(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    r-t[{i+1}] =", end=' ')
        tampilkanMatrix1D(v)
        print()

# spesific function
def panjangVector(V):
    res = 0
    for i in V:
        a = i * i
        res += a

    res = np.sqrt(res)
    return res

def radToDeg(res):
    ans = res * (180 / np.pi)
    return ans

def quickDot(u, v):
    res = np.dot(u, v)
    return res

def proy(U, V):
    resDot = quickDot(U, V)
    lengU = panjangVector(U)

    W1 = quickDot((resDot / pow(lengU, 2)), U)
    W2 = []

    for k, vec in enumerate(W1):
        W2.append(V[k] - vec)

    print(f"    Hasil W1 =", end = ' ')
    tampilkanMatrix1D(W1)
    print(f"    Hasil W2 =", end = ' ')
    tampilkanMatrix1D(W2)
    print()

def dotProduct(vectors):
    print("\n=== Kamu memilih operasi dot product===\n")
    print("Vektor input:\n")

    displayInput(vectors)

    print("=== Hasil dot product & sudutnya ===\n")
    for i, Uvec in enumerate(vectors):
        for j, Vvec in enumerate(vectors[i+1:], start = i+1):
            U = Uvec
            V = Vvec
            lengU = len(U)
            lengV = len(V)
            if lengU != lengV:
                print(f"Dot product tidak dapat dilakukan karena vector berbeda dimensi (V{i+1}: {lengU}d ; V{j+1}: {lengV}d)\n")
            else:
                kalkulasi = []
                ans = 0.0

                for n in range(lengV):
                    Un = U[n]
                    Vn = V[n]
                    ans += Un * Vn
                    kalkulasi.append(f"({Un:.2f} * {Vn:.2f})")

                print(f"    Hasil V{i+1} dot V{j+1} = [" + " + ".join(kalkulasi) + "]")
                print(f"    Hasil akhir = {ans:.2f}\n")

                # hitung sudut antara vector
                pjgU = panjangVector(U)
                pjgV = panjangVector(V)
                resRad = 0.0

                resRad = np.acos(ans / (pjgU * pjgV))
                resDeg = radToDeg(resRad)
                print(f"    Hasil hitung sudut V{i+1} dengan V{j+1} = arc cos({ans:.2f} / ({pjgU:.2f}) * ({pjgV:.2f}))")
                print(f"    Hasil sudut (rad) = {resRad:.2f} rad")
                print(f"    Hasil sudut (Deg): {resDeg:.2f}\n")

def proyeksiOrthogonal(vectors):
    print("\n=== Kamu memilih operasi proyeksi orthogonal ===\n")
    print("Vektor input:\n")

    displayInput(vectors)

    print("=== Hasil proyeksi orthogonal ===\n")
    for i, Uvec in enumerate(vectors):
        for j, Vvec in enumerate(vectors[i+1:], start = i+1):
            U = Uvec
            V = Vvec
            print(f"Hasil proyeksi orthogonal V{j+1} pada vector V{i+1}:")
            proy(U, V)

            print("Sebaliknya:")
            print(f"Hasil proyeksi orthogonal V{i+1} pada vector V{j+1}:")
            proy(V, U)

def hitungJrkTtkKeGrs2d(points, equations):
    print("\n=== Kamu memilih operasi hitung jarak titik ke garis===\n")
    print("Persamaan garis input:\n")

    displayInput2(equations)
    print(f"Titik uji:\n")
    displayInput3(points)

    print("=== Hasil hitung jarak titik ke garis ===\n")
    for i, vpoint in enumerate(points):
        for j, vequation in enumerate(equations):
            pt = vpoint
            ptx = pt[0]
            pty = pt[1]

            eq = vequation
            ans = 0.0

            if len(eq) < 2:
                print(f"Persamaan E{j+1} tidak memiliki komponen C / konstanta, tidak dapat dihitung\n")
                return

            A = eq[0]
            B = eq[1] if len(eq) > 2 else 0.0
            C = eq[2] if len(eq) > 2 else eq[1]
            # pembilang = abs((ptx * eq[0]) + 
            #                 (pty * eq[1] if len(eq) > 2 else 0) +
            #                 (eq[2] if len(eq) > 2 else eq[1]))

            pembilang = abs((ptx * A) + (pty * B) + C)
            # penyebut = np.sqrt((pow(eq[0], 2)) + (pow(eq[1], 2) if len(eq) > 2 else 0))
            penyebut = np.sqrt(pow(A, 2) + pow(B, 2))

            ans = pembilang / penyebut

            # print(f"Jarak titik P{i+1} ke garis E{j+1} = abs({eq[0]:.2f} * {ptx:.2f} + {eq[1]:.2f if len(eq) > 2 else 0.00} * {pty:.2f} + {eq[2]:.2f if len(eq) > 2 else eq[1]:.2f})") ... this is error due to :.2f is not in expression

            print(f"Jarak titik P{i+1} ke garis E{j+1} = abs(({A:.2f} * {ptx:.2f}) + ({B:.2f} * {pty:.2f}) + ({C:.2f})) / sqrt(({A:.2f})^2 + ({B:.2f})^2)")

            print(f"Hasil jarak akhir = {ans:.2f}\n")

def dotProductRT(sum, sub):
    print("\n=== Kamu memilih operasi dot product r+t , r-t ===\n")

    print("r+t input:\n")
    displayInput4(sum)

    print("r-t input:\n")
    displayInput5(sub)

    if len(sum) != len(sub):
        print(f"Dapat dilihat bahwa banyak elemen tidak sama dimana len(r+t) = {len(sum)} sedangkan len(r-t) = {len(sub)}, tidak dapat dihitung r.t")

    print("=== Hasil hitung r dot t ===\n")
    for i in range(len(sum)):
        plus = sum[i]
        minus = sub[i]

        if len(plus) != len(minus):
            print(f"Dapat dilihat bahwa banyak elemen tidak sama dimana len(r+t) = {len(plus)} sedangkan len(r-t) = {len(minus)}, tidak dapat dihitung r.t")

        sqrPlus = pow(panjangVector(plus), 2) / 4
        sqrMin = pow(panjangVector(minus), 2) / 4

        ans = sqrPlus - sqrMin

        print(f"    Hasil r dot t [{i+1}] = 0.25(|{sqrPlus:.2f}|^2 - |{sqrMin:.2f}|^2)")
        print(f"    Hasil akhirnya = {ans:.2f}\n")



# main driver
opsi = 4

U = [1, 2, 3]
V = [4, 5, 6]
J = [7, 8, 9]
K = [10, 11, 12]
L = [13, 14, 15]

# D = [-3, 5, 12]
# E = [5, 7, -2]
# vectors = [D, E]

vectors = [U, V, J, K, L]

point1 = [1, 1]
point2 = [-5, 8]
E1 = [5, -4, 9]
E2 = [3, 4, -10]
equations = [E1, E2]
points = [point1, point2]

sm1 = [2, 3, 4]
sm2 = [4, 5, 6]
sm3 = [7, 8, 9]
sb1 = [9, 8, 7]
sb2 = [7, 5, 6]
sb3 = [5, 4, 2]

sum = [sm1, sm2, sm3]
sub = [sb1, sb2, sb3]

match opsi:
    case 1:
        dotProduct(vectors)
    case 2:
        proyeksiOrthogonal(vectors)
    case 3:
        hitungJrkTtkKeGrs2d(points, equations)
    case 4:
        dotProductRT(sum, sub)