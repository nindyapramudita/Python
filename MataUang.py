# Nindya Pramudita-2309116053

#LOGIN
a = ('Login Dahulu!!!')
print(a)
print()
nama = str(input("Masukkan Nama Anda: "))
nim = int(input ("Masukkan Nim Anda : "))
kelas = input ("Masukkan kelas anda: ")
print()

# Konfersi mata uang Rupiah ke mata uang asing
print("Selamat Datang",nama,"di Konfersi Mata Uang Rupiah")
print("1. Rupiah-Dollar===========================")
print("2. Rupiah-Ringgit==========================")
print("3. Rupiah-Yen==============================")
print("===========================================")

#inputan pengguna/user
a = int(input("Masukkan jumlah uang anda: "))
b = str(input("Masukkan konfersi uang ke: "))

#proses konversi rupiah mata uang asing
dollar = a/15375
ringgit = a/3273,38
yen = a / 103,57

if b == "dollar": # proses jika inputan yang diminta adalah dollar
 print("IDR =Rp. ",a)
 print("USD =$ ",dollar)
 print()
elif b == "ringgit": # proses jika inputan yang diminta adalah ringgit
  print("IDR =Rp. ",a)
  print("MYR =RM ",ringgit)
  print()
elif b == "yen":  # proses jika inputan yang diminta adalah yen
  print("IDR =Rp. ",a)
  print("JPY =Yen ",yen)
  print()
else:  # proses jika inputan yang diminta tidak ada
   print("Konversi mata uang ",b ,"tidak ada!")
   print()
  


# Konversi mata uang asing ke asing
print("Selamat Datang",nama,"di Konfersi Mata Uang Asing")
print("1. Dollar-Ringgit==========================")
print("2. Ringgit-Dollar==========================")
print("3. Dollar-Yen==============================")
print("4. Yen-Dollar==============================")
print("5. Ringgit-Yen=============================")
print("6. Yen-Ringgit=============================")
print("===========================================")

# function konversi data
def konver_uang(uang, asal, tujuan):
    nilai_tukar = {
        'USD_MYR': 4.69,  # Nilai tukar Dolar ke Ringgit Malaysia
        'MYR_USD': 0.21,  # Nilai tukar Ringgit Malaysia ke Dolar
        'USD_JPY': 148.28,  # Nilai tukar Dolar ke Yen Jepang
        'JPY_USD': 0.0067,  # Nilai tukar Yen Jepang ke Dolar
        'MYR_JPY': 31.79,  # Nilai tukar Ringgit Malaysia ke Yen Jepang
        'JPY_MYR': 0.031,  # Nilai tukar Yen Jepang ke Ringgit Malaysia
    }

    if asal == tujuan:
        return uang  # disini ketika mata uang yang dimasukkan sama maka tidak akan dihitung. dikembalikan ke nominal awal

    konversi = uang * nilai_tukar.get(f'{asal}_{tujuan}', None) #mendefinisikan bagian function nilai tukar

    if konversi is not None:
        return konversi
    
    else: #jika inputan yang dimasukkan tidak ada pada pilihan maka akan menunjukkan output tersebut
        return 'Nilai tukar tidak tersedia' 

# Inputan pengguna/user
uang = float(input('Masukkan jumlah uang: '))
asal = input('Mata uang asal (USD/MYR/JPY): ').upper()
tujuan = input('Mata uang tujuan (USD/MYR/JPY): ').upper()
print("----------------------")


# Melakukan konversi serta mencetak hasilnya
hasil_konversi = konver_uang(uang, asal, tujuan)
if type(hasil_konversi) == float: #dalam bentuk tipe data float
    print(f'{uang} {asal} = {hasil_konversi} {tujuan}') #output hasil konversi
else:
    print(hasil_konversi)
