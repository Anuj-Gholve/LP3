# Experiment A4: 0/1 Knapsack using Dynamic Programming
# Prints the DP table and the maximum obtainable value.
# Time complexity: O(n * capacity); space complexity: O(n * capacity).

def knapsack_dp(values, weights, capacity):
    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")
    if any(weight < 0 for weight in weights):
        raise ValueError("Weights cannot be negative.")
    if any(value < 0 for value in values):
        raise ValueError("Values cannot be negative.")

    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value = values[i - 1]
        weight = weights[i - 1]
        for current_capacity in range(capacity + 1):
            # Zero-weight items are supported as well.
            if weight <= current_capacity:
                dp[i][current_capacity] = max(
                    value + dp[i - 1][current_capacity - weight],
                    dp[i - 1][current_capacity]
                )
            else:
                dp[i][current_capacity] = dp[i - 1][current_capacity]

    return dp


def main():
    try:
        n = int(input("Enter number of items: "))
        if n < 0:
            print("Number of items cannot be negative.")
            return

        values, weights = [], []
        for i in range(n):
            values.append(int(input(f"Enter value of item {i + 1}: ")))
            weights.append(int(input(f"Enter weight of item {i + 1}: ")))

        capacity = int(input("Enter knapsack capacity: "))
        dp = knapsack_dp(values, weights, capacity)

    except ValueError as error:
        print("Invalid input:", error)
        return

    print("\nDP Table (rows = items considered, columns = capacity):")
    print("     " + "".join(f"{w:4}" for w in range(capacity + 1)))
    for i, row in enumerate(dp):
        print(f"{i:3}  " + "".join(f"{value:4}" for value in row))

    print("\nMaximum value that can be put in knapsack:", dp[len(values)][capacity])


if __name__ == "__main__":
    main()
