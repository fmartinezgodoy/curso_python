list = []
for i in range(10):
    list.append(i+1)

list.reverse()

for num in list:
    print("{}".format(num), end=", ")
