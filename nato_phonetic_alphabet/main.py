import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

phonetic = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# # first approach
# is_word = True
# while is_word:
#     user_input = input("Enter a name: ").upper()
#     try:
#         result = [phonetic[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, numbers are not supported")
#     else:
#         print(result)
#         is_word = False


# another approach
def generate_phonetic():
    user_input = input("Enter a name: ").upper()
    try:
        result = [phonetic[letter] for letter in user_input]
    except KeyError:
        print("Sorry, numbers are not supported")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
