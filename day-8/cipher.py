# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = (position + int(shift)) % len(alphabet)
#         cipher_text += alphabet[new_position]
#     print(f"This is the encrypted message: {cipher_text}")
#
# def decrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - int(shift)
#         cipher_text += alphabet[new_position]
#     print(cipher_text)

def ceasar(direction, text, shift):
    end_text = ""

    for char in text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = (position + int(shift)) % len(alphabet)
            elif direction == "decode":
                new_position = (position - int(shift)) % len(alphabet)
            end_text += alphabet[new_position]
    print(end_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

to_continue = True
while to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(direction, text, shift)
    continue_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if continue_choice == "no":
        to_continue = False
        print("Goodbye!")