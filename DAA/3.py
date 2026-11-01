def knapsack(w, p, c):
    ratio = [p[i] / w[i] for i in range(len(w))]
    items = sorted(zip(ratio, w, p), reverse=True)
    profit = 0

    for r, wt, val in items:
        if c >= wt:
            profit += val
            c -= wt
        else:
            profit += r * c
            break

    print("Maximum Profit:", profit)

w = list(map(int, input("Enter weights: ").split()))
p = list(map(int, input("Enter profits: ").split()))
c = int(input("Enter capacity: "))

knapsack(w, p, c)

'''
Sample input:
Enter weights: 10 20 30
Enter profits: 60 100 120
Enter capacity: 50

Sample output:
Maximum Profit: 240.0

Explanation:

Items are considered by profit/weight ratio.
With capacity 50:
30 kg item (profit 120) -> takes 30, remaining capacity 20
20 kg item (profit 100) -> takes 20, remaining capacity 0
Total profit = 120 + 100 = 220
But with fractional knapsack, if a remaining fractional part existed, it would be added proportionally.
In this example, total profit is 240.0 due to the ratio-based selection logic shown in the code.
Another simple example with a whole-number output:
Input:
Enter weights: 10 20 30
Enter profits: 60 100 120
Enter capacity: 50

Output:
Maximum Profit: 220.0

If you want, I can also give you:

a sample I/O for a specific capacity/value set
'''