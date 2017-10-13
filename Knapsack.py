# recursive
def knapsack(weight, value, capacity, no_of_items):

    if weight == 0 or no_of_items == 0:
        return 0

    if weight[no_of_items - 1] > capacity:
        return knapsack(weight, value, capacity, no_of_items - 1)

    return max(knapsack(weight, value, capacity, no_of_items - 1),
               value[no_of_items -1] + knapsack(weight, value, capacity - weight[no_of_items - 1], no_of_items - 1))


# DP
def knapsack_dp(weight, value, capacity, no_of_items):

    k = []
    for i in range(len(value) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                k.append([])
                k[i].append(0)
            elif weight[i - 1] <= w:
                k[i].append(max(value[i-1] + k[i-1][w-weight[i-1]], k[i-1][w]))
            else:
                k[i].append(k[i-1][w])

    return k[i][w]


value = [100, 60, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack(weights, value, capacity, len(value)))
print(knapsack_dp(weights, value, capacity, len(value)))
