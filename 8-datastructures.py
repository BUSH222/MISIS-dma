# 1 - brackets
from collections import deque


def brackets(s):
    stack = deque()
    brackets = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in brackets.values():
            stack.append(c)
        elif c in brackets.keys():
            if not stack or stack[-1] != brackets[c]:
                return False
            stack.pop()

    return not stack


# print('YES' if brackets(input().strip()) else 'NO')

# 2 - sum of 2 numbers

def sum_of_two_numbers(nums, target):
    seen = []
    for num in nums:
        if target - num in seen:
            return True
        seen.append(num)
    return False

n, k = map(int, input().split())
if n == 0 and k != 0:
    print('NO')
elif n == 0 and k == 0:
    print('YES')
else:
    nums = list(map(int, input().split()))

    print('YES' if sum_of_two_numbers(nums, k) else 'NO')

# 3 - max in a rolling window

result = []
n, k = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(n - k + 1):
    result.append(max(nums[i:i + k]))
print(' '.join(map(str, result)))

# i am showing off
n,k=map(int,input().split());a=list(map(int,input().split()));print(*[max(a[i:i+k])for i in range(n-k+1)])
