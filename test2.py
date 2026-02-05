import math

t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    s = input()

    # Precompute factorials
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    def perm_count(st):
        freq = {}
        for c in st:
            freq[c] = freq.get(c, 0) + 1
        res = fact[n]
        for v in freq.values():
            res //= fact[v]
        return res

    # Initialize with first possible operation (i=0, j=0)
    temp = list(s)
    temp[0] = temp[0]
    best_string = "".join(temp)
    best_value = perm_count(best_string)

    # Try all operations
    for i in range(n):
        for j in range(n):
            temp = list(s)
            temp[i] = temp[j]
            cur = "".join(temp)

            val = perm_count(cur)
            if val < best_value:
                best_value = val
                best_string = cur

    answers.append(best_string)

print("\n".join(answers))
