# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


def fib(n: int, cache: dict = {}) -> int:
    if n in cache:
        return cache[n]

    if n <= 1:
        return 1

    cache[n] = fib (n - 1) + fib (n - 2)
    return cache[n]


def solution():
    n = 0
    sum = 0

    while True:
        fib_n = fib(n)

        if fib_n >= 4_000_000_000:
            break

        print(f"fib({n}) = {fib_n}")

        if fib_n % 2 == 0:
            sum += fib_n

        n += 1

    return sum

if __name__ == "__main__":
    print(f"Solution: {solution()}")