import random
from lab_4.gcd_ex import gcd_ex, gcd
from miller_rabin import is_likely_prime


def main():
    print("Generating RSA keys...")
    public_key, private_key = generate_rsa_keys(128)

    print("Public key:", public_key)
    print("Private key:", private_key)
    print()

    # Step 2: Encrypt a message
    message = "Hello World!"
    print("Original:", message)
    ciphertext = rsa_encrypt(message, public_key)
    print("Encrypted:", ciphertext)

    # Step 3: Decrypt the message
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print("Decrypted message:", decrypted_message)


# Function to generate a random prime number of approximately n bits
def generate_large_prime(bits):
    while True:
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_likely_prime(candidate):
            return candidate


# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd_result, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_result, x, y


# Generate RSA keys
def generate_rsa_keys(bits=1024):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # e should equal - gcd(e, phi_n) = 1
    e = 65537
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Compute d, the modular inverse of e mod phi_n
    _, d, _ = gcd_ex(e, phi_n)
    d = d % phi_n
    if d < 0:
        d += phi_n

    return (e, n), (d, n)  # Public and private keys


def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    plaintext_int = int.from_bytes(plaintext.encode('utf-8'), byteorder='big')
    ciphertext = pow(plaintext_int, e, n)
    return ciphertext


def rsa_decrypt(cipher_text, private_key):
    d, n = private_key
    decrypted_int = pow(cipher_text, d, n)
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
    return decrypted_bytes.decode('utf-8')


if __name__ == "__main__":
    main()
