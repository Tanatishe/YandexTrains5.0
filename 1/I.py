import datetime

n = int(input())
year = int(input())
holyds = []
for i in range(n):
    holyds.append(input().split())
first_day = input()

dow = [0, 0, 0, 0, 0, 0, 0]
days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}
months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}

date = datetime.datetime(year, 1, 1)
next_year = datetime.datetime(year + 1, 1, 1)
delta = datetime.timedelta(1)

while date < next_year:
    dow[date.weekday()] += 1
    date += delta

for i in holyds:
    day = datetime.datetime(year, months[i[1]], int(i[0])).weekday()
    dow[day] -= 1

print(days[dow.index(max(dow))], days[dow.index(min(dow))])
