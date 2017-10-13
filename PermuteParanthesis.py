str = []


def _print_parenthesis(pos, n, open, close):
    global str
    if close == n:
        print(str)
        return
    else:
        if open > close:
            str[pos] = '}'
            _print_parenthesis(pos + 1, n, open, close+1)

        if open < n:
            str[pos] = '{'
            _print_parenthesis(pos + 1, n, open + 1, close)


def print_parenthesis(n):
    _print_parenthesis(0, n, 0 , 0)


def main():
    global str
    str = [None] * 3 * 2
    print_parenthesis(3)


if __name__ == '__main__':
    main()


