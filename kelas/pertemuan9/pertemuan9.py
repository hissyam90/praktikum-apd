import pandas as pd
import numpy as np

# # # data awal string
# # data_awal = """NIM,Nama,Angkatan
# # 23001,Budi Santoso,2023
# # 23002,Ani Wijaya,2023
# # 23003,Citra Lestari,2023
# # 23004,Doni Firmansyah,2023
# # """

# # try:
# #     with open("mahasiswa.csv", "w") as f:
# #         f.write(data_awal) #khusus string
# #     print("File 'mahasiswa.csv' berhasil dibuat!")
# # except Exception as e:
# #     print(f"Gagal membuat file: {e}")

# dataAwal = {
#     'NIM': [2409106046],
#     'Nama': ['st'],
#     'Angkatan': ['2024']
# }

# # try:
# #     df = pd.DataFrame(dataAwal) #ubah dictionary menjadi dataframe
    
# #     df.to_csv("mahasiswa2.csv", index=False)# index=False penting agar nomor index (0) tidak ikut disimpan
# #     print("File 'mahasiswa2.csv' berhasil dibuat dengan data!")

# # except Exception as e:
# #     print(f"Gagal membuat file: {e}")

# # Untuk membaca file csv dan menyimpannya ke dataframe (df)
# df = pd.read_csv("mahasiswa.csv")
# # # print(df)
# # # print(df.head()) #menampilkan 5 teratas, jika menulis df.head(3) berarti menampilkan 3 teratas
# # # print(df.tail()) #menampilkan 5 terbawah, jika menulis df.tail(3) berarti menampilkan 3 terbawah
# # # print(df.info()) #buat ngeliat informasi ringkas

# # # # Data Sebelum di update
# # # print("Data Sebelum di Update")
# # # print(df.head())

# # # # mengubah pada index 1 di kolom "nama"
# # # df.loc[1, 'Nama'] = 'Maria'

# # # # Tampilkan data setelah diubah
# # # print("\nData Setelah di Update")
# # # print(df.head())

# # carIndex = df[df['Nama'] == "Citra Lestari"].index
# # df.loc[carIndex, 'Angkatan']  = 2019
# # print(df)

# # dataDF = pd.read_csv('mahasiswa.csv')

# # nim = int(input('NIM yang ingin di input'))
# # nama = input('Nama yang ingin di input')
# # angkatan = int(input('Angkatan yang ingin di input'))

# # dataBaru = pd.DataFrame({'NIM': [nim], 'Nama': [nama], 'Angkatan': [angkatan]})
# # dataDF = pd.concat([dataDF, dataBaru], ignore_index=True)
# # print(dataDF)
# # dataDF.to_csv('mahasiswa.csv', index=False)

# dataBaru = {
# 'NIM': [23005],
# 'Nama': ['budi Putra'],
# 'Angkatan': [2023]
# }

# # ubah dictionary ke dataframe
# df_baru = pd.DataFrame(dataBaru)

# # 3.gabung dataframe lama dengan dataframe baru
# df = pd.concat([df, df_baru], ignore_index=True)

# print("\nData setelah ditambah Eka Putra:")
# print(df)
# df.to_csv('mahasiswa.csv', index=False)

# #Buat nama kolom baru dan beri nilainya
# df['Asal'] = 'Samarinda'

# print("Data setelah ditambah kolom 'Asal':")
# print(df)

# # Menghapus baris berdasarkan index-nya
# # inplace=True berarti kita memodifikasi df secara langsung
# print(df)
# df.drop(index=1, inplace=True) #cara 1
# df = df.drop(index=1) #cara 2

# print("\nData setelah menghapus Citra (index 2):")
# print(df)

# # Menghapus kolom 'Asal'
# # axis=1 memberitahu pandas bahwa kita mau menghapus KOLOM
# print(df)
# df.drop('Asal', axis=1, inplace=True)

# print("\nData setelah menghapus kolom 'Asal':")
# print(df)

# kondisi = df['Nama'] != 'Ekas Putra'
# dfBaru = df[kondisi]
# print(dfBaru)

# df_baru = df.reset_index(drop=True) #jika false dia membuat index baru
# print(df_baru)

# data = {'NIM': [19001, 23001], 'Nama': ['Citra', 'Budi'], 'Angkatan': [2019, 2023]}
# df_benar = pd.DataFrame(data)
# print("--- Data Awal ---")
# print(df_benar)

# for index, row in df_benar.iterrows():
#     if row['Angkatan'] < 2020:
#         # Gunakan .loc[index, 'NamaKolomBaru'] untuk mengubah DataFrame ASLI
#         df_benar.loc[index, 'Status'] = 'Alumni'
#     else:
#         df_benar.loc[index, 'Status'] = 'Mahasiswa Aktif'

# print("\n--- Hasil yang Benar (Data Berubah) ---")
# print(df_benar)

url = 'https://raw.githubusercontent.com/orkvacy/dummy-data/refs/heads/main/dummyData.csv'
df = pd.read_csv(url)

# print(df.head(5))
df.isna().sum()