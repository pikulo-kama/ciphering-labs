from gcd_ex import gcd_ex


def inverse_element(operand_a, operand_b):
    gcd, x, y = gcd_ex(operand_a, operand_b)

    if gcd != 1:
        print(f"Modular inverse doesn't exist for {operand_a} % {operand_b}")
        exit(-1)

    return x % operand_b


if __name__ == '__main__':
    a = 5
    n = 18

    inverse = inverse_element(a, n)
    print(f"The modular inverse: {a} % {n} = {inverse}")
