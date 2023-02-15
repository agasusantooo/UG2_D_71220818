brand=input("Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma): ")


hargabrand1=int(input("Berapa harga barang H&M ? :"))

if (hargabrand1>24999999):
    diskonbarang1=hargabrand1*(25/100)
    print("Harga H&M    Rp. ",hargabrand1,"  Diskon Rp.",diskonbarang1)
elif (hargabrand1>9999999):
    diskonbarang1=hargabrand1*(10/100)
    print("Harga H&M     Rp. ",hargabrand1,"  Diskon Rp.",diskonbarang1)
else:
    diskonbarang1=0
    print("Harga H&M     Rp. ",hargabrand1,"  Diskon Rp. 0")

hargabrand2=int(input("Berapa harga barang Fendi ? :"))

if (hargabrand2>24999999):
    diskonbarang2=hargabrand2*(25/100)
    print("Harga Fendi    Rp. ",hargabrand2,"  Diskon Rp.",diskonbarang2)
elif (hargabrand2>9999999):
    diskonbarang2=hargabrand2*(10/100)
    print("Harga Fendi     Rp. ",hargabrand2,"  Diskon Rp.",diskonbarang2)
else:
    print("Harga Fendi     Rp. ",hargabrand2,"  Diskon Rp. 0")

hargabrand3=int(input("Berapa harga barang LV ? :"))

if (hargabrand3>24999999):
    diskonbarang3=hargabrand3*(25/100)
    print("Harga LV    Rp. ",hargabrand3,"  Diskon Rp.",diskonbarang3)
elif (hargabrand3>9999999):
    diskonbarang3=hargabrand3*(10/100)
    print("Harga LV     Rp. ",hargabrand3,"  Diskon Rp.",diskonbarang3)
else:
    print("Harga LV     Rp. ",hargabrand3,"  Diskon Rp. 0")
    
hargabrand4=int(input("Berapa harga barang Dior ? :"))

if (hargabrand4>24999999):
    diskonbarang4=hargabrand4*(25/100)
    print("Harga Dior    Rp. ",hargabrand4,"  Diskon Rp.",diskonbarang4)
elif (hargabrand4>9999999):
    diskonbarang4=hargabrand4*(10/100)
    print("Harga Dior     Rp. ",hargabrand4,"  Diskon Rp.",diskonbarang4)
else:
    print("Harga Dior     Rp. ",hargabrand4,"  Diskon Rp. 0")

totaldiskon=(diskonbarang1 + diskonbarang2 + diskonbarang3 + diskonbarang4)
totalbayar=((hargabrand1+hargabrand2+hargabrand3+hargabrand4)-totaldiskon)

print("Total diskon yang anda dapatkan adalah sebesar: Rp.",totaldiskon)
print("Total uang yang harus anda bayarkan adalah: Rp.",totalbayar)