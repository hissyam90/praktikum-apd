# # # # # # praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# # # # # # print(praktikum[4][0])

# # # # # # # list awal
# # # # # # studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # # # # # # Tambahkan Web
# # # # # # studyclub[2] = "Web"
# # # # # # print(studyclub)

# # # # # # # list awal
# # # # # # matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# # # # # # print(matakuliah)
# # # # # # # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# # # # # # # matakuliah.remove("Kalkulus")
# # # # # # # print(matakuliah)
# # # # # # del matakuliah[0:]
# # # # # # print(matakuliah)

# # # # # # list awal
# # # # # # matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# # # # # # print(matakuliah)
# # # # # # # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# # # # # # ambil_matkul = matakuliah.pop(2)
# # # # # # print(matakuliah)
# # # # # # print(ambil_matkul)

# # # # # # list
# # # # # matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# # # # # 'Orsikom','Basis Data']
# # # # # # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# # # # # print(matakuliah[1:6:2])
# # # # # # start stop step  
 
# # # # # List
# # # # a = [1, 2, 3]
# # # # b = [4, 5, 6]
# # # # # menggabungkan kedua list dengan operator (+)
# # # # c = a + b
# # # # print(c)

# # # # List
# # # a = ["teknik", "informatika"]
# # # # mengulang isi list dengan operator (*) sebanyak 3 kali
# # # c = a*3
# # # print(c)

# # kelas = [
# # ["Ridho", "Lian", "Nabil"],
# # ["Daffa", "Dante", "Santoso"],
# # ["Pernanda", "Riyadi", "Ahnaf"],
# # ]

# # print(kelas[1][2], [2][2])

# # list mahasiswa
# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     for j in i :
#         print (j)

anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
anggota[0] = "ahnaf"
print(anggota)