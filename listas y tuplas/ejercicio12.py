ma = []
maf0 = [1, 2, 3]
maf1 = [4, 5, 6]
ma.append(maf0)
ma.append(maf1)

mb = []
mbf0 = [-1, 0]
mbf1 = [0, 1]
mbf2 = [1, 1]
mb.append(mbf0)
mb.append(mbf1)
mb.append(mbf2)

mc = []
mcf1 = [0, 0]
mcf2 = [0, 0]
mc.append(mcf1)
mc.append(mcf2)

for a in range(2):
    if a == 0:
        fa = 1
    else:
        fa = -1
    suma = 0
    suma2 = 0
    for b in range(3):
        suma = suma + ma[a][b] * mb[b][a]
        suma2 = suma2 + ma[a + fa][b] * mb[b][a]
    mc[a][a] = suma
    mc[a+fa][a] = suma2

print(mc)




















