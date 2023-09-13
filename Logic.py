#Rumus

def AND(x,y,z): #ini logika AND
    return x < y and  x < Z

def OR(x,y,z): #ini logika OR
    return x < y or x < z

def NOT(x,y,z):  #ini logika NOT
    return not(x < y and x < z)

#Output
print("Hasilnya adalah = ", AND(10,3,11))  #hasilnya Falsa jika salah dan true jika benar 
print("Hasilnya adalah = ", OR(8,3,4))  #hasilnya Falsa jika salah dan true jika benar 
print("Hasilnya adalah = ", NOT(20,3,15))  #hasilnya Falsa jika salah dan true jika benar 