import sys
import timeit

# List [] bisa diganti isinya
Hewan = ["kelinci","beruang","gajah"]

# Tuple () tidak bisa diganti isinya hanya bisa di count dan index
Tanaman = ("mawar","melati","anggrek")

print (type(Hewan))
print (type(Tanaman))
print ()

print (Hewan[0]) #cara memanggil satu dari beberapa anggota data list dan tuple
print()

# Contoh pembuktian
Hewan[2] = "kucing" #mencoba mengganti index ke 2 
print(Hewan)
Tanaman[1] = "lavender"
print(Tanaman) #akan terjadi eror karena kita tidak bisa mengganti isi tuple itu sendiri
print()


# # # Keterangan: Data tuple lebih kecil dibandingkan data list.
# data_list = ["Nindya","makan","pisang goreng",1,2,3,4,5,"biji", False, 3.14]
# data_tuple = ("Nindya","makan","pisang goreng",1,2,3,4,5,"biji", False, 3.14)

# besar_datalist = sys.getsizeof(data_list)
# besar_datatuple = sys.getsizeof(data_tuple)

# print("Besar data list: ",besar_datalist)
# print("Besar data tuple: ",besar_datatuple)
# print()

# #Keterangan: Pembuktian waktu memproses List dan Tuple
# data_listt = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]",number=1000000)
# data_tuplee = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,10)",number=1000000)

# print("Waktu untuk memproses list : ",data_listt)
# print("Waktu untuk memproses tuple: ",data_tuplee)