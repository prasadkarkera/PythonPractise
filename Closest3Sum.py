def closest_3_sum(arr, target):

    arr.sort()
    minimum_sum = target

    for i in range(len(arr) - 2):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == target:
                return arr[i], arr[j], arr[k]
            elif sum > target:
                k -= 1
            else:
                j += 1

            if target - sum < minimum_sum:
                minimum_sum = target - sum
                tuple = arr[i], arr[j], arr[k]

    return tuple


arr = [1, 5, 7, 2, 9, 4]
print(closest_3_sum(arr, 24))
