# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way
# until a single-digit number is produced. The input will be a non-negative integer.


def digital_root(n):
    while n > 9:
        n = sum(int(i) for i in str(n))
    return n


if __name__ == '__main__':
    print(digital_root(16))  # 7
    print(digital_root(456))  # 6
    print(digital_root(942))  # 6
    print(digital_root(132189))  # 6
    print(digital_root(493193))  # 2
    print(digital_root(999999999999))  # 9
    print(digital_root(167346))  # 9
    print(digital_root(0))  # 0
    print(digital_root(10))  # 1
    print(digital_root(11))  # 2
    print(digital_root(999999999999))  # 9
