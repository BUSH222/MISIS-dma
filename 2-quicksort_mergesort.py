# n1
# TEST - quicksort_tests.zip

def quicksort(arr, s, e):
    thing = [(s, e)]

    while thing:
        low, high = thing.pop()
        if low < high:
            pivot_index = rearrange(arr, low, high)
            thing.append((low, pivot_index - 1))
            thing.append((pivot_index + 1, high))


def rearrange(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# N = int(input())
# arr = list(map(int, input().split()))
# quicksort(arr, 0, N - 1)
# print(' '.join(map(str, arr)))


# n2
# TEST - merge_sort.zip


def mergesort(arr, thing, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    mergesort(arr, thing, left, mid)
    mergesort(arr, thing, mid + 1, right)

    merge(arr, thing, left, mid, right)


def merge(arr, thing, left, mid, right):
    for i in range(left, right + 1):
        thing[i] = arr[i]

    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if thing[i] <= thing[j]:
            arr[k] = thing[i]
            i += 1
        else:
            arr[k] = thing[j]
            j += 1
        k += 1

    while i <= mid:
        arr[k] = thing[i]
        i += 1
        k += 1


N = int(input())
arr = list(map(int, input().split()))
thing = [0] * N
mergesort(arr, thing, 0, N - 1)
print(' '.join(map(str, arr)))
