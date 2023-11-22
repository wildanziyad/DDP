
#materi list

profilekendaraan=["aerox","matic","160","hitamdoff","2"]
profilekendaraan.append("30juta")
profilekendaraan.append("matic")
profilekendaraan.insert(2,"merkkendaraan")
print(profilekendaraan[1])


print()

#materi matchcase

soal = int(input ("menghitung luas bangun datar (pilih dari 1-3):"))
match soal:
    case 1:
     print("menghitung ilmu persegi")
     sisipersegi = int(input("masukan sisi :"))
     luaspersegi = sisipersegi * sisipersegi
     print("luas persegi =",luaspersegi)

    case 2 :
      print("menghitung luas lingkaran\n")
      jariJarilingkaran=int(input("masukan jari-jari lingkaran"))
      luaslingkaran=(3.14 * jariJarilingkaran * jariJarilingkaran )
      print("luas lingkaran =", float(luaslingkaran))

    case 3 :
        print("Menghitung luas segitiga")
        alassegeitiga =int(input("Masukan Alas segetiga :"))
        tinggisegitiga = int(input("Masukan Tinggi Segitiga :"))
        luassegitiga = 1/2 * alassegeitiga * tinggisegitiga
        print("luas segitiga =" , int(luassegitiga)) 
