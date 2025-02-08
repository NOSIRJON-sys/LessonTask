import math

x=int(input("X="))
if x<-2:
    y=math.sin(x)+math.sqrt(math.fabs(x+2))
elif x>2:
    y=math.pow(x+5,1/3)*math.tan(x/2)
else:
    y=x**2*(math.cos(math.pi))+math.log(x+6.78)
print("y=",y)


