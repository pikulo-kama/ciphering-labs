
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
