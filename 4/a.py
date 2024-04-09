n = int(input())
array = list(sorted(map(int, input().split())))
k = int(input())
reqs = []
for _ in range(k):
    reqs.append(list(map(int, input().split())))

answers = []


def binary_search_l(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


def binary_search_r(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return high


for borders in reqs:
    counter = 0
    print(binary_search_r(array, borders[1]) - binary_search_l(array, borders[0]) + 1, end=' ')
