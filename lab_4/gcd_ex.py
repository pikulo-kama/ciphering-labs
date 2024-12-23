

def gcd(operand_a, operand_b):

    gcd_result = None
    smaller = operand_b if operand_a > operand_b else operand_a

    for i in range(1, smaller + 1):

        if operand_a % i == 0 and operand_b % i == 0:
            gcd_result = i

    return gcd_result


def gcd_ex(operand_a, operand_b):

    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while operand_b != 0:

        # Perform integer division
        q, r = divmod(operand_a, operand_b)

        # Update a and b
        operand_a, operand_b = operand_b, r

        # Update x and y
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    # At this point, operand_a is the GCD
    return operand_a, x0, y0


if __name__ == '__main__':

    a, b = 612, 342
    gcd, x, y = gcd_ex(a, b)

    print(f"a={a}, b={b}")
    print(f"gcd={gcd}, x={x}, y={y}")
