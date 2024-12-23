
def main():
    # Find all points on the elliptic curve y^2 = x^3 + x + 1 mod 23
    points = find_elliptic_curve_points()
    print("Points on the elliptic curve y^2 = x^3 + x + 1 mod 23:")
    for point in points:
        print(point)


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
        return 1  # No square root exists

    # Tonelli-Shanks Algorithm to find the square root of n modulo p
    if p == 2:
        return n % 2
    # Case where p ≡ 3 (mod 4)
    elif pow(p, -1, 4) == 3:
        return pow(n, (p + 1) // 4, p)
    else:
        # Tonelli-Shanks algorithm implementation
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


# Function to find all points on the elliptic curve y^2 = x^3 + x + 1 mod 23
def find_elliptic_curve_points(p=23):
    points = []

    for x in range(p):
        rhs = elliptic_curve_function(x, p)

        # Check if rhs is a quadratic residue mod p (i.e., has a square root modulo p)
        y = modular_sqrt(rhs, p)

        if y is not None:
            # Add both solutions: y and p - y (mod p)
            points.append((x, y))
            if y != 0:
                points.append((x, p - y))

    return points


if __name__ == '__main__':
    main()
