from datetime import datetime
from datetime import datetime
from jarat import Jarat
from foglalas import Foglalas
from datetime import datetime

class Tarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jegy_foglalas(self, jarat, nev, datum):
        if self.datum_ell(datum):
            foglalas = Foglalas(nev, jarat, datum)
            self.foglalasok.append(foglalas)
            return "Sikeres foglalás! Jegy ára: "f"{jarat.ar} FT"
        return "Érvénytelen dátum"

    @staticmethod
    def datum_ell(datum: str):
        try:
            datum = datetime.strptime (datum, "%Y-%m-%d")
            return datum >= datetime.now()
        except ValueError:
            return False

    def lemondas(self, jarat_szam):
        for foglalas in self.foglalasok:
            if foglalas.jarat.jaratszam == jarat_szam:
                self.foglalasok.remove(foglalas)
                return f"{jarat_szam} Foglalása lemondva."
        return "Foglalás nem található."

    def jarat_hozzadas(self, flight):
        self.jaratok.append(flight)

    def fogl_lista(self):
        if self.foglalasok:
            for foglalas in self.foglalasok:
                return foglalas.jarat.jarat_info()
        else:
            return "Jelenleg nincs foglalás."

