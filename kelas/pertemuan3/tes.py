# angka = int(input("Masukkan sebuah angka: "))

# if angka > 5:
#     print("Angka lebih besar dari 5")
# else:
#     print("Angka tidak lebih besar dari 5")

# nilai = int(input("Masukkan nilai Anda: "))

# if nilai >= 80:
#     print("nilai A")
# elif nilai >= 70:
#     print("nilai B")
# elif nilai >= 60:
#     print("nilai C")
# else:
#     print("g lulus")

# pemakaianlistrik = int(input("Masukkan pemakaian listrik Anda (dalam kWh): "))
#     if pemakaianlistrik <= 100:
#         tarif = pemakaianlistrik * 1200
#     elif pemakaianlistrik >= 101 and pemakaianlistrik <= 300:
#         tarif = pemakaianlistrik * 1500
#     else:
#         tarif = pemakaianlistrik * 2000
    
#     print("Total tagihan listrik Anda adalah: Rp ", tarif)

nilai = int(input("Masukkan nilai Anda: "))

status = "Lulus" if nilai >= 60 else "Tidak Lulus"
print(status)
