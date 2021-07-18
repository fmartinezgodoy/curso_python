userInput = input('Ingrese los pares <palabra>:<traducción> separados por comas: ').split(",")

dict = {}

for pair in userInput:
    [spanish, english] = pair.split(':')
    dict[spanish] = english

phrase = input('Ingrese una frase en español: ')

traduction = ""
for word in phrase.split():
    if word in dict:
        traduction += "{} ".format(dict[word])
    else:
        traduction += "[] "
        
print(traduction)
