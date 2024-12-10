from gcd_ex import gcd_ex
from phi import phi


def mod_exp(base, exp, mod):
    mod_result = 1

    while exp > 0:

        if exp % 2 == 1:
            mod_result = (mod_result * base) % mod

        base = (base * base) % mod
        exp -= 1

    return mod_result


def inverse_element_2(operand_a, operand_n):
    if operand_a <= 0 or operand_n <= 0:
        print("Operands must be positive integers.")
        exit(-1)

    if operand_a >= operand_n:
        operand_a %= operand_n

    gcd, x, y = gcd_ex(operand_a, operand_n)

    if gcd != 1:
        print(f"No multiplicative inverse exists for {operand_a} % {operand_n} "
              f"where gcd({operand_a}, {operand_n}) != 1")

        exit(-1)

    # Check if n is prime
    is_prime = all(operand_n % i != 0 for i in range(2, int(operand_n ** 0.5) + 1))

    if is_prime:
        # Use Fermat's Theorem
        return mod_exp(operand_a, operand_n - 2, operand_n)

    else:
        # Use Euler's Theorem
        return mod_exp(operand_a, phi(operand_n) - 1, operand_n)


if __name__ == '__main__':
    a, n = 5, 18
    result = inverse_element_2(a, n)
    print(f"The multiplicative inverse: {a}^{a} % {n} = {result}")
