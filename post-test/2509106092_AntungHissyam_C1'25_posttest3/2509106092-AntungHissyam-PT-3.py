login="antung"
pw = "092"


user= input("masukkan username: ")
passw= input("masukkan password: ")
if user==login and passw==pw:
    print("\nlogin berhasil\n")
    print("=== MENU PEMBAYARAN UKT ===")
    print("1. Lunas (sekali bayar) - Biaya admin 1%")
    print("2. Cicilan 2x per semester - Biaya admin 5%")
    print("3. Cicilan 4x per semester - Biaya admin 8%")
    print("4. Cicilan 6x per semester - Biaya admin 12%")
    pilihan = input("Pilih metode pembayaran (1-4): ")

    # ukt
    ukt = 6000000

    if pilihan == "1":
        admin = 1/100
        total = ukt + (ukt * admin)
        print(f"\n=== HASIL PEMBAYARAN ===")
        print(f"Total yang harus dibayar: Rp {total:,}")

    elif pilihan == "2":
        admin = 5/100
        total = ukt + (ukt * admin)
        cicilan = total / 2
        print(f"\n=== HASIL PEMBAYARAN ===")
        print(f"Total yang harus dibayar: Rp {total:,}")
        print(f"Cicilan per periode (2x): Rp {cicilan:,}")

    elif pilihan == "3":
        admin = 8/100
        total = ukt + (ukt * admin)
        cicilan = total / 4
        print(f"\n=== HASIL PEMBAYARAN ===")
        print(f"Total yang harus dibayar: Rp {total:,}")
        print(f"Cicilan per periode (4x): Rp {cicilan:,}")

    elif pilihan == "4":
        admin = 12/100
        total = ukt + (ukt * admin)
        cicilan = total / 6
        print(f"\n=== HASIL PEMBAYARAN ===")
        print(f"Total yang harus dibayar: Rp {total:,}")
        print(f"Cicilan per periode (6x): Rp {cicilan:,}")

    else:
        print("Pilihan tidak valid.")
else:
    print("login gagal")