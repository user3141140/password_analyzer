import string
import random

def cek_kekuatan_password(password):
    
    daftar_pasaran = ["123456", "password", "rahasia", "qwerty", "123456789"]
    
    if password.lower() in daftar_pasaran:
        print("\n=== HASIL ANALISIS PASSWORD ===")
        print(f"Password kamu: {password}")
        return "🔴 KEKUATAN: SANGAT LEMAH! (⚠️ Password ini terlalu berbahaya, sangat mudah ditebak!)"
    
    panjang = len(password)
    ada_besar = any(char.isupper() for char in password)
    ada_besar = any(char.isupper() for char in password)
    ada_kecil = any(char.islower() for char in password)
    ada_angka = any(char.isdigit() for char in password)
    ada_simbol = any(char in string.punctuation for char in password)
    
    skor = 0
    if panjang >= 10: skor += 1
    if panjang >= 15: skor += 1
    if ada_besar and ada_kecil: skor += 1
    if ada_angka: skor += 1
    if ada_simbol: skor += 1
    
    print("\n=== HASIL ANALISIS PASSWORD ===")
    print(f"Password kamu: {password}")
    print(f"Panjang: {panjang} karakter")
    
    if skor <= 2:
        return "🔴 KEKUATAN: LEMAH! (Sangat mudah ditebak/dihack)"
    elif skor <= 4:
        return "🟡 KEKUATAN: SEDANG! (Lumayan, tapi bisa ditingkatkan lagi)"
    else:
        return "🟢 KEKUATAN: SANGAT KUAT! (Aman dari metode Brute Force)"

def buat_password_otomatis(panjang_req):
    karakter = string.ascii_letters + string.digits + string.punctuation
    password_baru = ''.join(random.choice(karakter) for i in range(panjang_req))
    return password_baru

while True: 
      
        print("=== TOOLS KEAMANAN PASSWORD SEDERHANA ===")
        print("1. Cek Kekuatan Password")
        print("2. Buat Password Aman")
        print("3. Keluar dari program")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
              pwd = input("Masukkan password yang mau dicek: ")
              hasil = cek_kekuatan_password(pwd)
              print(hasil)
        elif pilihan == "2":
              panjang = int(input("berapa panjang karakter yang diinginkan? (Saran: minimal 15): "))
              pwd_aman = buat_password_otomatis(panjang)
              print(f"\nPassword aman buat kamu: {pwd_aman}")
              print("🟢 KEKUATAN: SANGAT KUAT! (Karena acak, angka, & simbol)")
        elif pilihan =="3":
              print("Terima kasih telah mencoba program kami :)") 
              break
        else:
              print("Pilihan tidak valid, Coba lagi") 
