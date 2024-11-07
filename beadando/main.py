from tarsasag import Tarsasag
from jarat import Jarat
from belfoldi import Belfoldi
from kulfoldi import Nemzetkozi
from foglalas import Foglalas

#adatok
tarsasag = Tarsasag("Malév")
Belfoldi1 = Belfoldi("D345", "Sopron", 11000)
Belfoldi2 = Belfoldi("D346", "Pécs", 9000)
Belfoldi3 = Belfoldi("D347", "Debrecen", 10000)
Nemzetkozi1 = Nemzetkozi("I987", "Rotterdam", 20000)
Nemzetkozi2 = Nemzetkozi("I789", "New York", 45000)
tarsasag.jarat_hozzadas(Belfoldi1)
tarsasag.jarat_hozzadas(Belfoldi2)
tarsasag.jarat_hozzadas(Belfoldi3)
tarsasag.jarat_hozzadas(Nemzetkozi1)
tarsasag.jarat_hozzadas(Nemzetkozi2)


def menu():
    while True:
        print("\n Menüpont kiválasztása:")
        print("1 Jegy foglalás:")
        print("2 Foglalás lemondása:")
        print("3 Aktuális foglalások:")
        print("4 Kilépés")

        valasztas = input("Add meg a megtekinteni kívánt menüpont számát: ")

        if valasztas == "1":
            jaratszam = input("Add meg a foglalni kívánt járat számát: ")
            jarat = next((j for j in tarsasag.jaratok if j.jaratszam == jaratszam), None)
            if jarat:
                nev = input("Add meg a neved : ")
                datum = input("Mikorra szeretnéd foglalni?(ÉÉÉÉ-HH-NN): ")
                foglalas = tarsasag.jegy_foglalas(jarat, nev, datum)
                print(foglalas)
            else:
                print("Nincs ilyen járat.")

        elif valasztas == "2":
            jaratszam = input("Add meg a lemondani kívánt járat számát: ")
            eredmeny = tarsasag.lemondas(jaratszam)
            print(eredmeny)
        elif valasztas == "3":
            print("Aktuális foglalások:")
            print(tarsasag.fogl_lista())
        elif valasztas == "4":
            print("Kilépés... Viszlát!")
            break
        else:
            print("Ilyen menüpont nincs, próbáld újra.")



menu()

