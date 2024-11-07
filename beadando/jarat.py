from abc import ABC

class Jarat(ABC):
    def __init__(self, jaratszam, cel, ar):
        self.jaratszam = jaratszam
        self.cel = cel
        self.ar = ar

    def jarat_info(self):
        return self.jaratszam, self.cel, self.ar
        pass

