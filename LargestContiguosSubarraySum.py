# http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


def largest_contiguous_sum(arr):
    length = len(arr)

    if length < 1:
        return 0

    current_max = arr[0]
    global_max = arr[0]

    for i in range(1, length):
        current_max = max(arr[i], current_max + arr[i])
        global_max = max(current_max, global_max)

    return global_max


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(f'Maximum contiguous sum is {largest_contiguous_sum(a)}')

a = [-2, -3, -4, -5, -1, -5, -7, -3]
print(f'Maximum contiguous sum is {largest_contiguous_sum(a)}')

a = [1, 2, 4, 9]
print(f'Maximum contiguous sum is {largest_contiguous_sum(a)}')