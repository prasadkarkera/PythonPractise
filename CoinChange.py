# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

def count_solutions(coins, no_of_coins, total_sum):

    if total_sum == 0:
        return 1

    if total_sum < 0:
        return 0

    if no_of_coins <= 0 and total_sum >= 1:
        return 0

    return count_solutions(coins, no_of_coins - 1, total_sum) + \
           count_solutions(coins, no_of_coins, total_sum - coins[no_of_coins - 1])


coins = [1, 2, 3];
print(count_solutions(coins, len(coins), 4))