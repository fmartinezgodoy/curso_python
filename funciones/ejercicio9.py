def divisores(numero):
    div = []

    for i in range(numero):
        if numero % (i+2) == 0:
            div.append(i+2)

    return div

def multiplos(numero):

    mul = []

    for i in range(100):
        mul.append(numero * i)


    return mul

def dcm(numero1, numero2):

    dcm_final = 0
    check = False

    divisores_n1 = divisores(numero1)
    divisores_n2 = divisores(numero2)

    for i in range(len(divisores_n1)):
        for e in range(len(divisores_n2)):
            if divisores_n1[len(divisores_n1)-i-1] == divisores_n2[len(divisores_n2)-e-1]:
                dcm_final = divisores_n1[len(divisores_n1)-i-1]
                check = True
                break
        if check == True:
            break

    return dcm_final

def mcm(numero1, numero2):

    mcm_final = 0
    check = False

    multiplos_n1 = multiplos(numero1)
    multiplos_n2 = multiplos(numero2)

    for i in range(99):
        for e in range(99):
            if multiplos_n1[i+1] == multiplos_n2[e+1]:
                mcm_final = multiplos_n1[i+1]
                check = True
                break
                print(" Ultima i {}, ultima e {}".format(i,e))
        if check == True:
            break

    return mcm_final


numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

dcm_final = dcm(numero1, numero2)
mcm_final = mcm(numero1, numero2)

print("El dcm es {} y el mcm es {}".format(dcm_final, mcm_final))

