

def main():

    examples = [
        (0xD4, 0x02, 0xB3),  # D4 * 02 = B3
        (0xBF, 0x03, 0xDA),  # BF * 03 = DA
    ]

    for value, multiplier, expected in examples:

        if multiplier == 0x02:
            result = mul02(value)

        elif multiplier == 0x03:
            result = mul03(value)

        else:
            continue

        print(
            f"{value:02X} * {multiplier:02X} = {result:02X}, "
            f"Expected: {expected:02X}, "
            f"Test: {'PASS' if result == expected else 'FAIL'}"
        )


def mul02(byte):
    """
    Multiply a byte by 02 in GF(2^8) using bit shifting and XOR.
    """
    byte <<= 1  # Shift left (multiply by x)

    if byte & 0x100:  # Check if the 8th bit is set (carry)
        byte ^= 0x1B  # Reduce modulo m(x) = 0x1B

    return byte & 0xFF  # Ensure the result is a byte


def mul03(byte):
    """
    Multiply a byte by 03 in GF(2^8).
    This is equivalent to: mul03(byte) = mul02(byte) XOR byte.
    """
    return mul02(byte) ^ byte


if __name__ == '__main__':
    main()
