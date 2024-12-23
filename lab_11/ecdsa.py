# Function to calculate (x^3 + x + 1) mod 23
def elliptic_curve_function(x, p=23):
    return (x ** 3 + x + 1) % p


# Function to check if a number is a quadratic residue modulo p
def is_quadratic_residue(n, p):
    return pow(n, (p - 1) // 2, p) == 1


# Function to compute the square root modulo p (using Tonelli-Shanks algorithm)
def modular_sqrt(n, p):
    """Return the square root of n modulo p if one exists."""
    if not is_quadratic_residue(n, p):
        return None  # No square root exists

    # Tonelli-Shanks Algorithm to find the square root of n modulo p
    if p == 2:
        return n % 2
    elif pow(p, -1, 4) == 3:  # Case where p ≡ 3 (mod 4)
        return pow(n, (p + 1) // 4, p)
    else:
        # Tonelli-Shanks algorithm implementation for general case
        q = p - 1
        s = 0
        while q % 2 == 0:
            q //= 2
            s += 1
        z = 2
        while is_quadratic_residue(z, p):
            z += 1
        m = s
        c = pow(z, q, p)
        t = pow(n, q, p)
        r = pow(n, (q + 1) // 2, p)
        while t != 0 and t != 1:
            t2i = t
            i = 0
            for i in range(1, m):
                t2i = pow(t2i, 2, p)
                if t2i == 1:
                    break
            b = pow(c, 2 ** (m - i - 1), p)
            m = i
            c = b
            t = (t * b) % p
            r = (r * b) % p
        return r if t == 1 else None


# Function to add two points on the elliptic curve
def elliptic_curve_add(P, Q, p=23):
    if P == (None, None):  # Point at infinity
        return Q
    if Q == (None, None):  # Point at infinity
        return P

    x_P, y_P = P
    x_Q, y_Q = Q

    # Point Doubling (P == Q)
    if P == Q:
        numerator = (3 * x_P ** 2 + 1) % p
        denominator = (2 * y_P) % p
        denominator_inv = pow(denominator, -1, p)  # Inverse of the denominator modulo p
        lamb = (numerator * denominator_inv) % p
    else:
        # Point Addition (P != Q)
        if x_P == x_Q:
            return (None, None)  # If x_P == x_Q and y_P != y_Q, return the point at infinity
        numerator = (y_Q - y_P) % p
        denominator = (x_Q - x_P) % p
        denominator_inv = pow(denominator, -1, p)  # Inverse of the denominator modulo p
        lamb = (numerator * denominator_inv) % p

    x_R = (lamb ** 2 - x_P - x_Q) % p
    y_R = (lamb * (x_P - x_R) - y_P) % p

    return (x_R, y_R)


# Function to compute n*G on the elliptic curve
def elliptic_curve_multiply(n, G, p=23):
    result = (None, None)  # Identity point (point at infinity)
    addend = G

    while n > 0:
        if n % 2 == 1:
            result = elliptic_curve_add(result, addend, p)
        addend = elliptic_curve_add(addend, addend, p)
        n //= 2

    return result


# Function to generate keys (private key d, public key Q)
def generate_keys(p=23):
    d = 5  # Private key, can be chosen randomly
    G = (17, 20)  # Generator point G
    Q = elliptic_curve_multiply(d, G, p)  # Public key Q = d * G
    return d, Q


# Function for Elliptic Curve ElGamal Encryption
def elgamal_encrypt(message, Q, p=23):
    # Step 1: Choose a random integer k (secret) and compute C1 = k * G
    k = 3  # Random number chosen for encryption
    G = (17, 20)  # Generator point G
    C1 = elliptic_curve_multiply(k, G, p)

    # Step 2: Compute C2 = M + k * Q (M is the message point)
    M = message  # Message point (can map message to curve)
    C2 = elliptic_curve_add(M, elliptic_curve_multiply(k, Q, p), p)

    return C1, C2


# Function for Elliptic Curve ElGamal Decryption
def elgamal_decrypt(C1, C2, d, p=23):
    # Step 1: Compute d * C1
    dC1 = elliptic_curve_multiply(d, C1, p)

    # Step 2: Compute the inverse of d * C1 and subtract from C2
    dC1_inv = elliptic_curve_multiply(-d, C1, p)  # Using -d for inverse
    M = elliptic_curve_add(C2, dC1_inv, p)  # M = C2 - d * C1

    return M


# Test the ElGamal Encryption and Decryption
private_key, public_key = generate_keys()

# Message point (17, 20) is used as an example message (this can be mapped to any valid point)
message_point = (17, 20)

# Encrypt the message
C1, C2 = elgamal_encrypt(message_point, public_key)

# Decrypt the message
decrypted_message = elgamal_decrypt(C1, C2, private_key)

print(f"Encrypted C1: {C1}")
print(f"Encrypted C2: {C2}")
print(f"Decrypted message: {decrypted_message}")
