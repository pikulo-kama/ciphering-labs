import random


def is_likely_prime(number, round_count=40):

    # Step 1: Handle trivial cases
    if number % 2 == 0:
        return False

    # Step 2: Write p-1 as 2^s * d
    s = 0
    d = number - 1

    while d % 2 == 0:
        d //= 2
        s += 1

    # Step 3: Perform k rounds of testing
    for _ in range(round_count):

        a = random.randint(2, number - 2)  # Random number in range [2, p-2]
        x = pow(a, d, number)  # Compute a^d % p

        if x == 1 or x == number - 1:
            continue

        # Step 4: Check repeated squaring
        composite = True

        for _ in range(s - 1):
            x = pow(x, 2, number)  # x = x^2 % p
            if x == number - 1:
                composite = False
                break

        if composite:
            return False

    # If no rounds failed, p is probably prime
    return True


def get_probability(round_count):
    return 1 - (1 / (2 ** round_count))


if __name__ == '__main__':

    # Input: p (number to test) and k (number of rounds)
    number_to_test = int(input("Enter an odd number (> 3): "))
    number_of_rounds = int(input("Enter the number of rounds: "))

    if number_to_test <= 3:
        print(f"p should be bigger than 3, {number_to_test} was provided.")
        exit(-1)

    if is_likely_prime(number_to_test, number_of_rounds):
        print(f"The number {number_to_test} is probably prime with probability {get_probability(number_of_rounds):.6f}")

    else:
        print(f"The number {number_to_test} is composite.")
