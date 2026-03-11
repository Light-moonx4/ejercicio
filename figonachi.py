numero=int(input("digite numero:"))

z=0
x=1

for numero in range(0,numero+1):
    if numero==0:
        print(z)
    elif numero==1:
        print(x)
    elif numero>1:
        y=z+x
        z=x
        x=y
        print(x)