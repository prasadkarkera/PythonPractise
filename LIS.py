# http://www.geeksforgeeks.org/longest-increasing-subsequence/


def lis(arr):
    l = [1]*len(arr)

    for i in range(len(arr)):
        for j in range(0, i):

            if arr[i] > arr[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1

    maximum = 0
    for i in range(len(l)):
        if maximum < l[i]:
            maximum = l[i]

    return maximum


arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
print('Length of lis is ', lis(arr))