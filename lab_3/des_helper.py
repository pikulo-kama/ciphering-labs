
def hex_to_binary(string):
    mapping_table = {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111"
    }

    binary_string = ""

    for i in range(len(string)):
        binary_string = binary_string + mapping_table[string[i]]

    return binary_string


def binary_to_hex(string):
    mapping_table = {
        "0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1110": 'E',
        "1111": 'F'
    }

    hex_string = ""
    for i in range(0, len(string), 4):

        character = ""

        character = character + string[i]
        character = character + string[i + 1]
        character = character + string[i + 2]
        character = character + string[i + 3]

        hex_string = hex_string + mapping_table[character]

    return hex_string


def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0

    while binary != 0:
        dec = binary % 10

        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return decimal


def decimal_to_binary(decimal):

    res = bin(decimal).replace("0b", "")

    if len(res) % 4 != 0:

        div = len(res) / 4
        div = int(div)

        counter = (4 * (div + 1)) - len(res)

        for i in range(0, counter):
            res = '0' + res

    return res


def shift_left(k, nth_shifts):
    s = ""

    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""

    return k


def xor(a, b):
    ans = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans
