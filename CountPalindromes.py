# http://www.geeksforgeeks.org/count-palindromic-subsequence-given-string/


def count_palindromes(input_str, i, j):

    if i < 0 or j < 0 or i >= len(input_str):
        return 0

    if i == j:
        return 1

    if input_str[i] == input_str[j]:
        return count_palindromes(input_str, i + 1, j) + count_palindromes(input_str, i, j - 1) + 1

    else:
        return count_palindromes(input_str, i, j - 1) + \
           count_palindromes(input_str, i + 1, j) - \
           count_palindromes(input_str, i + 1, j - 1)


print(count_palindromes('abc', 0, 2))