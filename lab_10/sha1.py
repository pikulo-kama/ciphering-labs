import struct


def main():
    message = b"Hello, World!"
    hash_value = sha1(message)

    print(f"SHA-1 Hash: {hash_value}")


def rotate_left(n, b):
    return ((n << b) & 0xFFFFFFFF) | (n >> (32 - b))


def pad_message(message):
    message_len = len(message) * 8  # Length in bits
    message += b'\x80'  # Append 1 followed by zeros
    while len(message) % 64 != 56:
        message += b'\x00'  # Padding with 0s
    message += struct.pack('>Q', message_len)  # Append the original length in bits
    return message


def sha1(message):
    # Initialize variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Pad the message
    message = pad_message(message)

    # Process the message in 512-bit (64-byte) chunks
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]

        # Break the chunk into 16 32-bit words
        w = list(struct.unpack('>16I', chunk))

        # Extend the 16 32-bit words into 80 32-bit words
        for t in range(16, 80):
            w.append(rotate_left(w[t - 3] ^ w[t - 8] ^ w[t - 14] ^ w[t - 16], 1))

        # Initialize the working variables
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for t in range(80):
            if 0 <= t <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= t <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= t <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            # Update the working variables
            temp = (rotate_left(a, 5) + f + e + w[t] + k) & 0xFFFFFFFF
            e = d
            d = c
            c = rotate_left(b, 30)
            b = a
            a = temp

        # Update the hash values
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Return the final hash as a 160-bit (20-byte) hex string
    return struct.pack('>5I', h0, h1, h2, h3, h4).hex()


if __name__ == '__main__':
    main()
