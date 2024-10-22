#Program Mencari Luas Dan Keliling Jajaran Genjang

a = alas_jgj = int(input("Masukan Nilai Alas: "))
t = tinggi_jgj = int(input("Masukan Nilai Tinggi: "))
b = bawah_jgj = int(input("Masukan Nilai Bawah: "))

#Rumus Menghitung Luas Dan Keliling Jajaran Genjang
luas_jgj = a * t
keliling_jgj = 2 * (a + b)

#Menampilkan Nilai Luas Dan Keliling Jajaran Genjang
print ("Nilai Luas Jajaran Genjang Adalah: ", luas_jgj)
print ("Nilai Keliling Jajaran Genjang Adalah: ", keliling_jgj)