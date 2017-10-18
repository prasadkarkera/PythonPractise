# http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/


def edit_distance(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)
    else:
        return 1 + min(edit_distance(str1, str2, m, n-1),  # add
                       edit_distance(str1, str2, m-1, n),  # subtract
                       edit_distance(str1, str2, m-1, n-1))  # replace


def edit_distance_dp(str1, str2):

    m = len(str1)
    n = len(str2)

    L = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                L[i][j] = j

            if j == 0:
                L[i][j] = i

            if str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1]
            else:
                L[i][j] = 1 + min(L[i-1][j], L[i][j-1], L[i-1][j-1])

    return L[i][j]


str1 = 'sunday'
str2 = 'saturday'

print(edit_distance(str1, str2, len(str1), len(str2)))
print(edit_distance_dp(str1, str2))
