def kalkulator(angka1, angka2, operator):
    if operator == '+':
        hasil = angka1 + angka2
        keterangan = 'Tambah'
    elif operator == '-':
        hasil = angka1 - angka2
        keterangan = 'Kurang'
    elif operator == '*':
        hasil = angka1 * angka2
        keterangan = 'Kali'
    elif operator == '/':
        if angka2 != 0:
            hasil = angka1 / angka2
            keterangan = 'Bagi'
        else:
            return "Error: Pembagian dengan angka 0 tidak valid."
    elif operator == '**':
        hasil = angka1 ** angka2
        keterangan = 'Pangkat'
    else:
        return "Error: Operator tidak valid."

    return f"Hasil {keterangan} {angka1} {operator} {angka2} = {hasil}"

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Pilih operator (+, -, *, /, **): ")
output = kalkulator(angka1, angka2, operator)

print("Angka pertama:", angka1)
print("Angka kedua:", angka2)
print("Pilihan Operator:", operator)
print(output)