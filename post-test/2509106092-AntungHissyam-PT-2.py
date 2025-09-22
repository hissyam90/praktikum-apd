nama = input("nama :")
nim = input("nim :")
hargalaptop = int(input("harga laptop :"))

laptopAcer = hargalaptop - int(hargalaptop * 5/100)
laptopAsus = hargalaptop - int(hargalaptop * 7/100)
laptopLenovo = hargalaptop - int(hargalaptop * 10/100)

print(f"{nama} dengan nim {nim} ingin membeli laptop seharga Rp{hargalaptop:,}")
print(f"jika {nama} membeli laptop acer, maka harganya setelah diskon 5% adalah Rp{laptopAcer:,}")
print(f"jika {nama} membeli laptop asus, maka harganya setelah diskon 7% adalah Rp{laptopAsus:,}")
print(f"jika {nama} membeli laptop lenovo, maka harganya setelah diskon 10% adalah Rp{laptopLenovo:,}")