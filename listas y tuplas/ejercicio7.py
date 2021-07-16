abc = []
for i in range(26):
    abc.append(
        chr(97+i)
    )

abc.insert(15,'ñ')

toDelete=[]

for word in abc:
    i = abc.index(word)
    if i % 3 == 0:
        toDelete.append(i)

toDelete.reverse()

for i in toDelete:
    abc.pop(i)

print(abc)
