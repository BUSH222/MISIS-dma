# n1
# TEST - lower_bound_tests.zip


def n1():
    _, x = map(int, input().split())
    a = list(map(int, input().split()))

    left, right = 0, len(a) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
    print(result)


# n2
# TEST - nearest_element_tests.zip

def n2():
    _, x = map(int, input().split())
    a = list(map(int, input().split()))

    left, right = 0, len(a) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            result = mid
            right = mid - 1

    if a[result-1] == x or abs(a[result-1]-x) == abs(a[result]-x):
        print(result-1)
    else:
        print(result)


# n3
# TEST - peak_tests.zip


def n3():
    input()
    a = list(map(int, input().split()))

    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if a[mid] > a[left]:
            left = mid
        else:
            right = mid - 1
    print(left)


n3()

# n4
# TEST - logistics_tests_fixed.zip


def n4():
    pass
