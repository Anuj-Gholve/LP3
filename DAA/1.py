def iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def recursive(n):
    if n <= 1:
        return n
    return recursive(n - 1) + recursive(n - 2)

n = int(input("Enter number of terms: "))

print("Iterative Fibonacci:")
iterative(n)

print("Recursive Fibonacci:")
for i in range(n):
    print(recursive(i), end=" ")

# Iterative: Time O(n), Space O(1)
# Recursive: Time O(2^n), Space O(n)
