################ Libary
import os

################ Data Karyawan
namaKaryawan = ["Asep", "Irama", "Suetono"]
passKaryawan = ["asep123", "iramacantik", "g30ppkn"]

################ Property
usernameLogin = ""
passLogin = ""
statusLogin = True
pilihMenu = 0
menuAktif = "login"

################ Function
def MenuLogin() : 
    global usernameLogin
    global passLogin
    global pilihMenu
    global statusLogin
    global menuAktif

    print("===================================================================")
    print("                         Warung Makan Sunda")
    print("===================================================================")
    print("[1] Login")
    print("[2] Exit")
    print("")
    pilihMenu = int(input("Pilih Menu : "))

    # Cek Menu
    if pilihMenu == 2 :
        print("Terima kasih atas pekerjaan hari ini ~")
        exit()
    elif pilihMenu == 1 :
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
            elif statusLogin == False and i == len(namaKaryawan) :
                print("Username/Password tidak di temukan")
                ctn = input("...")
                os.system('cls')
            

def Dashboard(usernameLogin) :
    print("===================================================================")
    print("                 Warung Makan Sunda - Halo ", usernameLogin)
    print("===================================================================")
    print("[1] Buat Pesanan")
    print("[2] Cek Pesanan")
    print("[3] Logout")

i = 1
while i == 1 :
    os.system('cls')

    match menuAktif :
        case "login" :
            MenuLogin()
        case "dashboard" :
            Dashboard(usernameLogin)

exit()



print("""
    ===================================================================
 
                                        Warung Sunda
                                List Menu Makanan dan Minuman 
      
    =====================================================================
    :      Makanan      : Harga    :        Minuman           : Harga   :      
    :A. Nasi,Ayam Goreng: Rp.12000 : A. Es teh manis          : Rp.3000 :
    :B. Nasi,Telur dadar: Rp.10000 : B. Es Jeruk              : Rp.5000 :
    :C. Nasi,Usus Goreng: Rp.8000  : C. Es Coklat             : Rp.4000 :
    ====================================================================
    """)
pembeli = input("Masukan Nama Pembeli: ")
print ("Nama Pembeli :", pembeli)

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
    global total1
    global porsi
    global jenis1
    print("/~~Menu Makanan~~")
    print("1. Nasi,Ayam Goreng - Rp12000")
    print("2. Nasi,Telur dadar - Rp10000")
    print("3. Nasi,Usus Goreng - Rp8000 ")
    nomor=int(input("Masukan Pilihan:  "))
    porsi=int(input("Berapa porsi   :  "))

    if nomor==1:
        total1=porsi*12000
        print (porsi,"porsi Nasi,Ayam Goreng = Rp", total1)
        jenis1=("Nasi,Ayam Goreng")
    elif nomor==2:
        total1=porsi*10000
        print (porsi,"porsi Nasi,Telur dadar = Rp", total1)
        jenis1=("Nasi,Telur dadar")
    elif nomor==2:
        total1=porsi*8000
        print (porsi,"porsi Nasi,Usus Goreng = Rp", total1)
        jenis1=("Nasi,Usus Goreng")
    else:
        print("Pilihan tifak ada")
        fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
    global total2
    global jenis2
    global gelas
    print("/n~~Menu Minuman~~")
    print("1. Es teh manis          - Rp3000")
    print("2. Es jeruk              - Rp5000")
    print("3. Es Coklat             - Rp4000") 
    nomor=int(input("Masukan Pilihan:"))
    gelas=int(input("Berapa Gelas   :"))
    
    if nomor==1:
        total2=gelas*3000
        print(gelas," Es teh manis = Rp")
        jenis2=(" Gelas Es teh manis")
    elif nomor==2:
        total2=gelas*5000
        print(gelas," Es Jeruk")
        jenis2=(" Gelas Es Jeruk")
    elif nomor==3:
        total2=gelas*4000
        print(gelas," Es Coklat")
        jenis2=(" Gelas Es Coklat")
    else:
        print("Pilihan tidak ada")
        fungsiminuman


fungsiminuman()

totalsemua=0
totalsemua=total1+total2
print("/nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("/n===========================================")
print("===========S T R U K   B E L I ============")
print("===========================================")
print (" Nama         :",pembeli)
print (" Makanan      :",porsi,jenis1,"-",total1)
print (" Minuman      :",gelas,jenis2,"-",total2)
print (" Tagihan      : Rp.",totalsemua)
print (" Uang         : Rp.",uang)
print(" Kembalian     : Rp.",kembalian)
print("=============================================")
print("=============================================")