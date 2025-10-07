print("=== Selamat Datang di Toko Furnitur Infordeh ===")

login = "antung"
pw = "092"
percobaan = 0
login_berhasil = False

while percobaan < 3:
    user = input("Masukkan Username: ")
    passw = input("Masukkan Password (NIM): ")

    if user == login and passw == pw:
        print("Login berhasil!\n")
        login_berhasil = True
        break
    else:
        percobaan += 1
        print(f"Username atau password salah! Percobaan ke-{percobaan}")

if not login_berhasil:
    print("\nLogin gagal 3 kali. Program berhenti.")
    exit()

while True:
    print("\n=== Menu Pembelian Furnitur ===")
    print("1. Sofa - Rp 500.000")
    print("2. Meja Belajar - Rp 250.000")
    print("3. Rak Lemari - Rp 150.000")
    print("4. Keluar")

    pilihan = input("Pilih furnitur (1-4): ")

    if pilihan == "1":
        nama_barang = "Sofa"
        harga = 500000
    elif pilihan == "2":
        nama_barang = "Meja Belajar"
        harga = 250000
    elif pilihan == "3":
        nama_barang = "Rak Lemari"
        harga = 150000
    elif pilihan == "4":
        print("Terima kasih telah berbelanja di Toko Furnitur Infordeh!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")
        continue

    jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: "))

    # hitung total bayar pake for
    total_bayar = 0
    for i in range(jumlah):
        total_bayar += harga

    # struk
    print("\n=== STRUK PEMBELIAN ===")
    print(f"{nama_barang} x{jumlah} Rp {harga:,}      : Rp {total_bayar:,}")
    print("---------------------------------------")

    # hitung diskon & hadiah
    if total_bayar >= 700000:
        potongan = total_bayar * 20/100
        total_akhir = total_bayar - potongan
        print(f"Diskon 20% diterapkan   : -Rp {potongan:,}")
        print(f"Total Bayar Akhir       : Rp {total_akhir:,}")

    elif total_bayar >= 500000 and total_bayar < 700000:
        potongan = total_bayar * 8/100
        total_akhir = total_bayar - potongan
        print(f"Diskon 8% diterapkan    : -Rp {potongan:,}")
        print(f"Total Bayar Akhir       : Rp {total_akhir:,}")

    elif total_bayar >= 150000 and total_bayar < 500000:
        total_akhir = total_bayar
        print("Selamat Anda mendapatkan hadiah Kitchen Set.")
        print(f"Total Bayar : Rp {total_akhir:,}")

    else:
        total_akhir = total_bayar
        print("Belanja di bawah Rp150.000 tidak mendapat potongan atau hadiah.")
        print(f"Total Bayar : Rp {total_akhir:,}")

    print("==============================")
    print("Terima kasih telah berbelanja di Toko Furnitur Infordeh!\n")
    continue
