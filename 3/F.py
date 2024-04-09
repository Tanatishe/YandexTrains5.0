dictionary = {}

for i in input().split():
    if i[0] not in dictionary:
        dictionary[i[0]] = [i, ]
    else:
        dictionary[i[0]].append(i)
        dictionary[i[0]] = sorted(dictionary[i[0]], key=lambda x: (len(x), x))

text = input().split()

for i, k in enumerate(text):
    if k[0] in dictionary:
        for j in dictionary[k[0]]:
            if j == k[:len(j)]:
                text[i] = j
                break

with open("output.txt", "w") as file:
    file.write(' '.join(text))
