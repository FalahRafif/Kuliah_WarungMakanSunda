################ Libary
import os

################ Data Karyawan
namaKaryawan = ["Asep", "Irama", "Suetono"]
passKaryawan = ["asep123", "iramacantik", "g30ppkn"]

################ Data Login
usernameLogin = ""
passLogin = ""
statusLogin = False

############### Data Menu
pilihMenu = 0
menuAktif = "login"

############### Data Pesanan
namaPembeli = []
totalHargaPesanan = []
uangDiBayar = []

pesanan = []
hargaPesanan = []
banyakPesanan = []
################ Function
def MenuLogin() : 
    global usernameLogin
    global passLogin
    global pilihMenu
    global statusLogin
    global menuAktif

    try :
        # Tampilan CLI
        print("===================================================================")
        print("                         Warung Makan Sunda")
        print("===================================================================")
        print("[1] Login")
        print("[2] Exit")
        print("")
        pilihMenu = int(input("Pilih Menu : "))

        # Cek Menu
        if pilihMenu == 2 : # Exit
            print("Terima kasih atas pekerjaan hari ini ~")
            exit()
        elif pilihMenu == 1 : # Login
            os.system('cls')
            print("===================================================================")
            print("                 Warung Makan Sunda - Login Karyawan")
            print("===================================================================")
            usernameLogin = str(input("Username      :   "))
            passLogin = str(input("Password      :   "))

            # Validasi Login
            for i in range(len(namaKaryawan) + 1) :
                if statusLogin == False and i != len(namaKaryawan) :
                    if namaKaryawan[i] == usernameLogin and passKaryawan[i] == passLogin :
                        print("Login Berhasil")
                        statusLogin = True
                        menuAktif = "dashboard"
                        return
                elif statusLogin == False and i == len(namaKaryawan) :
                    print("Username/Password tidak di temukan")
                    enter = input("...")
                    os.system('cls')
        else : 
            print("Input Menu Tidak Valid!")
            enter = input("...")
            return
    except ValueError as ex :
        ErrorHandler(ex)

def Dashboard(usernameLogin) :
    global pilihMenu
    global menuAktif
    global statusLogin
    
    try :
        # Tampilan CLI
        print("===================================================================")
        print("                 Warung Makan Sunda - Halo ", usernameLogin)
        print("===================================================================")
        print("[1] Buat Pesanan")
        print("[2] History Pesanan")
        print("[3] Logout")
        pilihMenu = int(input("Pilih Menu : "))

        # Opsi Menu
        if pilihMenu == 1 :
            menuAktif = "buat-pesanan"
            return
        elif pilihMenu == 2 :
            menuAktif = "history-pesanan"
            return
        elif pilihMenu == 3 :
            menuAktif = "login"
            statusLogin = False
            return
        else :
            print("Input Menu Tidak Valid!")
            enter = input("...")
            return
    except ValueError as ex :
        ErrorHandler(ex)

def BuatPesanan(usernameLogin) :
    try :
        global menuAktif 
        pesanan.append([])
        hargaPesanan.append([])
        nomorPesanan = len(pesanan)-1
        banyakPesanan.append([])
        totalHargaPesanan.append(0)

        # Tampilan CLI
        print("===================================================================")
        print("                 Warung Makan Sunda - Halo ", usernameLogin)
        print("                     List Menu Makanan  & Minuman       ")
        print("=========================================================================")
        print("""|       Makanan       : Harga    |        Minuman           : Harga   |  
| A. Nasi,Ayam Goreng : Rp.12000 | A. Es teh manis          : Rp.3000 |
| B. Nasi,Telur Dadar : Rp.10000 | B. Es Jeruk              : Rp.5000 |
| C. Nasi,Usus Goreng : Rp.8000  | C. Es Coklat             : Rp.4000 |
=========================================================================""")
        banyakBeli = int(input      ("Banyak Pesanan di Beli     :    "))
        pembeli = str(         input("Nama Pembeli               :    "))
        namaPembeli.append(pembeli)

        # Validasi Pesanan
        for i in range(banyakBeli) :
            print                   ("=========== [Pesanan ke " + str(i+1) +"] ===========")
            jenisPesanan = str(input(               "Jenis Pesanan (M/Mn)       :    "))
            banyakPesanan[nomorPesanan].append(int(input("Banyak Pesanan             :    ")))

            if jenisPesanan == "M" :  # Validasi Makanan
                kodeMakanan = str(input("Pilih Kode Makanan (A/B/C) :    "))       
                if kodeMakanan.upper() == "A" :
                    pesanan[nomorPesanan].append("Nasi,Ayam Goreng")
                    hargaPesanan[nomorPesanan].append(12000)
                    totalHargaPesanan[nomorPesanan] += 12000 * banyakPesanan[nomorPesanan][i]
                elif kodeMakanan.upper() == "B" :
                    pesanan[nomorPesanan].append("Nasi,Telur Dadar")
                    hargaPesanan[nomorPesanan].append(10000)
                    totalHargaPesanan[nomorPesanan] += 10000 * banyakPesanan[nomorPesanan][i]
                elif kodeMakanan.upper() == "C" :
                    pesanan[nomorPesanan].append("Nasi,Usus Goreng")
                    hargaPesanan[nomorPesanan].append(8000)
                    totalHargaPesanan[nomorPesanan] += 8000 * banyakPesanan[nomorPesanan][i]
                else : # Validasi Gagal Pilih Makanan
                    print("Kode Makanan Tidak Valid!")
                    a = input("...")
                    return
            elif jenisPesanan == "Mn" : # Validasi Minuman
                kodeMakanan = str(input("Pilih Kode Makanan (A/B/C) :    "))       
                if kodeMakanan.upper() == "A" :
                    pesanan[nomorPesanan].append("Es teh manis")
                    hargaPesanan[nomorPesanan].append(3000)
                    totalHargaPesanan[nomorPesanan] += 3000 * banyakPesanan[nomorPesanan][i]
                elif kodeMakanan.upper() == "B" :
                    pesanan[nomorPesanan].append("Es Jeruk")
                    hargaPesanan[nomorPesanan].append(5000)
                    totalHargaPesanan[nomorPesanan] += 5000 * banyakPesanan[nomorPesanan][i]
                elif kodeMakanan.upper() == "C" :
                    pesanan[nomorPesanan].append("Es Coklat")
                    hargaPesanan[nomorPesanan].append(4000)
                    totalHargaPesanan[nomorPesanan] += 4000 * banyakPesanan[nomorPesanan][i]
                else : # Validasi Gagal Pilih Minuman
                    print("Kode Minuman Tidak Valid!")
                    a = input("...")
                    return
            else : # Validasi Gagal
                # Revert Pesanan
                pesanan.pop(nomorPesanan)
                hargaPesanan.pop(nomorPesanan)
                totalHargaPesanan.pop(nomorPesanan)
                namaPembeli.pop(nomorPesanan)
                banyakPesanan.pop(nomorPesanan)

                print("Kode Makanan Tidak Valid!")
                a= input("...")
                menuAktif = "dashboard"
                return

        # Validasi Uang Bayar
        print("Total Harga                :    Rp.", totalHargaPesanan[nomorPesanan])
        uangBayar = int(input("Uang di Bayar              :    Rp. "))
        if uangBayar < totalHargaPesanan[nomorPesanan] :
            print("Uang Tidak Cukup!")
            enter = input("...")
            menuAktif = "dashboard"
            return
        else :
            uangDiBayar.append(uangBayar)

        BuatStruk(nomorPesanan+1)
    except ValueError as ex : 
        ErrorHandler(ex)

def BuatStruk(nomorPesanan = 0) :
    global menuAktif
    os.system("cls")

    # Validasi nomor pesanan
    try :
        if nomorPesanan == 0 :
            print("Nomor Pesanan Tidak Valid!")
            enter = input("...")
            menuAktif = "dashboard"
            return
        testPesanan = namaPembeli[nomorPesanan-1]
        nomorPesanan = nomorPesanan - 1
    except :
        print("Nomor Pesanan Tidak Valid!")
        enter = input("...")
        menuAktif = "dashboard"
        return
    
    # Buat Struk
    print("===========================================")
    print("===========S T R U K   B E L I ============")
    print("===========================================")
    print(" Kasir        : ", usernameLogin)
    print(" Pembeli      : ", namaPembeli[nomorPesanan])
    print(" --------------------------------------------")
    for i in range(len(pesanan[nomorPesanan])) :
        print(" %i. %ix - %s (Rp.%s) = Rp. %s" %(
            (i+1) #nomor struk
            , banyakPesanan[nomorPesanan][i] #banyak pesanan
            , pesanan[nomorPesanan][i] #nama pesanan
            , hargaPesanan[nomorPesanan][i] #harga per satuan
            , (banyakPesanan[nomorPesanan][i] * hargaPesanan[nomorPesanan][i]) # Total Harga Pesanan
        ))
    print(" --------------------------------------------")
    print(" Total Harga  : Rp.", totalHargaPesanan[nomorPesanan])
    print(" Uang di Bayar: Rp.", uangDiBayar[nomorPesanan])
    print(" Kembalian    : Rp.", (uangDiBayar[nomorPesanan] - totalHargaPesanan[nomorPesanan]))
    print("=============================================")
    print("=============================================")

    print("")
    print("Struk Tersimpan")
    enter = input("...")
    menuAktif = "dashboard"
    return

def HistoryPesanan(usernameLogin) :
    global menuAktif
    totalPesanan = len(namaPembeli)

    try :
        print("===================================================================")
        print("                 Warung Makan Sunda - Halo ", usernameLogin)
        print("                            History Pesanan       ")
        print("=========================================================================")
        
        for i in range(totalPesanan) :
            print("%i. Pesanan Atas Nama '%s' - Total Harga : %i" %(
                (i+1) #nomor history
                , namaPembeli[i] #nama pembeli
                , totalHargaPesanan[i] #total harga pesanan
            ))
        print("=========================================================================")
        print("[1] Cek Detail/Buat Struk")
        print("[2] Kembali")

        pilihMenu = int(input("Pilih Menu : "))

        if pilihMenu == 1 :
            pilihMenu = int(input("Pilih Nomor History Pesanan : "))
            BuatStruk(pilihMenu)
        elif pilihMenu == 2 :
            menuAktif = "dashboard"
            return
        else :
            print("Input Menu Tidak Valid!")
            enter = input("...")
            return
    except ValueError as ex :
        ErrorHandler(ex)
    
def ErrorHandler(ex) : 
    print("=======================[Error]=======================")
    print(ex)
    print("=======================[Error]=======================")
    print("Terjadi Kesalahan Sistem, Silahkan di Coba Kembali",)
    a = input("...")