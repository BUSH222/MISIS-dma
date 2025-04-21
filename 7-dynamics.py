# 1 - Наибольшая возрастающая подпоследовательность
def biggest_subsequence(arr, n):
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# n = int(input())
# arr = list(map(int, input().split()))
# print(biggest_subsequence(arr, n))


# 2 - Количество разбиений числа

def count_partitions(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j]

    return dp[n][n]


# print(count_partitions(int(input())))


# 3 - Максимальная сумма пути

def max_path_sum(n, arr):
    if n == 1:
        return arr[0]
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, n):
        dp[i] = arr[i] + max(dp[i - 1], dp[i - 2])
    return dp[-1]


n = int(input())
arr = list(map(int, input().split()))
print(max_path_sum(n, arr))
