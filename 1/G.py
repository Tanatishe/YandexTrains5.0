we = int(input())
hp = int(input())
spawn = int(input())

they = 0
turn = 0
agro = False
answers = []


def experiment(we, hp, spawn, they, turn, agro):
    while (hp > 0 or they > 0) and we > 0:
        turn += 1
        shots = we

        if shots >= hp and not agro:
            answers.append(experiment(we, hp, spawn, they, turn - 1, agro=True))

        if shots >= hp and agro:
            shots -= hp
            hp = 0
            they -= shots
        else:
            rashod = they
            they = they - shots
            shots -= rashod
            if they < 0:
                they = 0
            if shots < 1 and hp > 0:
                return -1
            hp -= shots

        we -= they
        if hp > 0:
            they += spawn
    return (turn if we > 0 else -1)


answers.append(experiment(we, hp, spawn, they, turn, agro))

answers = list(sorted(set(answers)))
answer = answers[1] if len(answers) > 1 and answers[0] == -1 else answers[0]

print(answer)
