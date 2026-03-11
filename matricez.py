n=int(input("digite el tamaño de la matriz:"))

matriz=[ ]

for i in range(n):
    fila=[ ]
    for z in range(n):
        if z ==0:
            fila.append(1)
        else:
            fila.append(fila[z-1]+(z+1))
    matriz.append(fila)

for fila in matriz:
    print(fila)