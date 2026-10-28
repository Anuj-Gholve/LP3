# Experiment A1: Recursive and non-recursive Fibonacci series
# Time complexity: iterative O(n); recursive O(n) for this series-building method.
# Space complexity: O(n) to store the series; recursive call stack O(n).

def fibonacci_iterative(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_recursive(n):
    """Build the first n Fibonacci numbers recursively."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = fibonacci_recursive(n - 1)
    if n == 2:
        series.append(1)
    else:
        series.append(series[-1] + series[-2])
    return series


def main():
    try:
        n = int(input("Enter the number of Fibonacci terms: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print("Fibonacci series (iterative):", fibonacci_iterative(n))
    print("Fibonacci series (recursive):", fibonacci_recursive(n))


if __name__ == "__main__":
    main()
