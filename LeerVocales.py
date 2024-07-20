def count_vowels (palabra):
    contador = 0
    for i in range (len(palabra)):
        if palabra[i] in ("aeiouAEIOU"):
            contador += 1
    return (contador)

palabra = input("type a word: ")

print("the number of vowels is:" + str(count_vowels (palabra)))