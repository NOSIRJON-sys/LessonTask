class TUPLAM:
    def __init__(self):
        self.toplam = []

    def qoshish(self, element):
        if element not in self.toplam:
            self.toplam.append(element)

    def chop_etish(self):
        print("To'plam elementlari:", self.toplam)

    def get_toplam(self):
        return self.toplam.copy()


class TUPLAM_AMALLARI(TUPLAM):
    def ochirish(self, element):
        if element in self.toplam:
            self.toplam.remove(element)

    @staticmethod
    def kesishma(t1, t2):
        natija = TUPLAM()
        for el in t1.get_toplam():
            if el in t2.get_toplam():
                natija.qoshish(el)
        return natija

    @staticmethod
    def birlashma(t1, t2):
        natija = TUPLAM()
        for el in t1.get_toplam() + t2.get_toplam():
            natija.qoshish(el)
        return natija

    @staticmethod
    def ayirma(t1, t2):
        natija = TUPLAM()
        for el in t1.get_toplam():
            if el not in t2.get_toplam():
                natija.qoshish(el)
        return natija


if __name__ == "__main__":
    t1 = TUPLAM_AMALLARI()
    t1.qoshish(1)
    t1.qoshish(2)
    t1.qoshish(3)

    t2 = TUPLAM_AMALLARI()
    t2.qoshish(2)
    t2.qoshish(3)
    t2.qoshish(4)

    print("t1:")
    t1.chop_etish()

    print("t2:")
    t2.chop_etish()

    print("Kesishma:")
    kesishma = TUPLAM_AMALLARI.kesishma(t1, t2)
    kesishma.chop_etish()

    print("Birlashma:")
    birlashma = TUPLAM_AMALLARI.birlashma(t1, t2)
    birlashma.chop_etish()

    print("Ayirma (t1 - t2):")
    ayirma = TUPLAM_AMALLARI.ayirma(t1, t2)
    ayirma.chop_etish()
