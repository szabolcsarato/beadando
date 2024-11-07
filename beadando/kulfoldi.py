from jarat import Jarat

class Nemzetkozi(Jarat):
    def __init__(self, jaratszam, cel, ar):
        super().__init__(jaratszam, cel, ar)

    def jarat_info(self):
        return f"Nemzetközi járat: {self.jaratszam}, Célállomás:{self.cel}, Ár:{self.ar}"