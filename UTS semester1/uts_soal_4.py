def hitung_luas_layang_layang(d1, d2):
    luas = (d1 * d2) / 2
    return luas

def hitung_keliling_layang_layang(d1, d2):
    sisi1 = d1 / 2
    sisi2 = d2 / 2
    keliling = 2 * (sisi1 + sisi2)
    return keliling

diagonal1 = float(input("Masukkan panjang diagonal 1: "))
diagonal2 = float(input("Masukkan panjang diagonal 2: "))
luas_layang_layang = hitung_luas_layang_layang(diagonal1, diagonal2)
keliling_layang_layang = hitung_keliling_layang_layang(diagonal1, diagonal2)

print("Luas layang-layang: {:.2f}".format(luas_layang_layang))
print("Keliling layang-layang: {:.2f}".format(keliling_layang_layang))