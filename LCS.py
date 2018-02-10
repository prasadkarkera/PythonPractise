# http://www.geeksforgeeks.org/longest-common-subsequence/

def lcs(word1, word2):
    m = len(word1)
    n = len(word2)

    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                L[i][j] = 0
            elif word1[i-1] == word2[j-1]:
                L[i][j] = 1 + L[i - 1][j - 1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[i][j]


X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))

