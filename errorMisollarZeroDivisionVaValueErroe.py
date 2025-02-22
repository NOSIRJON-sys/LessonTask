try:

    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("ikkinchi sonni kiriting: "))
    c=a/b
    print(f"c= {c}")
except ZeroDivisionError:
    print("maxrajda nol bo`b qoldi")
except ValueError:
    print("raqamli qiymat kiriting")