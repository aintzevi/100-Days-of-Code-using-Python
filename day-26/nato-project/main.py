import pandas

# Create a dictionary of the phonetic alphabet
data = pandas.read_csv ('nato_phonetic_alphabet.csv')

phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Give your word: ").upper()

phonetic_code_words = [phonetic_alphabet[letter] for letter in input_word]
print(phonetic_code_words)
