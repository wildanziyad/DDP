#quiz no 1 cuyy


nama_kendaraan = input("Nama Kendaraan (contoh: mobil, motor): ")
jenis_bensin = input("Jenis Bensin (Pertalite/Pertamax/Pertamax Turbo): ")
kota_tujuan = input("Kota Tujuan: ")


jarak_tempuh = 0
harga_per_liter = 0
total_harga = 0

if jenis_bensin == "Pertalite":
    harga_per_liter = 10000
    jarak_tempuh = 12
elif jenis_bensin == "Pertamax":
    harga_per_liter = 14000
    jarak_tempuh = 13
elif jenis_bensin == "Pertamax Turbo":
    harga_per_liter = 17000
    jarak_tempuh = 13.5


if kota_tujuan == "Jakarta":
    jarak_kota = 20
elif kota_tujuan == "Bekasi":
    jarak_kota = 35.7
elif kota_tujuan == "Depok":
    jarak_kota = 5
elif kota_tujuan == "Tangerang":
    jarak_kota = 99
elif kota_tujuan == "Bogor":
    jarak_kota = 120.6


pemakaian_bensin = jarak_kota / jarak_tempuh
total_harga = pemakaian_bensin * harga_per_liter
print("\nRincian Perjalanan:")
print(f"Nama Kendaraan: {nama_kendaraan}")
print(f"Jenis Bensin: {jenis_bensin}")
print(f"Kota Tujuan: {kota_tujuan}")
print(f"Pemakaian Bensin: {pemakaian_bensin:.2f} liter")
print(f"Total Biaya: Rp {total_harga:.2f}")

print("==========================================================================")


print()

#nomor 2

#input
nama_pembeli=input("Nama Pembeli :")
no_hp_pembeli=input("no hp pembeli :")
pesan_menu=input("Pesan Menu Apa? (makanan atau minuman) : ")

#variable 
harga_menu = 0
jumlah_pesenan=0
harga_total=0

#memproses makanan
if pesan_menu == "makanan":
    print("Menu Makanan:")
    print("1. Nasi Goreng (Rp. 15.000)")
    print("2. Mie Goreng (Rp. 12.000)")
    print("3. Ayam Geprek (Rp. 18.000)")
    menu_makanan = input("Masukkan pesanan makanan: ")
    if menu_makanan == "1":
        harga_menu = 15000
    elif menu_makanan == "2":
        harga_menu = 12000
    elif menu_makanan == "3":
        harga_menu = 18000

#memproses minumanan
elif pesan_menu == "minuman":
    print("Menu Minuman:")
    print("1. Aneka Jus (Rp. 15.000)")
    print("2. Soft Drink (Rp. 10.000)")
    print("3. Sweet Ice Tea (Rp. 5.000)")
    menu_minuman = input("Masukkan pesanan minuman: ")
    if menu_minuman == "1":
        harga_menu = 15000
    elif menu_minuman == "2":
        harga_menu = 10000
    elif menu_minuman == "3":
        harga_menu = 5000

# Input jumlah pesanan
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

# Menghitung harga total
harga_total = harga_menu * jumlah_pesanan

# Output
print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", menu_makanan if pesan_menu == "makanan" else menu_minuman)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus dibayarkan:", harga_total)


print()
print("==========================================================================")

#nomor3
for i in range (1, 21):
    if i % 3 == 0:
        print("STT TERPADU Nurul Fikri")
    print(i)