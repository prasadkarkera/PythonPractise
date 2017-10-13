

def climbingStaircase(n, k, int_output=[], output=[]):
    if n < 0:
        return int_output[:-1], output

    if n == 0:
        print(int_output)
        output.append(int_output)
        return [], output

    for i in range(1, k + 1):
        int_output.append(i)
        int_out, output = climbingStaircase(n - i, k, int_output, output)

        if int_out is not None:
            int_output = int_out

    return None, output


int_output, output = climbingStaircase(4, 2)
print(output)
