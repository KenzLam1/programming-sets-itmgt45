'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    # Returns space
    if letter == " ":
        return " "
    # Converts letter to its ASCII number
    base= ord('A')
    letter_code = ord(letter) - base
    # Apply the shift (%26 to wrap around the alphabet)
    shift_amt = shift % 26
    new_code = (letter_code + shift_amt) % 26
    # Convert back to a character
    return chr(base + new_code)

def caesar_cipher(message, shift):
    new_message = ""
    for char in message:
        if char == " ":
            new_message += " "
        else:
            new_message += shift_letter(char, shift)
    return new_message

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    # Convert letter_shift to its corresponding shift amount
    shift_amt = ord(letter_shift) - ord('A') 
    return shift_letter(letter, shift_amt)

def vigenere_cipher(message, key):
    result = ""
    key_index = 0
    key_len = len(key)
    for char in message:
        shift_amt = ord(key[key_index % key_len]) - ord("A")
        if char == " ":
            result += " "
        else:
            result += shift_letter(char, shift_amt)
        key_index += 1
    return result

def scytale_cipher(message, shift):
    # Pad message with underscores if needed
    length = len(message)
    rem = length % shift
    if rem != 0:
        to_add = shift - rem
        message = message + ("_" * to_add)
        length = len(message)
    # Number of rows after wrapping around the scytale
    rows = length // shift
    # Build the encoded message
    encoded = ""
    for i in range(length):
        source_index = (i // shift) + rows * (i % shift)
        encoded += message[source_index]
    return encoded

def scytale_decipher(message, shift):
    length = len(message)
    rows = length // shift

    decoded_chars = ["?"] * length # placeholder list

    for j in range(length):
        a = j % rows
        b = j // rows
        i = a * shift + b
        decoded_chars[j] = message[i]

    # Join the list back into a string
    decoded = "".join(decoded_chars)
    return decoded  

