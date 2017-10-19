# Given a nested list of integers, returns  the sum of all integers in the list weighted by their depth
# For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
# Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)


def reverse_depth_sum(input, level, sum):

    for i in range(len(input)):
        if type(input[i]) is list:
            sum = reverse_depth_sum(input[i], level + 1, sum)
        else:
            sum += (input[i] * level)

    return sum


input = [[1, 1], 2, [1, 1]]
assert reverse_depth_sum(input, 1, 0) == 10
assert reverse_depth_sum([1,[4, [6]]] , 1, 0) == 27
