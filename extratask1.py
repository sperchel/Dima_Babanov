# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging
# its digits.


def next_bigger(n):
    n = str(n)
    for i in range(len(n) - 1, 0, -1):
        if n[i] > n[i - 1]:
            return int(n[:i - 1] + n[i] + ''.join(sorted(n[i - 1] + n[i + 1:])))
    return -1


if __name__ == '__main__':
    print(next_bigger(12))  # 21
    print(next_bigger(513))  # 531
    print(next_bigger(2017))  # 2071
    print(next_bigger(414))  # 441
    print(next_bigger(144))  # 414
    print(next_bigger(9))  # -1
    print(next_bigger(111))  # -1
    print(next_bigger(531))  # -1
    print(next_bigger(123456789))  # 123456798
    print(next_bigger(1234567890))  # 1234567908
