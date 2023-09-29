#Login User 
print("--------------------")
print("--Login Kalkulator--")
print("--------------------")
nama = input("Nama Anda : ") #input nama user
nim  = input("Nim Anda  : ") #input nim user

#Tampilan setelah login
print()
print(f"Selamat Datang {nama} di projek kalkulator sederhana!")
print()

#Kalkulator serta kode inputan
print("----Kalkulator----")
print("--1. Penjumlahan--")
print("--2. Pengurangan--")
print("--3. Perkalian----")
print("--4. Pembagian----")
print("--5. Modulus------")
print()

angka1     = int(input("Masukkan angka pertama   : ")) #inputkan angka pertama
angka2     = int(input("Masukkan angka kedua     : ")) #inputkan angka kedua
kalkulator = int(input("Pilih Kalkulator 1/2/3/4/5 : ")) #input kode kalkulator
print()

#proses percabangan dan kalkulasi
if kalkulator == 1 : #jika kede 1 dipanggil
    penjumlahan = angka1 + angka2 #dijumlah angka pertama dengan kedua
    print(f"{angka1} + {angka2} = {penjumlahan}") #menunjukkan hasil penjumlahan
elif kalkulator == 2: #jika kode 2 dipanggil
    pengurangan = angka1 - angka2 #dikurang angka pertama dan kedua
    print(f"{angka1} - {angka2} = {pengurangan}") #menunjukan hasil pengurangan
elif kalkulator == 3: #jika kode 3 dipanggil
    pengalian = angka1 * angka2 #dikali angka pertama dan kedua
    print(f"{angka1} * {angka2} = {pengalian}") #menunjukkan hasil perkalian
elif kalkulator == 4: #jika kode 4 dipanggil
     pembagian = angka1/angka2 #dibagi angka pertama dan kedua
     print(f"{angka1} / {angka2} = {pembagian}") #menunjukkan hasil pembagian
else: #jika kode selain 1,2,3,4 dipanggil maka
    modulus = angka1 % angka2 #dimodus angka pertama dan kedua
    print(f"{angka1} % {angka2} = {modulus}") #menunjukkan hasil modulus



