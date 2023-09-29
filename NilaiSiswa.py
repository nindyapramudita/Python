#Table Nilai
print("-----------------------")
print("----Nilai Mahasiswa----")
print("-----------------------")
print("---A  = Nilai > 85-----")
print("---A- = Nilai 80-85----")
print("---B+ = Nilai 75-79----")
print("---B  = Nilai 70-74----")
print("---B- = Nila1 65-69----")
print("---C+ = Nilai 60-64----")
print("---C  = Nilai 55-59----")
print("---C- = Nilai 50-54----")
print("---D  = Nilai 40-49----")
print("---E  = Nilai < 40-----")
print()

nama  = str(input("Nama Mahasiswa : ")) #input nama mahasiswa
nim   = int(input("Nim Mahasiswa  : ")) #input nim siswa
print()
nilai = float(input("Masukkan Nilai : ")) #input nilai siswa
print()

if nilai > 85: #jika nilainya di atas 85
    print(f"Selamat {nama} - {nim}") #ouput nilai A
    print(f"Nilai anda A atau {nilai}")
    print("Semangat dan terus belajar!")
elif (nilai >= 80) and (nilai <= 85) : #jika nilainya di bawah atau sama dengan 85 dan diatas 80
    print(f"Selamat {nama} - {nim}")
    print(f"Nilai anda A- atau {nilai}")
    print("Semangat dan terus belajar!")
elif (nilai >= 75) and (nilai <= 79) :#jika nilainya di bawah atau sama dengan 79 dan diatas 75
    print(f"Selamat {nama} - {nim}")
    print(f"Nilai anda B+ atau {nilai}")
    print("Semangat dan terus belajar!")
elif (nilai >= 70) and (nilai <= 74) :#jika nilainya di bawah atau sama dengan 74 dan diatas 70
    print(f"Selamat {nama} - {nim}")
    print(f"Nilai anda B atau {nilai}")
    print("Semangat dan terus belajar!")
elif (nilai >= 65) and (nilai <= 69) :#jika nilainya di bawah atau sama dengan 69 dan diatas 65
    print(f"Mohon maaf {nama} - {nim}")
    print(f"Nilai anda B- atau {nilai}")
    print("Belajar lagi dan pahami materi!")
elif (nilai >= 60) and (nilai <= 64) :#jika nilainya di bawah atau sama dengan 64 dan diatas 60
    print(f"Mohon maaf {nama} - {nim}")
    print(f"Nilai anda C+ atau {nilai}")
    print("Belajar lagi dan pahami materi!")
elif (nilai >= 55) and (nilai <= 59) :#jika nilainya di bawah atau sama dengan 59 dan diatas 55
    print(f"Mohon maaf {nama} - {nim}")
    print(f"Nilai anda C atau {nilai}")
    print("Belajar lagi dan pahami materi!")
elif (nilai >= 50) and (nilai <= 54) :#jika nilainya di bawah atau sama dengan 54 dan diatas 50
    print(f"Mohon maaf {nama} - {nim}")
    print(f"Nilai anda C- atau {nilai}")
    print("Belajar lagi dan pahami materi!")
elif (nilai >= 40) and (nilai <= 49) :#jika nilainya di bawah atau sama dengan 49 dan diatas 40
    print(f"Mohon maaf {nama} - {nim}")
    print(f"Nilai anda D atau {nilai}")
    print("Belajar lagi dan pahami materi!")
elif nilai < 40 :#jika nilainya dibawah 40
    print(f"Mohon maaf {nama} - {nim}")
    print(f"Nilai anda E atau {nilai}")
    print("Belajar lagi dan pahami materi!")
else: #jika nilai yang diinputkan tidak terdaftar
    print("Error")
