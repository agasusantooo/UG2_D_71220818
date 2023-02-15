telurbakar=7000
leleterbang=10000
escoklat=5000
esdoger=13000

print("============= MAKANAN =============")
print("1. Telur Bakar           :Rp 7.000")
print("Lele Terbang Mas Bhe     :Rp 10.000")
print("Es Coklat Lempu          :Rp 5.000")
print("4. Es Doger Langensari   :Rp 13.000")

print("=================== PESANAN ==================")
jumlahtelurbakar=int(input("Telur Bakar    : "))
jumlahleleterbang=int(input("Lele Terbang   : "))
jumlahescoklat=int(input("Es Coklat      : "))
jumlahesdoger=int(input("Es Doger       : "))

totaltelurbakar=telurbakar*jumlahtelurbakar
totalleleterbang=leleterbang*jumlahleleterbang
totalescoklat=escoklat*jumlahescoklat
totalesdoger=esdoger*jumlahesdoger
totalsemua=(totaltelurbakar + totalleleterbang + totalescoklat + totalesdoger)

print("================= TOTAL ==================")
print("TOTAL TELUR BAKAR x",jumlahtelurbakar,"           : Rp ",totaltelurbakar)
print("TOTAL LELE TERBANG x ",jumlahleleterbang,"         : Rp ",totalleleterbang)
print("TOTAL ES COKLAT x ",jumlahescoklat,"            : Rp ",totalescoklat)
print("TOTAL ES DOGER x ",jumlahesdoger,"             : Rp ",totalesdoger)
print("Jumlah total biaya yang harus dibayar adalah Rp ",totalsemua)