from des_helper import (
    hex_to_binary,
    binary_to_decimal,
    binary_to_hex,
    decimal_to_binary,
    xor,
    shift_left
)

from des_matrix import (
    INITIAL_PERMUTATION,
    STR_PERMUTATION,
    FINAL_PERMUTATION,
    KEY_COMPRESSION_TABLE,
    EXP_D,
    S_BOX,
    KEY_PARITY,
    SHIFT_TABLE
)


def permute(key, data_arr, bound):
    permutation = ""

    for i in range(0, bound):
        permutation = permutation + key[data_arr[i] - 1]

    return permutation


def encrypt(pt, rkb):
    pt = hex_to_binary(pt)

    pt = permute(pt, INITIAL_PERMUTATION, 64)

    left = pt[0:32]
    right = pt[32:64]

    for i in range(0, 16):

        right_expanded = permute(right, EXP_D, 48)
        xor_x = xor(right_expanded, rkb[i])
        s_box_str = ""

        for j in range(0, 8):
            row = binary_to_decimal(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = binary_to_decimal(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))

            val = S_BOX[j][row][col]
            s_box_str = s_box_str + decimal_to_binary(val)

        s_box_str = permute(s_box_str, STR_PERMUTATION, 32)

        result = xor(left, s_box_str)
        left = result

        if i != 15:
            left, right = right, left

    combine = left + right

    encrypted_text = permute(combine, FINAL_PERMUTATION, 64)
    return encrypted_text


def main():
    key = "82AABB0C7CDD9136"
    text = "DE23EE14E6ED5EBA"

    # Encode key
    key = hex_to_binary(key)
    key = permute(key, KEY_PARITY, 56)

    left = key[0:28]
    right = key[28:56]

    rkb = []
    rk = []

    for i in range(0, 16):
        # Shifting the bits by nth shifts by checking from shift table
        left = shift_left(left, SHIFT_TABLE[i])
        right = shift_left(right, SHIFT_TABLE[i])

        # Combination of left and right string
        combine_str = left + right

        # Compression of key from 56 to 48 bits
        round_key = permute(combine_str, KEY_COMPRESSION_TABLE, 48)

        rkb.append(round_key)
        rk.append(binary_to_hex(round_key))

    encrypted_text = binary_to_hex(encrypt(text, rkb))

    rkb_revision = rkb[::-1]
    decrypted_text = binary_to_hex(encrypt(encrypted_text, rkb_revision))

    print(f"Original: {text}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")


if __name__ == '__main__':
    main()
