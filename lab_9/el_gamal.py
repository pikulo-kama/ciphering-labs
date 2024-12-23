import random
from lab_8.diffie_hellman_exchange import generate_safe_prime, find_primitive_root


def main():
    p, q = generate_safe_prime()  # Use the function to generate small primes
    g = find_primitive_root(p)

    print(f"Safe prime number p: {p}")
    print(f"Prime number q: {q}")
    print(f"Generator g: {g}")

    # ElGamal Key Generation
    x, h = elgamal_keygen(p, g)
    print(f"Private key x: {x}")
    print(f"Public key h: {h}")

    # Encrypt a message (for simplicity, let's use a small integer as the message)
    m = 15  # Example message
    print(f"Original message m: {m}")

    # ElGamal encryption
    c1, c2 = elgamal_encrypt(p, g, h, m)
    print(f"Ciphertext (c1, c2): ({c1}, {c2})")

    # ElGamal decryption
    decrypted_m = elgamal_decrypt(p, x, c1, c2)
    print(f"Decrypted message: {decrypted_m}")

    assert m == decrypted_m, "Decryption failed! The message doesn't match."


def mod_inverse(a, m):
    """Returns the modular inverse of a under modulo m"""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def elgamal_keygen(p, g):
    """Generate ElGamal public and private keys"""
    # Private key x (random integer between 2 and p-2)
    x = random.randint(2, p - 2)
    # Public key h = g^x mod p
    h = pow(g, x, p)
    return x, h


def elgamal_encrypt(p, g, h, m):
    """Encrypt message m using ElGamal"""
    # Choose a random integer y
    y = random.randint(2, p - 2)
    # c1 = g^y mod p
    c1 = pow(g, y, p)
    # c2 = m * h^y mod p
    c2 = (m * pow(h, y, p)) % p
    return c1, c2


def elgamal_decrypt(p, x, c1, c2):
    """Decrypt the ciphertext (c1, c2) using ElGamal"""
    # Compute m = c2 * (c1^x)^-1 mod p
    c1_x = pow(c1, x, p)
    c1_x_inv = mod_inverse(c1_x, p)
    m = (c2 * c1_x_inv) % p
    return m


if __name__ == '__main__':
    main()
