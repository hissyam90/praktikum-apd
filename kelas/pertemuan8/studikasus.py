import random

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""

for i in range(12):
    kata_sandi += random.choice(karakter)

print(kata_sandi)
