################ Libary
import os
import Function.Modul as _modul
################ Looping Menu
i = 1
while i == 1 :
    os.system('cls')

    try : 
        match _modul.menuAktif :
            case "login" :
                _modul.MenuLogin()
            case "dashboard" :
                _modul.Dashboard(_modul.usernameLogin)
            case "buat-pesanan" :
                _modul.BuatPesanan(_modul.usernameLogin)
            case "history-pesanan" :
                _modul.HistoryPesanan(_modul.usernameLogin)
    except ValueError as ex:
        print("=======================[Error]=======================")
        print(ex)
        print("=======================[Error]=======================")
        print("Terjadi Kesalahan Sistem, Silahkan di Coba Kembali",)
        a = input("...")

exit()