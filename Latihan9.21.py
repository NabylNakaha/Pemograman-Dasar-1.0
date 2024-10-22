#Menginput Nilai Pada Tiap Variable Serta Mengubah Variable
nama_mahasiswa = input("Inputkan nama: ")
kelas_mahasiswa = input("Inputkan kelas: ") 
nim_mahasiswa = input("Inputkan NIM: ") 
alamat_mahasiswa = input("Inputkan alamat: ")
umur_mahasiswa = input("Inputkan umur: ")
nohp_mahasiswa = input("Inputkan nomor HP: ")
tinggi_mahasiswa = int(input("Inputkan tinggi badan (dalam cm): "))

#Menampilkan Output Variable
print(nama_mahasiswa, "dari kelas", kelas_mahasiswa, "dengan NIM", nim_mahasiswa) 
print("Beralamat di", alamat_mahasiswa, "berumur", umur_mahasiswa, "tahun dan tinggi badan", tinggi_mahasiswa, "cm")
print("Nomor HP:", nohp_mahasiswa) #Terdapat Error Di Variable  Line Ke-13 Karena Ada Simbol Underscore Setelah no
