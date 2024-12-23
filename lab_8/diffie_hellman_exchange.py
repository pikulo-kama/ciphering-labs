import random
from lab_5.miller_rabin import is_likely_prime


def main():
    p, q = generate_safe_prime()  # Use the function to generate small primes
    g = find_primitive_root(p)

    print(f"Safe prime number p: {p}")
    print(f"Prime number q: {q}")
    print(f"Generator g: {g}")

    # Perform Diffie-Hellman key exchange
    shared_secret = diffie_hellman_exchange(p, g)
    print(f"Shared secret: {shared_secret}")


# Generate a safe prime p where p = 2q + 1, and q is prime
def generate_safe_prime():
    """Generates a small safe prime number p where p = 2q + 1 and q is also prime"""
    while True:
        q = random.randint(2, 100)  # Choose a small q
        if is_likely_prime(q, round_count=5):
            p = 2 * q + 1
            if is_likely_prime(p, round_count=5):
                return p, q


# Function to find a primitive root (generator) g for the group Z_p
def find_primitive_root(p):
    """Find a primitive root modulo p"""
    # Check for the existence of a primitive root by testing all numbers from 2 to p-1
    for g in range(2, p):
        # Check if g is a primitive root (it is if g^k mod p != 1 for all k < p-1)
        if all(pow(g, (p - 1) // d, p) != 1 for d in get_factors(p - 1)):
            return g
    return -1  # If no primitive root is found (which should be very unlikely)


# Function to get the factors of a number n (needed for primitive root check)
def get_factors(n):
    """Returns the factors of n"""
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


# Diffie-Hellman key exchange function
def diffie_hellman_exchange(p, g):
    # Generate private keys for two users
    private_a = random.randint(2, p - 2)  # User 1's private key
    private_b = random.randint(2, p - 2)  # User 2's private key

    # Compute public keys (A = g^a % p, B = g^b % p)
    public_a = pow(g, private_a, p)
    public_b = pow(g, private_b, p)

    # Exchange public keys (A and B) and compute the shared secret
    shared_secret_1 = pow(public_b, private_a, p)  # User 1 computes shared secret
    shared_secret_2 = pow(public_a, private_b, p)  # User 2 computes shared secret

    # Check if both users compute the same shared secret
    assert shared_secret_1 == shared_secret_2, "The secrets do not match!"

    return shared_secret_1


if __name__ == '__main__':
    main()
