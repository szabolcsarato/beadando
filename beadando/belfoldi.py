from jarat import Jarat

class Belfoldi(Jarat):
    def __init__(self, jaratszam, cel, ar):
        super().__init__(jaratszam, cel, ar)

    def jarat_info(self):
        return f"Belföldi járat: {self.jaratszam}, Célállomás: {self.cel}, Jegyár: {self.ar}  FT"


