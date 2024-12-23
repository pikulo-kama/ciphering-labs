import string


def main():

    keyword = "SuperSecretKey"
    shift = 3

    text = "Hello world"
    encrypted_text = caesar_cipher(text, keyword, shift, encrypt=True)
    decrypted_text = caesar_cipher(encrypted_text, keyword, shift, encrypt=False)

    print(f"Keyword: {keyword}")
    print(f"Shift: {shift}")
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text.capitalize()}")


def create_keyword_alphabet(keyword):
    """
    Creates a unique alphabet based on the given keyword.

    :param keyword: The keyword to generate the shifted alphabet.
    :return: A string containing the modified alphabet.
    """
    keyword = "".join(dict.fromkeys(keyword.upper()))  # Remove duplicates in keyword
    remaining_letters = "".join([char for char in string.ascii_uppercase if char not in keyword])
    return keyword + remaining_letters


def caesar_cipher(text, keyword, shift, encrypt=True):
    """
    Encrypts or decrypts text using the Caesar cipher with a keyword.

    :param text: The text to be encrypted or decrypted.
    :param keyword: The keyword to generate the modified alphabet.
    :param shift: The number of positions to shift the letters.
    :param encrypt: Whether to encrypt (True) or decrypt (False) the text.
    :return: The encrypted or decrypted text.
    """
    alphabet = string.ascii_uppercase
    shifted_alphabet = create_keyword_alphabet(keyword)

    if not encrypt:
        shift = -shift  # Reverse shift for decryption

    result = []
    for char in text.upper():
        if char in alphabet:
            original_index = shifted_alphabet.index(char)
            new_index = (original_index + shift) % len(alphabet)
            result.append(shifted_alphabet[new_index])
        else:
            result.append(char)  # Keep non-alphabetic characters unchanged

    return "".join(result)


if __name__ == '__main__':
    main()
