class Tuplam:
    def __init__(self, elementlar=None):
        if elementlar is None:
            self.elementlar = set()
        else:
            self.elementlar = set(elementlar)

    def qoshing(self, element):
        self.elementlar.add(element)

    def ochirish(self, element):
        self.elementlar.discard(element)

    def kesishma(self, boshqa_tuplam):
        return Tuplam(self.elementlar & boshqa_tuplam.elementlar)

    def birlashma(self, boshqa_tuplam):
        return Tuplam(self.elementlar | boshqa_tuplam.elementlar)

    def ayirma(self, boshqa_tuplam):
        return Tuplam(self.elementlar - boshqa_tuplam.elementlar)

    def __str__(self):
        return f"{self.elementlar}"

    def __repr__(self):
        return self.__str__()

a = Tuplam([1, 2, 3, 4])
b = Tuplam([3, 4, 5, 6])

print("a:", a)
print("b:", b)

a.qoshing(7)
print("a ga 7 qo‘shildi:", a)

a.ochirish(2)
print("a dan 2 o‘chirildi:", a)

print("Kesishma:", a.kesishma(b))
print("Birlashma:", a.birlashma(b))
print("Ayirma (a - b):", a.ayirma(b))
