
def phi(operand_m):
    result = operand_m
    p = 2

    while p * p <= operand_m:

        # Check if p is a factor of m
        if operand_m % p == 0:

            # Remove all occurrences of p from m
            while operand_m % p == 0:
                operand_m //= p

            # Apply the formula
            result -= result // p

        p += 1

    # If m > 1, it is a prime factor
    if operand_m > 1:
        result -= result // operand_m

    return result


if __name__ == '__main__':
    test_data = [9, 18, 13]

    for m in test_data:
        print(f"phi({m}) = {phi(m)}")
