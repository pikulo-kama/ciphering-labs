import string


def main():
    secret_key = "SuperSecretKey"
    text = "Hello World"

    encrypted = encrypt(text, secret_key)

    print(f"Secret: {secret_key}")
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")


def encrypt(text, key):
    """
    Encrypts a given plaintext using a matrix-based cipher and a keyword.

    The function creates a matrix from the keyword, prepares the input text
    by splitting it into digraphs (pairs of letters), and then encrypts the
    text using the Playfair cipher rules:
        - If the two letters are in the same row, they are replaced with the
          letters to their immediate right (wrapping around if necessary).
        - If the two letters are in the same column, they are replaced with
          the letters immediately below them (wrapping around if necessary).
        - If the two letters form a rectangle, they are replaced by the
          letters on the same row but in the opposite corners of the rectangle.

    :param text: The plaintext to be encrypted. Should only contain alphabetic characters.
    :param key: The keyword used to generate the cipher matrix.
    :return: The encrypted ciphertext as a string.
    """
    text = text.replace(" ", "")
    encrypted_text = ""

    matrix = create_matrix(key)
    pairs = prepare_text(text)

    for pair in pairs:
        encrypted_text += encrypt_pair(pair, matrix)

    return encrypted_text


def create_matrix(key):
    """
    Creates a matrix for encryption using a keyword.

    The matrix is filled with letters of the alphabet based on the keyword.
    The letters of the keyword are added first, avoiding duplicates, followed
    by the remaining letters of the alphabet that are not in the keyword.
    For a standard Latin alphabet, the letter "J" is typically excluded to
    fit into a 5x5 grid.

    :param key: The keyword used to generate the matrix.

    :return: A 5x5 matrix (list of lists) containing
    the letters for the cipher.
    """
    alphabet = string.ascii_uppercase.replace("J", "")
    key = "".join(dict.fromkeys(key.upper() + alphabet))  # Unique symbols
    matrix = [list(key[i:i + 5]) for i in range(0, 25, 5)]

    return matrix


def prepare_text(text):
    """
    Prepares the input text for encryption by splitting it into digraphs (pairs of letters)
    and handling special cases such as duplicate letters and odd-length text.

    The function:
        - Converts the text to uppercase.
        - Replaces the letter "J" with "I" (to fit into a 5x5 matrix for Playfair cipher).
        - Splits the text into pairs of letters (digraphs).
        - Adds an "X" between duplicate letters in a pair (e.g., "BALLOON" -> ["BA", "LX", "LO", "ON"]).
        - Adds an "X" at the end if the text has an odd length.

    :param text: The plaintext string to be prepared. Should contain only alphabetic characters.
    :return: A list of string pairs (digraphs) ready for encryption.
    """
    text = text.upper().replace("J", "I")
    result = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            result.append(a + "X")
            i += 1
        else:
            result.append(a + b)
            i += 2
    return result


def find_position(matrix, letter):
    """

    Traverses matrix to find row and column
    of provided letter.

    :param matrix: Matrix where letter should be found
    :param letter: Letter to search for
    :return: a pair of row inder and column index
    """
    for row_idx, row in enumerate(matrix):
        for col_idx, char in enumerate(row):
            if char == letter:
                return row_idx, col_idx

    return None


def encrypt_pair(pair, matrix):
    """
    Encrypts a pair of letters using the Playfair cipher rules.

    The function determines the positions of the two letters in the cipher matrix
    and applies the following rules:
        - If the letters are in the same row, replace each with the letter to
          its immediate right, wrapping around to the start of the row if needed.
        - If the letters are in the same column, replace each with the letter
          immediately below, wrapping around to the top of the column if needed.
        - If the letters form the corners of a rectangle, replace them with the
          letters in the same row but at the opposite corners of the rectangle.

    :param pair: A string containing exactly two letters to encrypt.
    :param matrix: A 5x5 matrix (list of lists) containing the cipher alphabet.
    :return: A string of two encrypted letters.
    """
    first_row, first_column = find_position(matrix, pair[0])
    second_row, second_column = find_position(matrix, pair[1])

    if first_row == second_row:  # Same row
        return matrix[first_row][(first_column + 1) % 5] + matrix[second_row][(second_column + 1) % 5]

    elif first_column == second_column:  # Same column
        return matrix[(first_row + 1) % 5][first_column] + matrix[(second_row + 1) % 5][second_column]

    else:  # Different rows and columns
        return matrix[first_row][second_column] + matrix[second_row][first_column]


if __name__ == '__main__':
    main()
