vowels = ["a", "e", "i", "o", "u"]

# a function that finds a vowel with "w" as it arguement
def fv(w, v):
    for i in v:
        for j in w:
            if i in j:
                print(f"{i} is in {w}")


word = str(input("Enter a word: "))
fv(word, vowels)