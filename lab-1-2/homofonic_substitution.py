import random

# Ukrainian alphabet
ukrainian_alphabet = [
    "а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й",
    "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч",
    "ш", "щ", "ь", "ю", "я"
]

# Create a dictionary mapping letters to random numbers
letter_to_number = {}
number_to_letter = {}
used_numbers = set()

# Assign random numbers to letters
for letter in ukrainian_alphabet:
    while True:
        random_number = random.randint(100, 999)  # You can adjust the range of numbers
        if random_number not in used_numbers:
            used_numbers.add(random_number)
            letter_to_number[letter] = random_number
            number_to_letter[random_number] = letter
            break


def encrypt(text):
    """
    Encrypts text into set of three-digit numbers.

    :param text: Text to be encrypted.
    :return: Encrypted text.
    """
    encrypted_text = []

    for character in text:
        if character in letter_to_number:
            # Convert letter to random number
            encrypted_text.append(letter_to_number[character])
        else:
            # Non-alphabet characters are added as they are
            encrypted_text.append(character)

    return "".join([str(digit) for digit in encrypted_text])


def decrypt(text):
    """
    Decrypts text from set of three-digit numbers
    back to original string based on the letter-digit mapping table.

    :param text: Text to be decrypted.
    :return: Decrypted text.
    """
    decrypted_text = ""
    encrypted_text_array = [int(text[i:i + 3]) for i in range(0, len(text), 3)]

    for character in encrypted_text_array:
        if isinstance(character, int):
            decrypted_text += number_to_letter[character]
        else:
            decrypted_text += character

    return decrypted_text


def main():

    text = "привіт"
    encrypted_text = encrypt(text)
    decrypted_text = decrypt(encrypted_text)

    print(f"Original: {text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")


if __name__ == '__main__':
    main()
