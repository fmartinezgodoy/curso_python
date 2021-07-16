word = input("Ingrese una palabra: ")

vowels = ('a','e','i','o','u')
vowelsCount = [0,0,0,0,0] # a,e,i,o,u

for char in word:
    if char in vowels:
        vowelsCount[
            vowels.index(char)
        ] += 1
    
for vowel in vowels:
    print(
        "La vocal {} aparece {} veces.".format(
            vowel, 
            vowelsCount[vowels.index(vowel)]
        )
    )
