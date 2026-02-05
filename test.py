def is_composite(x):
    if x < 4:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False


t = int(input())
results = []

for _ in range(t):
    n = int(input())

    if n <= 4:
        results.append("-1")
        continue

    evens = [i for i in range(2, n + 1, 2)]
    odds = [i for i in range(1, n + 1, 2)]

    last_even = evens[-1]

    chosen_odd = None
    for o in odds:
        if is_composite(last_even + o):
            chosen_odd = o
            break

    odds.remove(chosen_odd)

    permutation = evens + [chosen_odd] + odds
    results.append(" ".join(map(str, permutation)))


print("\n".join(results))
