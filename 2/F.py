n = int(input())
numbers = list(map(int, input().split()))
a, b, k = map(int, input().split())

aprehod = a // k if a % k > 0 else a // k - 1
ahod = aprehod % n
bprehod = b // k if b % k > 0 else b // k - 1
bhod = bprehod % n

antinumbers = [numbers[0]] + numbers[-1:0:-1]

if aprehod // n == bprehod // n:
    answer = max(max(numbers[ahod:bhod + 1]), max(antinumbers[ahod:bhod + 1]))
else:
    answer = max(max(numbers[ahod:]), max(numbers[:bhod + 1]), max(antinumbers[ahod:]), max(antinumbers[:bhod + 1]))

print(answer)
