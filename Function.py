# Cara mendefinisikan Fungsi
def fungsi(): #harus menggunakan def
  print('Ini Fungsi')

# Cara memanggil fungsi
fungsi() #tidak perlu menggunakan print
print()

# implementasi fungsi sederhana "Laundry"
def laundry(): #nama yang dipanggil
  print('Selamat datang di Laundry Nindya')
  print(' Spesialis Laundry Baju Terbaik ')
  print('================================')

def kilo(kg):
  laundry()#memanggil
  harga = 6000
  total = harga * kg
  print('Harga ',kg,"kilogram baju= Rp.",total)

kilo(7)#memanggil dan menginputkan nilai kilogram
print()
kilo(10)
print()
kilo(4)