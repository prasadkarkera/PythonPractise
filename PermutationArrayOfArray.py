def permutations(arrays, i, one_result, final_result):
    if i == len(arrays):
        return None, one_result

    for number in arrays[i]:
        one_result.append(number)
        output, one_result = permutations(arrays, i + 1, one_result, final_result)
        if not output:
            final_result.append(one_result)
            one_result = one_result[:-1]

    one_result = []
    return final_result, one_result


def permutations_of_array(arr):
    return permutations(arr, 0, [], [])


def main():
    arrays = [[1, 2, 3], [4], [5, 6]]
    output, discarded_intermediate = permutations_of_array(arrays)
    print(output)


if __name__ == '__main__':
    main()

