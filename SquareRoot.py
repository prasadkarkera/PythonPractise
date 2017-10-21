def get_square_root(number):

    start = 1
    end = number/2

    while abs(start - end) > 0.0000005:
        mid = (start + end)/2

        if mid * mid == number:
            return mid
        elif mid * mid < number:
            start = mid
        else:
            end = mid

    return (start+end)/2


print(get_square_root(20))
