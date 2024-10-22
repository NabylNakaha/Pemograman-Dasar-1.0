#Mengubah Variable Beserta Nilainya
nama_mahasiswa = "Nabyl"
umur_mahasiswa = 19
program_studi_mahasiswa = "Sistem Informasi"
jenis_kelamin_mahasiswa = "Laki-laki"
tinggi_mahasiswa = 170
kelas_mahasiswa = "SI-1A"
lulus = False

nama_mahasiswa = "Kevin"
umur_mahasiswa = 17
program_studi_mahasiswa = "Sistem Informasi"
jenis_kelamin_mahasiswa = "Laki-Laki"
tinggi_mahasiswa = 170
kelas_mahasiswa = "SI-1A"
lulus = True

#Menampilkan Output Variable
print("Nama:", nama_mahasiswa)
print("Umur:", umur_mahasiswa, "tahun")
print("Tinggi Badan: ", tinggi_mahasiswa, "cm") 
print("Program Studi:", program_studi_mahasiswa) 
print("Kelas:", kelas_mahasiswa)
print("Jenis Kelamin: ", jenis_kelamin_mahasiswa)

#Menampilkan Status Mahasiswa
if lulus == True:
    print("Status: Alumni")
else:
    print("Status: Mahasiswa aktif")
