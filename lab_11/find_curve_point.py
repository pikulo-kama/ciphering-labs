from elliptic_curve import modular_sqrt


def main():
    G = (17, 25)

    # Find the order of point G
    order = find_order_of_point(G)
    print("Order of the point G =", order)


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
        lamb = (3 * x_P ** 2 + 1) * modular_sqrt(2 * y_P, p) % p
    else:
        lamb = (y_Q - y_P) * modular_sqrt(x_Q - x_P, p) % p

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


# Function to find the order of a point G
def find_order_of_point(G, p=23):
    n = 1
    current_point = G
    while current_point != (None, None):  # Identity point (O)
        n += 1
        current_point = elliptic_curve_multiply(n, G, p)
        if n > p:  # Break if we exceeded the field size (it's safe to assume the order is smaller)
            break
    return n


if __name__ == '__main__':
    main()
