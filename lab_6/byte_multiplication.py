from galois_multiplication import mul02


def main():

    # Test example: 57 * 83 = C1
    a = 0x57
    b = 0x83
    expected = 0xC1

    result = byte_multiplication(a, b)

    print(f"{a:02X} * {b:02X} = {result:02X}, "
          f"Expected: {expected:02X}, "
          f"Test: {'PASS' if result == expected else 'FAIL'}")


def byte_multiplication(a, b):
    """
    Multiply two bytes a and b in GF(2^8) using modular reduction.
    """
    result = 0  # Initialize the result

    for _ in range(8):  # Iterate through 8 bits of 'a'
        if a & 1:  # If the least significant bit of 'a' is set
            result ^= b  # Add 'b' to the result (XOR)

        # Shift 'b' left is necessary
        b = mul02(b)

        # Shift 'a' right to process the next bit
        a >>= 1

    return result & 0xFF  # Return the result as a byte (8 bits)


if __name__ == '__main__':
    main()
