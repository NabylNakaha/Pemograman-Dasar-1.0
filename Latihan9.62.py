#Program MenghitungGajiBersih

#Masukan Nilai Variable Gaji Pokok
gaji_pokok_nabyl = int(input("Masukan Nilai Total Gaji Pokok: "))

#Nilai Pajak Dan Tunjangan
pajak_nabyl = 0.1 #Total Pajak Gaji Anda Sebesar 10%
tunjangan_nabyl = 0.2 #Total Tunjangan Anda Sebesar 20%

#Rumus Untuk Menghitung Gaji Bersih
detail_pajak_nabyl = gaji_pokok_nabyl * pajak_nabyl
detail_tunjangan_nabyl = gaji_pokok_nabyl * tunjangan_nabyl
gaji_bersih_nabyl = gaji_pokok_nabyl + detail_tunjangan_nabyl - detail_pajak_nabyl

#Menampilkan Total Gaji Pokok, Pajak, Tunjangan, Dan Gaji Bersih 
print ("Total Gaji Pokok Anda Adalah: ", gaji_pokok_nabyl)
print ("Total Pajak Anda Adalah: ", detail_pajak_nabyl)
print ("Total Tunjangan Anda Adalah: ", detail_tunjangan_nabyl)
print ("Total Gaji Bersih Anda Adalah: ", gaji_bersih_nabyl)