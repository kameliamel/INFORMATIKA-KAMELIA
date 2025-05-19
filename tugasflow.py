def hitung(a, b, pilihan):
    if pilihan == "1":
        return a + b
    elif pilihan == "2":
        return a - b
    elif pilihan == "3":
        return a * b
    elif pilihan == "4":
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol!"
    else:
        return "Pilihan tidak valid!"

# Program utama
while True:
    print("\n=== MENU KALKULATOR ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    pilihan = input("Pilih operasi (1/2/3/4/5): ")

    if pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    try:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))

        hasil = hitung(a, b, pilihan)
        print("Hasil:", hasil)
    except ValueError:
        print("Input tidak valid! Masukkan angka.")