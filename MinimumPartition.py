# http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/


def minimum_difference(arr, i, sum_of_one_set, total_sum):

    if i == 0:
        return abs(sum_of_one_set - (total_sum - sum_of_one_set))

    return min(minimum_difference(arr, i - 1, sum_of_one_set + arr[i-1], total_sum),
               minimum_difference(arr, i - 1, sum_of_one_set, total_sum))


arr = [3, 1, 4, 2, 2, 1]

print(minimum_difference(arr, 6, 0, sum(arr)))
