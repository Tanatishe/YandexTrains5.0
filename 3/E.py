n1 = int(input())
massiv1 = list(map(int, input().split()))
n2 = int(input())
massiv2 = list(map(int, input().split()))
n3 = int(input())
massiv3 = list(map(int, input().split()))

massiv1 = set(massiv1)
massiv2 = set(massiv2)
massiv3 = set(massiv3)

answer = (massiv1 & massiv2) | (massiv1 & massiv3) | (massiv2 & massiv3)

print(*sorted(answer))
