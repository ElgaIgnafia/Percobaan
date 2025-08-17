def main():
    print("Tentukan tipe suhu awal yang ingin Anda konversikan!")
    print("Ketik 1 untuk Celcius")
    print("Ketik 2 untuk Reamur")
    print("Ketik 3 untuk Fahreinheit")
    
    x = int(input())
    
    if x == 1:
        print("Masukkan nilai suhu dalam Celcius")
        celcius = float(input())
        fahreinheit = (9.0/5.0*celcius) + 32
        reamur = (4.0/5.0*celcius)
        print(f"Konversi Suhu {celcius} Celcius ke Fahreinheit adalah {fahreinheit}")
        print(f"Konversi Suhu {celcius} Celcius ke Reamur adalah {reamur}")
    elif x == 2:
        print("Masukkan nilai suhu dalam Reamur")
        reamur = float(input())
        fahreinheit = (9.0/4.0*reamur) + 32
        celcius = (5.0/4.0*reamur)
        print(f"Konversi Suhu {reamur} Reamur ke Fahreinheit adalah {fahreinheit}")
        print(f"Konversi Suhu {reamur} Reamur ke Celcius adalah {celcius}")
    elif x == 3:
        print("Masukkan nilai suhu dalam Fahreinheit")
        fahreinheit = float(input())
        reamur = (4.0/9.0*(fahreinheit-32))
        celcius = (5.0/9.0*(fahreinheit-32))
        print(f"Konversi Suhu {fahreinheit} Fahreinheit ke Reamur adalah {reamur}")
        print(f"Konversi Suhu {fahreinheit} Fahreinheit ke Celcius adalah {celcius}")

if __name__ == "__main__":
    main()