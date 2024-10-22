#Program MenghitungBiayaAngkutan

#Masukan Nilai Variable Jarak
jarak_nabyl = int(input("Masukan Nilai Total jarak (KM): "))

#Menghitung Biaya Angkutan
harga_angkutan = (1 * 4500) + ((jarak_nabyl-1)* 2000)

#Menampilkan Total Biaya Angkutan
print ("Biaya Angkutan Anda Adalah: ", harga_angkutan)
