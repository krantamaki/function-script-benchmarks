from math import ceil, sqrt

limit = 1_000_000
# limit = 10_000

bool_array = [True for i in range(limit + 1)]

for i in range(2, ceil(sqrt(limit)) + 1):
    if bool_array[i]:
        for j in range(i * i, limit + 1, i):
            bool_array[j] = False

primes = [i for i, x in enumerate(bool_array) if x]

# print(len(primes))
