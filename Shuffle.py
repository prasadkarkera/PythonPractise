import random


def shuffle(arr):
    length = len(arr)

    for i in range(length - 1, 0, -1):

        j = random.randint(0, i)

        arr[i], arr[j] = arr[j], arr[i]

    return arr

output = shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(output)