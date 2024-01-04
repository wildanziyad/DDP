import tkinter as tk

def konvert_suhu():
    
    try:
        from_unit = var_dropdown_isi1.get()
        inputan_dalam = float(inputan.get())
    
        if from_unit == 'Celsius':
            hasil_c = inputan_dalam
            hasil_f = (9/5*inputan_dalam)  + 32
            hasil_k = inputan_dalam + 273.15
            hasil_re = inputan_dalam * 4/5
            hasil_ra = (inputan_dalam + 273.15) * 9/5
            hasil = f"{hasil_f:.2f} farenheit \n\n{hasil_k:.2f} kelvin \n\n{hasil_re:.2f} reamure \n\n{hasil_ra:.2f} rankin \n\n{hasil_c:.2f} celcius"
            result_label.config(text=hasil)
            
        elif from_unit == 'Fahrenheit':
            hasil_c = (inputan_dalam-32)*5/9
            hasil_f = inputan_dalam
            hasil_k = (inputan_dalam + 459.67)*5/9
            hasil_re = (inputan_dalam-32) * 4/9
            hasil_ra = inputan_dalam+459.67
            hasil = f"{hasil_f:.2f} farenheit \n\n{hasil_k:.2f} kelvin \n\n{hasil_re:.2f} reamure \n\n{hasil_ra:.2f} rankin \n\n{hasil_c:.2f} celcius"
            result_label.config(text=hasil)
            
        elif from_unit == 'Kelvin':
            hasil_c = inputan_dalam - 273.15
            hasil_f = (inputan_dalam*9/5)-459.67
            hasil_k = inputan_dalam
            hasil_re = 4/5*(inputan_dalam-273)
            hasil_ra = inputan_dalam*9/5
            hasil = f"{hasil_f:.2f} farenheit \n\n{hasil_k:.2f} kelvin \n\n{hasil_re:.2f} reamure \n\n{hasil_ra:.2f} rankin \n\n{hasil_c:.2f} celcius"
            result_label.config(text=hasil)
            
        elif from_unit == 'Reamur':
            hasil_c = inputan_dalam /0.8
            hasil_f = inputan_dalam*2.25+32
            hasil_k = inputan_dalam/0.8+273.15
            hasil_re = inputan_dalam
            hasil_ra = inputan_dalam*2.25+491.67
            hasil = f"{hasil_f:.2f} farenheit \n\n{hasil_k:.2f} kelvin \n\n{hasil_re:.2f} reamure \n\n{hasil_ra:.2f} rankin \n\n{hasil_c:.2f} celcius"
            result_label.config(text=hasil)
            
        elif from_unit == 'Rankine':
            hasil_c = (inputan_dalam-491.67)*5/9
            hasil_f = inputan_dalam-459.67
            hasil_k = inputan_dalam*5/9
            hasil_re = (inputan_dalam-491.67)*4/9
            hasil_ra = inputan_dalam
            hasil = f"{hasil_f:.2f} farenheit \n\n{hasil_k:.2f} kelvin \n\n{hasil_re:.2f} reamure \n\n{hasil_ra:.2f} rankin \n\n{hasil_c:.2f} celcius"
            result_label.config(text=hasil)
    except ValueError:
        result_label.config(text="Error, tolong masukkan angka !")
        
# Membuat wadah tk
wadah_tk = tk.Tk()

# Membuat judul wadah
wadah_tk.title("Konverter Suhu Celsius | Fahrenheit | Kelvin | Reamur | Rankine")

# label suhu
label_temp = tk.Label(wadah_tk, text="Suhu :")
label_temp.grid(row=0, column=0, padx=10, pady=10)

# Input suhu
inputan = tk.Entry(wadah_tk)
inputan.grid(row=0, column=1, padx=10, pady=10)


# List untuk dropdown menu suhu 
list_dropdown = ['Celsius', 'Fahrenheit', 'Kelvin', 'Reamur',"Rankine"]

# Mengatur variabel kontrol string untuk parameter optionmenu
var_dropdown_isi1 = tk.StringVar(wadah_tk)

# Mengatur tampilan awal yaitu Celsius ke Fahrenheit
var_dropdown_isi1.set(list_dropdown[0])

# Membuat opsi menu dengan parameter
opsi_menu1 = tk.OptionMenu(wadah_tk, var_dropdown_isi1, *list_dropdown)

# Mengatur posisi list dropdown menu 1 dan 2
opsi_menu1.grid(row=0, column=2, padx=10, pady=5)

# Membuat label untuk menampilkan hasil konversi
result_label = tk.Label(wadah_tk, text="")
result_label.grid(row=2, column=1, pady=10)

# Membuat tombol untuk mengonversi suhu
button_konvert = tk.Button(wadah_tk, text="Konversi suhu", command=konvert_suhu)
button_konvert.grid(row=3, column=1, pady=10)

# Menjalankan aplikasi
wadah_tk.mainloop()