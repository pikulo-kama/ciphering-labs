from lab_6.byte_multiplication import byte_multiplication as byte_mult


RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def main():

    plaintext = [0x00, 0x00, 0x01, 0x01, 0x03, 0x03, 0x07, 0x07, 0x0f, 0x0f, 0x1f, 0x1f, 0x3f, 0x3f, 0x7f, 0x7f]
    key = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    ciphertext = aes_encrypt(plaintext, key)

    print("Ciphertext:", [f"{byte:02X}" for byte in ciphertext])


def sub_byte(byte):
    """
    Compute SubBytes transformation for a single byte using the AES S-Box.
    """
    # Inverse in GF(2^8)
    if byte == 0:
        inverse = 0

    else:
        inverse = 1

        for _ in range(254):
            inverse = byte_mult(inverse, byte)

    # Affine transformation
    affine = inverse

    for i in range(5):
        affine ^= (inverse >> i) & 0xFF

    return affine ^ 0x63


# AES transformations
def sub_bytes(state):
    """
    Apply the SubBytes transformation to the state.
    """
    return [[sub_byte(byte) for byte in row] for row in state]


def shift_rows(state):
    """
    Apply the ShiftRows transformation to the state.
    """
    return [
        state[0],
        state[1][1:] + state[1][:1],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3],
    ]


def mix_columns(state):
    """
    Apply the MixColumns transformation to the state.
    """
    def mix_column(column):
        return [
            byte_mult(column[0], 2) ^ byte_mult(column[1], 3) ^ column[2] ^ column[3],
            column[0] ^ byte_mult(column[1], 2) ^ byte_mult(column[2], 3) ^ column[3],
            column[0] ^ column[1] ^ byte_mult(column[2], 2) ^ byte_mult(column[3], 3),
            byte_mult(column[0], 3) ^ column[1] ^ column[2] ^ byte_mult(column[3], 2),
        ]
    return [mix_column(col) for col in zip(*state)]


def add_round_key(state, round_key):
    """
    XOR the state with the round key.
    """
    return [[state[row][col] ^ round_key[row][col] for col in range(4)] for row in range(4)]


def key_expansion(key):
    """
    Perform AES-128 key expansion.
    """
    def rot_word(word):
        return word[1:] + word[:1]

    def sub_word(word):
        return [sub_byte(byte) for byte in word]

    expanded_key = [key[i:i + 4] for i in range(0, 16, 4)]
    for i in range(4, 44):
        temp = expanded_key[i - 1]
        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            temp[0] ^= RCON[i // 4 - 1]
        expanded_key.append([expanded_key[i - 4][j] ^ temp[j] for j in range(4)])
    return [expanded_key[i:i + 4] for i in range(0, 44, 4)]


def aes_encrypt(plaintext, key, rounds=10):
    """
    Encrypt a single 128-bit block using AES-128.
    """
    state = [plaintext[i:i + 4] for i in range(0, 16, 4)]
    round_keys = key_expansion(key)

    state = add_round_key(state, round_keys[0])

    for round in range(1, rounds):

        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[rounds])

    return [byte for row in state for byte in row]


if __name__ == '__main__':
    main()
