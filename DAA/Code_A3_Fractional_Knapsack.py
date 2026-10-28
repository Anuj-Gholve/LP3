# Experiment A3: Fractional Knapsack using a greedy algorithm
# Time complexity: O(n log n) due to sorting.
# Space complexity: O(n) to store the items.

def fractional_knapsack(items, capacity):
    """
    items is a list of (value, weight) pairs.
    Returns (maximum_value, selected_items), where selected_items contains
    (value, weight, fraction_taken).
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")
    for value, weight in items:
        if value < 0:
            raise ValueError("Item values cannot be negative.")
        if weight <= 0:
            raise ValueError("Every item must have a positive weight.")

    # Sort by descending value-to-weight ratio.
    sorted_items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)
    remaining = capacity
    total_value = 0.0
    selected = []

    for value, weight in sorted_items:
        if remaining <= 0:
            break
        fraction = min(1.0, remaining / weight)
        if fraction > 0:
            selected.append((value, weight, fraction))
            total_value += value * fraction
            remaining -= weight * fraction

    return total_value, selected


def main():
    try:
        n = int(input("Enter number of items: "))
        if n < 0:
            print("Number of items cannot be negative.")
            return

        items = []
        for i in range(n):
            value = float(input(f"Enter value of item {i + 1}: "))
            weight = float(input(f"Enter weight of item {i + 1}: "))
            items.append((value, weight))

        capacity = float(input("Enter knapsack capacity: "))
        maximum_value, selected = fractional_knapsack(items, capacity)

    except ValueError as error:
        print("Invalid input:", error)
        return

    print("\nItems taken (value, weight, fraction taken):")
    for value, weight, fraction in selected:
        print(f"Value={value:g}, Weight={weight:g}, Fraction={fraction:.4f}")
    print(f"Maximum total value in knapsack: {maximum_value:.2f}")


if __name__ == "__main__":
    main()
