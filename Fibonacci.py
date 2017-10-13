def fibonacci(n):
    prev = 0
    current = 1

    for i in range(2, n):
        next = prev + current
        prev = current
        current = next

    return next


def main():
    output = fibonacci(10)
    print(output)


if __name__ == '__main__':
    main()


