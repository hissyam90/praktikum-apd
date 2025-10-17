# # # # # # # Membuat set 
# # # # # # buah = {"apel", "jeruk", "mangga", "apel", 21311, (123)}  
# # # # # # print(buah) 

# # # # # # angka_ganjil = {1, 3, 5, 7, 9} 
# # # # # # for angka in angka_ganjil: 
# # # # # #     print(angka)
    

# # # # # # angka_ganjil.add(11)
# # # # # # print(angka_ganjil)

# # # # # # angka_ganjil.remove(3)
# # # # # # print(angka_ganjil)

# # # # # # angka_ganjil.discard(11)  

# # # # # # Daftar_buku = { 
# # # # # # "Buku1" : "Bumi Manusia", 
# # # # # # "Buku2" : "Laut Bercerita" 
# # # # # # }

# # # # # # # # print(Daftar_buku["Buku2"]) 
# # # # # # # # print(Daftar_buku) 

# # # # # # for dawdaw in Daftar_buku.items(): 
# # # # # #     print(dawdaw)
# # # # # # for a in dawdaw.values(): 
# # # # # #     print(a)

# # # # # # Biodata = { 
# # # # # #     "Nama" : "Antung Hissyam", 
# # # # # #     "NIM" : 2509106092, 
# # # # # #     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Jaringan Komputer", "Sistem Operasi"], 
# # # # # #     "Mahasiswa_Aktif" : True, 
# # # # # #     "Social Media" : {        
# # # # # #         "Instagram" : "keisoiyam" 
# # # # # #       } 
# # # # # # }

# # # # # # # print(f"nama saya adalah {Biodata["Nama"]}") 
# # # # # # # print(f"Instagram : {Biodata['Social Media']['Instagram']}") 
 
# # # # # # print(f"nama saya adalah {Biodata.get("Nama")}") 
# # # # # # print(f"{Biodata['mashashdwada']}")
# # # # # # print(Biodata.get("Nama")) 
# # # # # # print(Biodata.get("Alamat")) 
# # # # # # print(Biodata.get("Alamat", "Key tersebut tidak ada")) 
# # # # # # print(Biodata.get("Nama"))

# # # # # # print(f"{Biodata['KRS'][1:4:2]}") 

# # # # # # list_nama= dict(mahasiswa1="Daffa Santoso", mahasiswa2="bambang", mahasiswa3="ucup", mahasiswa4="otong")
# # # # # # print(list_nama)

# # # # # Film = { 
# # # # #     "Avenger Endgame" : "Action", 
# # # # #     "Sherlock Holmes" : "Mystery", 
# # # # #     "The Conjuring" : "Horror"
# # # # # } 
# # # # # #Sebelum Ditambah 
# # # # # print(Film) 
 
# # # # # Film["Zombieland"] = "Comedy" 
# # # # # Film.update({"Hours" : "Thriller"}) 
# # # # # #Setelah Ditambah 
# # # # # print(Film) 
 
# # # # # #Sebelum Ditambah 
# # # # # {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# # # # # 'The Conjuring': 'Horror'} 
 
# # # # # #Setelah Ditambah 
# # # # # {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# # # # # 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours': 
# # # # # 'Thriller'} 

# # # # data = { 
# # # # "Nama" : "Daffa", 
# # # # "Umur" : 19, 
# # # # "Jurusan" : "Informatika" 
# # # # } 
# # # # #Sebelum Dihapus 
# # # # print(data) 
 
# # # # del data["Nama"] 
 
# # # # #Setelah diubah
# # # # print(data)

# # # # #memanggil data yang telah dihapus 
# # # # print(data.get("Nama")) 
 
# # # # {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
 
# # # # {'Umur': 19, 'Jurusan': 'Informatika'} 
 
# # # # None 

# # # data = { 
# # # "Nama" : "Daffa", 
# # # "Umur" : 19, 
# # # "Jurusan" : "Informatika" 
# # # } 
 
# # # #Sebelum Dihapus 
# # # print(data) 
 
# # # cache = data.pop("Nama") 
 
# # # #Setelah dihapus 
# # # print(data) 
 
# # # #memanggil data yang telah dihapus pada dictionary 
# # # print(data.get("Nama")) 
 
# # # #memanggil data yang telah dihapus pada variabel cache 
# # # print(cache) 
 
# # # {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
# # # {'Umur': 19, 'Jurusan': 'Informatika'} 

# # data = { 
# #     "Nama" : "Daffa", 
# #     "Umur" : 19, 
# #     "Jurusan" : "Informatika" 
# # }
# # print("Jumlah Data = ", len(data)) 

# buku = { 
#  "Buku1" : "Bumi Manusia", 
#  "Buku2" : "Laut Bercerita" 
# } 
 
# pinjam = buku.copy() 
# pinjam['buku2'] = "Anak Semua Bangsa"
# print("Dictionary yang telah disalin : ", pinjam) 
# print(buku)

Musik = { 
"The Chainsmoker" : ["All we Know", "The Paris"], 
"Alan Walker" : ["Alone", "Lily"], 
"Neffex" : ["Best of Me", "Memories"] 
} 
 
for penyanyi, album in Musik.items(): 
 print(f"Musik milik {penyanyi} adalah : ") 
 for song in album: 
  print(song) 
 print("") 
 
