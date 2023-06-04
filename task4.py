# There is an array of numbers - arr [1, 3, 6, 2, 2, 0, 4, 5]
# there is a number target = 5.
# Count the number of pairs in the array, the sum of which will give target


def count_pairs(arr, target):
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count


if __name__ == '__main__':
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5))  # 4
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 7))  # 4
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 8))  # 3
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 9))  # 2
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 10))  # 2
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 11))  # 1
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 12))  # 1
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 13))  # 0
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 14))  # 0
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 15))  # 0
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 16))  # 0
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 17))  # 0
    print(count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 18))  # 0
