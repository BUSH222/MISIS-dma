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


N = int(input())
arr = list(map(int, input().split()))
quicksort(arr, 0, N - 1)
print(' '.join(map(str, arr)))

