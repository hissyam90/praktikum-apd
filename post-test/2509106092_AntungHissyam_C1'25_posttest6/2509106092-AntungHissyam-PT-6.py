pengguna = {
    "admin": {"password": "123", "role": "admin"}
}

pegawai = {}  
login = None

while True:
    print("""
=====================================
| PROGRAM MANAJEMEN PEGAWAI         |
| Perusahaan Cumi Hitam Pak Kris    |
=====================================
| 1. Register                       |
| 2. Login                          |
| 3. Keluar                         |
=====================================
""")

    menu = input("Pilih menu: ")

    # register
    if menu == "1":
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        while True:
            role = input("Masukkan role (admin/pengguna): ")
            if role == "admin" or role == "pengguna":
                break
            else:
                print("Role tidak valid, hanya boleh 'admin' atau 'pengguna'.")

        if username in pengguna:
            print("Username sudah terdaftar.")
        else:
            pengguna[username] = {"password": password, "role": role}
            print("Registrasi berhasil! Silakan login.")

    # login
    elif menu == "2":
        if len(pengguna) == 0:
            print("Belum ada pengguna, silakan registrasi dahulu.")
        else:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if username in pengguna and pengguna[username]["password"] == password:
                login = {"username": username, "role": pengguna[username]["role"]}
                print("Login berhasil sebagai", login["role"])

                # menu admin
                if login["role"] == "admin":
                    while True:
                        print("""
==============================
| MENU ADMIN                 |
==============================
| 1. Lihat Data Pegawai      |
| 2. Tambah Pegawai          |
| 3. Edit Data Pegawai       |
| 4. Hapus Pegawai           |
| 5. Logout                  |
==============================
""")
                        pilihan = input("Pilih menu: ")

                        # read
                        if pilihan == "1":
                            if len(pegawai) == 0:
                                print("Belum ada data pegawai.")
                            else:
                                print("=== DATA PEGAWAI ===")
                                for idp, data in pegawai.items():
                                    print(f"ID: {idp} | Nama: {data['nama']} | Jabatan: {data['jabatan']} | Nomor HP: {data['hp']}")

                        # create
                        elif pilihan == "2":
                            idp = input("Masukkan ID Pegawai: ")
                            if idp in pegawai:
                                print("ID pegawai sudah terdaftar.")
                            else:
                                nama = input("Masukkan Nama Pegawai: ")
                                jabatan = input("Masukkan Jabatan: ")
                                hp = input("Masukkan Nomor HP: ")
                                pegawai[idp] = {"nama": nama, "jabatan": jabatan, "hp": hp}
                                print("Data pegawai berhasil ditambahkan.")

                        # update
                        elif pilihan == "3":
                            if len(pegawai) == 0:
                                print("Belum ada data pegawai.")
                            else:
                                id_edit = input("Masukkan ID Pegawai yang ingin diubah: ")
                                if id_edit in pegawai:
                                    nama_baru = input("Masukkan Nama baru: ")
                                    jabatan_baru = input("Masukkan Jabatan baru: ")
                                    hp_baru = input("Masukkan Nomor HP baru: ")
                                    pegawai[id_edit]["nama"] = nama_baru
                                    pegawai[id_edit]["jabatan"] = jabatan_baru
                                    pegawai[id_edit]["hp"] = hp_baru
                                    print("Data berhasil diperbarui.")
                                else:
                                    print("ID pegawai tidak ditemukan.")

                        # delete
                        elif pilihan == "4":
                            if len(pegawai) == 0:
                                print("Belum ada data pegawai.")
                            else:
                                id_hapus = input("Masukkan ID Pegawai yang ingin dihapus: ")
                                if id_hapus in pegawai:
                                    del pegawai[id_hapus]
                                    print("Data pegawai berhasil dihapus.")
                                else:
                                    print("ID pegawai tidak ditemukan.")

                        elif pilihan == "5":
                            print("Logout berhasil.")
                            login = None
                            break
                        else:
                            print("Pilihan tidak valid.")

                # menu pengguna
                elif login["role"] == "pengguna":
                    while True:
                        print("""
==============================
| MENU PENGGUNA              |
==============================
| 1. Lihat Data Pegawai      |
| 2. Logout                  |
==============================
""")
                        pilihan = input("Pilih menu: ")
                        if pilihan == "1":
                            if len(pegawai) == 0:
                                print("Belum ada data pegawai.")
                            else:
                                print("=== DATA PEGAWAI ===")
                                for idp, data in pegawai.items():
                                    print(f"ID: {idp} | Nama: {data['nama']} | Jabatan: {data['jabatan']} | Nomor HP: {data['hp']}")
                        elif pilihan == "2":
                            print("Logout berhasil.")
                            login = None
                            break
                        else:
                            print("Pilihan tidak valid.")
            else:
                print("Username atau password salah.")

    elif menu == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid.")
