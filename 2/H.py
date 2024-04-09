i, j = map(int, input().split())
matrix = []
for _ in range(i):
    matrix.append(list(map(int, input().split())))

answer = [-1, -1]
first = -1
first_id = [-1, -1]
second = -2
second_id = [-2, -2]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > first:
            second = first
            second_id = first_id
            first = matrix[i][j]
            first_id = [i, j]
        elif matrix[i][j] > second:
            second = matrix[i][j]
            second_id = [i, j]

if first_id[0] == second_id[0]:
    fire_numb = first_id[0]
    answer[0] = fire_numb + 1
    for target in range(len(matrix[fire_numb])):
        matrix[fire_numb][target] = -1
    third = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > third:
                third = matrix[i][j]
                answer[1] = j + 1
elif first_id[1] == second_id[1]:
    fire_numb = first_id[1]
    answer[1] = fire_numb + 1
    for target in range(len(matrix)):
        matrix[target][fire_numb] = -1
    third = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > third:
                third = matrix[i][j]
                answer[0] = i + 1
else:
    ray1 = matrix[first_id[0]].copy()
    ray1.remove(first)
    ray2 = matrix[second_id[0]].copy()
    ray2.remove(second)
    ray3 = []
    for i in range(len(matrix)):
        ray3.append(matrix[i][first_id[1]])
    ray3.remove(first)
    ray4 = []
    for i in range(len(matrix)):
        ray4.append(matrix[i][second_id[1]])
    ray4.remove(second)
    hz = [max(ray1), max(ray2), max(ray3), max(ray4)]
    answer = (
        (first_id[0] + 1, second_id[1] + 1), (second_id[0] + 1, first_id[1] + 1), (second_id[0] + 1, first_id[1] + 1),
        (first_id[0] + 1, second_id[1] + 1))[
        hz.index(max(hz))]
print(*answer)
