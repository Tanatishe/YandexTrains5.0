import re

with open('input.txt', 'r') as file:
    massiv = []
    massiv = file.readlines()

for i, j in enumerate(massiv):
    massiv[i] = j.strip()

dicK = {}
dicK_players = {}
answer = []
first_team_goals = 0
second_team_goals = 0


def first_goal_operator(temp_goals_list):
    temp_goals_list = list(sorted(temp_goals_list, key=lambda x: x[1]))
    dicK_players[temp_goals_list[0][0]]['first_goals'] += 1
    dicK[dicK_players[temp_goals_list[0][0]]['team']]['first_goals'] += 1


for i, j in enumerate(massiv):
    if j[0] == '"':
        teams = re.findall(r'"(.*?)"', j)
        score = re.findall(r'\d+:\d+', j)
        score = list(map(int, score[0].split(':')))
        first_team_goals = score[0]
        second_team_goals = score[1]
        temp_goals_list = []
        for counter, team in enumerate(teams):
            if team not in dicK:
                dicK[team] = {'matches': 1, 'goals': score[counter], 'first_goals': 0}
            else:
                dicK[team]['matches'] += 1
                dicK[team]['goals'] += score[counter]

    elif first_team_goals > 0 or second_team_goals > 0:

        now_team = teams[not first_team_goals]

        if first_team_goals > 0:
            first_team_goals -= 1
        else:
            second_team_goals -= 1

        name = ' '.join(j.split()[:-1])
        goal_time = int(j.split()[-1].strip('\''))
        temp_goals_list.append([name, goal_time])
        if name not in dicK_players:
            dicK_players[name] = {'team': now_team, 'goals': 1, 'first_goals': 0,
                                  'list_of_minutes': [goal_time, ]}
        else:
            dicK_players[name]['goals'] += 1
            dicK_players[name]['list_of_minutes'].append(goal_time)
        if first_team_goals == 0 and second_team_goals == 0:
            first_goal_operator(temp_goals_list)

    else:
        if 'Total goals for' in j:
            temp_name = re.findall(r'"(.*?)"', j)[0]
            if temp_name in dicK:
                answer.append(dicK[temp_name]['goals'])
            else:
                answer.append(0)
        elif 'Mean goals per game for' in j:
            temp_name = re.findall(r'"(.*?)"', j)[0]
            if temp_name in dicK:
                temp_answer = dicK[temp_name]['goals'] / dicK[temp_name]['matches']
                # temp_answer = int(temp_answer * 1000)/1000
                answer.append(temp_answer)
            else:
                answer.append(0)
        elif 'Total goals by' in j:
            temp_name = j.removeprefix('Total goals by ')
            if temp_name in dicK_players:
                answer.append(dicK_players[temp_name]['goals'])
            else:
                answer.append(0)
        elif 'Mean goals per game by' in j:
            temp_name = j.removeprefix('Mean goals per game by ')
            if temp_name in dicK_players:
                temp_answer = dicK_players[temp_name]['goals'] / dicK[dicK_players[temp_name]['team']]['matches']
#                 temp_answer = int(temp_answer * 1000) / 1000
                answer.append(temp_answer)
            else:
                answer.append(0)
        elif 'Goals on minute' in j:
            minute = int(re.findall(r'\d+', j)[0])
            temp_name = j.removeprefix(f'Goals on minute {minute} by ')
            if temp_name in dicK_players:
                temp_answer = 0
                for mint in dicK_players[temp_name]['list_of_minutes']:
                    if mint == minute:
                        temp_answer += 1
                answer.append(temp_answer)
            else:
                answer.append(0)
        elif 'Goals on first' in j:
            minute = int(re.findall(r'\d+', j)[0])
            temp_name = j.removeprefix(f'Goals on first {minute} minutes by ')
            if temp_name in dicK_players:
                temp_answer = 0
                for mint in dicK_players[temp_name]['list_of_minutes']:
                    if mint <= minute:
                        temp_answer += 1
                answer.append(temp_answer)
            else:
                answer.append(0)
        elif 'Goals on last' in j:
            minute = int(re.findall(r'\d+', j)[0])
            temp_name = j.removeprefix(f'Goals on last {minute} minutes by ')
            if temp_name in dicK_players:
                temp_answer = 0
                for mint in dicK_players[temp_name]['list_of_minutes']:
                    if mint >= 91 - minute:
                        temp_answer += 1
                answer.append(temp_answer)
            else:
                answer.append(0)
        elif 'Score opens by' in j:
            temp_name = j[15:]
            actual_dict = [dicK, dicK_players][not temp_name[0] == '"']
            temp_name = temp_name.strip('"')

            temp_answer = actual_dict[temp_name]['first_goals'] if temp_name in actual_dict else 0

            answer.append(temp_answer)

print(*answer, sep='\n')
