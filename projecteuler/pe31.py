coinSizes = [1, 2, 5, 10, 20, 50, 100, 200]


def solution(target):
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coinSizes:
        for j in range(coin, target + 1):
            ways[j] += ways[j - coin]

    return ways[len(ways) - 1]


print(solution(2))
