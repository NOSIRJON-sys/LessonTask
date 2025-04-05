#2 masala
sevimli_taomlar = {
    "Nosir": "osh",
    "Nodir": "manti",
    "Abdurashid": "norin",
    "Shox": "shashlik",
    "SindorAka": "lag'mon"
}

for ism in sevimli_taomlar:
    print(f"{ism}ning sevimli taomi {sevimli_taomlar[ism]}")

#1 masala

ukam={
    "ismi": "Nozimjon",
    "familya": "Ro`zmatov",
    "TYil": "2010",
    "TJoy": "Xorazm"

}
print(
    f"Ukamning ismi {ukam['ismi']} ,familiyasi {ukam['familya']}, {ukam['TYil']}-yilda {ukam['TJoy']}da tug`ilgan"
)

#3 masala

python_izohli_lugati = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
}
print(python_izohli_lugati['tuple'])

#4 masala

lugat = {
    "Dog": "It",
    "Pussy": "mushukcha",
    "phone": "telefon",
    "list": "Ro'yxat",
    "dictionary": "Lug'at"
}
kalit_soz = input("Kalit so'z kiriting: ").lower()
if kalit_soz in lugat:
    print(lugat[kalit_soz])
else:
    print("Bunda so'z mavjud emas")

#5 masala

lugat = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "list": "Ro'yxat"
}
kalit = input("Kalit so'z kiriting: ").lower()
if kalit in lugat:
    print(f"{kalit.capitalize()} so'zi {lugat[kalit]} deb tarjima qilinadi")
else:
    print("Bunday so'z mavjud emas")

