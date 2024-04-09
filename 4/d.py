with open('input.txt', 'r') as file:
    w, n, m = map(int, file.readline().split())
    array_a = list(map(int, file.readline().split()))
    array_b = list(map(int, file.readline().split()))


def check(width, array):
    now_w = width
    h = 1
    is_first = True
    for word in array:
        if is_first:
            now_w -= word
            is_first = False
        else:
            if now_w >= word + 1:
                now_w -= word + 1
            else:
                h += 1
                now_w = width - word
    return h


left = max(array_a)
lrirht = w - max(array_b)
minimum = max(n, m)

while left <= lrirht:
    mid = (left + lrirht) // 2
    left_l = check(mid, array_a)
    lright_l = check(w - mid, array_b)
    now_min = max(left_l, lright_l)
    minimum = min(minimum, now_min)
    # print(left_l, lright_l)
    if check(mid, array_a) >= check(w - mid, array_b):
        left = mid + 1
    else:
        lrirht = mid - 1

print(minimum)
