def search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = int((start + end)/2)

        if arr[mid] == target:
            return mid

        if arr[start] < arr[mid]:
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] < target <= arr[end]:
            start = mid + 1
        else:
            end = mid - 1


arr = [5, 6, 7, 8, 9, 1, 2, 3]
print(search(arr, 3))
