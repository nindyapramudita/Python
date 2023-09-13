#Rumus

def equal(x,y): #ini equal
    return x == y

def NotEqual(x,y): #ini not equal
    return x != y

def Gthan(x,y):  #ini Greater than
    return x > y

def Lthan(x,y): #ini Less than
    return x < y

def Gthanoequal(x,y): #ini Greater than or equal to
    return x >= y
def Lthanoequal(x,y): #ini Less than or equal to
    return x <= y

#Output
print("Hasilnya adalah = ", Lthanoequal(10,3))  #hasilnya Falsa jika salah dan true jika benar 
print("Hasilnya adalah = ", Gthanoequal(8,3))  #hasilnya Falsa jika salah dan true jika benar 
print("Hasilnya adalah = ", Lthan(8,3))  #hasilnya Falsa jika salah dan true jika benar 
print("Hasilnya adalah = ", Gthan(8,3))  #hasilnya Falsa jika salah dan true jika benar 
print("Hasilnya adalah = ", NotEqual(8,3))  #hasilnya Falsa jika salah dan true jika benar
print("Hasilnya Adalah = ", equal(8,8)) #hasilnya Falsa jika salah dan true jika benar
