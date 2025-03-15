def complex_sonlar(a1, b1, a2, b2, operation):
    z1 = complex(a1, b1)
    z2 = complex(a2, b2)

    if operation == "+":
        return z1 + z2
    elif operation == "-":
        return z1 - z2
    elif operation == "*":
        return z1 * z2
    elif operation == "/":
        if z2 != 0:
            return z1 / z2
        else:
            return "Nolga bo‘lish mumkin emas!"
    else:
        return "Noto‘g‘ri amal!"
a1=int(input("a1="))
b1=int(input("b1="))
a2=int(input("a2="))
b2=int(input("b2="))

print("Qo‘shish:", complex_sonlar(a1, b1, a2, b2, "+"))
print("Ayirish:", complex_sonlar(a1, b1, a2, b2, "-"))
print("Ko‘paytirish:", complex_sonlar(a1, b1, a2, b2, "*"))
print("Bo‘lish:", complex_sonlar(a1, b1, a2, b2, "/"))
