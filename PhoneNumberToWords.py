
hashtable = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


def print_words_util(number, current_digit, output, n):
    if current_digit == n:
        print(output)
        return

    for i in range(0, len(hashtable[number[current_digit]])):
        output[current_digit] = hashtable[number[current_digit]][i]
        print_words_util(number, current_digit+1, output, n)

        if number[current_digit] == 0 or number[current_digit] == 1:
            return


def print_words(number, n):
    output = {}
    print_words_util(number, 0, output, n)


def main():
    number = [2, 3, 4]
    print_words(number, len(number))


if __name__ == '__main__':
    main()
