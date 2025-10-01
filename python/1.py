# https://projecteuler.net/problem=1

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#       3,       6,       9
#             5,           , 10
# 3 + 6 + 9 + 5 + 10 = 33
def solution():
    N = 1_000
    soma = 0

    for i in range(N):
        if (i % 3 == 0) or (i % 5 == 0):
            soma += i

    return soma


if __name__ == "__main__":
    answer = solution()
    print(answer)
