# http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
# https://www.youtube.com/watch?v=s6FhG--P7z0


def subset_sum(input_set, length, sum):

    if sum == 0:
        return True

    if length == 0 and sum != 0:
        return False

    return subset_sum(input_set, length - 1, sum) or subset_sum(input_set, length - 1, sum - input_set[length - 1])


def subset_sum_dp(input_set, sum):
    length = len(input_set)

    L = []

    # L.append([True for i in range(length + 1)])

    for i in range(sum + 1):
        L.append([])
        for j in range(length + 1):

            if i == 0:
                L[i].append(True)
            elif j == 0:
                L[i].append(False)
            else:
                L[i].append(L[i][j - 1])
                if i >= input_set[j-1]:
                    L[i][j] = L[i][j] or L[i - input_set[j-1]][j-1]

    return L[sum][length]


def subset_sum_dp_2_tushar(input_set, sum):
    length = len(input_set)

    L = [[None for j in range(sum + 1)] for i in range(length + 1)]

    for i in range(length + 1):
        for j in range(sum + 1):

            if i == 0:
                L[i][j] = False
            elif j == 0:
                L[i][j] = True
            elif j < input_set[i-1]:
                L[i][j] = L[i-1][j]
            else:
                L[i][j] = L[i-1][j] or L[i-1][j-input_set[i-1]]

    print(L)
    return L[length][sum]


input = [3, 34, 4, 12, 5, 2]
print(subset_sum(input, 6, 17))
print(subset_sum_dp(input, 17))
print(subset_sum_dp_2_tushar(input, 17))

