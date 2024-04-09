F1, S1 = map(int, input().split(':'))
F2, S2 = map(int, input().split(':'))
homegame = int(input()) - 1
answer = (S2 + S1) - (F1 + F2)
test = (F1 - S2) if homegame else (F2 - S1 + answer)
if test < 1:
    answer += 1

if answer < 0:
    answer = 0

print(answer)
