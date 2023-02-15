pelanggan=[]
jenismember=[]
def menu():
    print("!! Selamat datang di H+ Gym !!")
    print("Silahkan pilih menu dibawah ini:")
    print("1. Menambah data")
    print("2. Menampilkan data")
    print("3. Keluar")
    pilihan=int(input("Silahkan masukan pilihan yang anda inginkan : "))
    if (pilihan == 1):
        nama=input("Masukkan nama pelanggan :")
        member=input("Masukkan jenis member : ")
        pelanggan.append(nama)
        jenismember.append(member)
        print("Data sudah berhasil ditambahkan!")
        menu()
    elif (pilihan == 2):
        print("Pelanggan    Member")
        for i in pelanggan:
            print (str(pelanggan) , str(jenismember))
        menu()
    else :
        print("Sistem Berhenti...")

menu()