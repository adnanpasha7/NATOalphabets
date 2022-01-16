import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    word = input("Enter a word: ").upper()
    try:
        output = [dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate()
    else:
        print(output)
generate()