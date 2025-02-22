import math

n=int(input("nechta son?:"))
s=0
d=0
for i in range(1, n + 1):
    xi=float(input("xi="))
    s=s+xi/n
    d=d+(((xi-s)**2)/n-1)
d=math.pow(d,1/2)
print(s)
print(d)