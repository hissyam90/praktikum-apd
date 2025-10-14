pengguna = [["admin", "123", "admin"]]
pegawai = []
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

        sudah_ada = False
        for user in pengguna:
            if user[0] == username:
                sudah_ada = True
        if sudah_ada:
            print("Username sudah terdaftar.")
        else:
            pengguna.append([username, password, role])
            print("Registrasi berhasil! Silakan login.")

    # login
    elif menu == "2":
        if len(pengguna) == 0:
            print("Belum ada pengguna, silakan registrasi dahulu.")
        else:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            login = None
            for user in pengguna:
                if user[0] == username and user[1] == password:
                    login = user
            if login == None:
                print("Username atau password salah.")
            else:
                print("Login berhasil sebagai", login[2])
                # menu admin
                if login[2] == "admin":
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
                                for p in pegawai:
                                    print(f"ID: {p[0]} | Nama: {p[1]} | Jabatan: {p[2]} | Nomor HP: {p[3]}")

                        # create
                        elif pilihan == "2":
                            idp = input("Masukkan ID Pegawai: ")
                            nama = input("Masukkan Nama Pegawai: ")
                            jabatan = input("Masukkan Jabatan: ")
                            hp = input("Masukkan Nomor HP: ")
                            pegawai.append([idp, nama, jabatan, hp])
                            print("Data pegawai berhasil ditambahkan.")

                        # update
                        elif pilihan == "3":
                            if len(pegawai) == 0:
                                print("Belum ada data pegawai.")
                            else:
                                id_edit = input("Masukkan ID Pegawai yang ingin diubah: ")
                                ditemukan = False
                                for p in pegawai:
                                    if p[0] == id_edit:
                                        ditemukan = True
                                        nama_baru = input("Masukkan Nama baru: ")
                                        jabatan_baru = input("Masukkan Jabatan baru: ")
                                        hp_baru = input("Masukkan Nomor HP baru: ")
                                        p[1] = nama_baru
                                        p[2] = jabatan_baru
                                        p[3] = hp_baru
                                        print("Data berhasil diperbarui.")
                                if not ditemukan:
                                    print("ID pegawai tidak ditemukan.")

                        # delete
                        elif pilihan == "4":
                            if len(pegawai) == 0:
                                print("Belum ada data pegawai.")
                            else:
                                id_hapus = input("Masukkan ID Pegawai yang ingin dihapus: ")
                                hapus = False
                                for i in range(len(pegawai)):
                                    if pegawai[i][0] == id_hapus:
                                        del pegawai[i]
                                        hapus = True
                                        print("Data pegawai berhasil dihapus.")
                                        break
                                if not hapus:
                                    print("ID pegawai tidak ditemukan.")

                        elif pilihan == "5":
                            print("Logout berhasil.")
                            login = None
                            break
                        else:
                            print("Pilihan tidak valid.")

                # menu user
                elif login[2] == "pengguna":
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
                                for p in pegawai:
                                    print(f"ID: {p[0]} | Nama: {p[1]} | Jabatan: {p[2]} | Nomor HP: {p[3]}")
                        elif pilihan == "2":
                            print("Logout berhasil.")
                            login = None
                            break
                        else:
                            print("Pilihan tidak valid.")

    elif menu == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid.")
