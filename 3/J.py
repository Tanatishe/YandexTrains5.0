import datetime
start = datetime.datetime.now()


with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().split())

spisok = []
for i in range(k):
    spisok.append([])

main_flag = True


class Devices:
    counter = 1
    update_list = [0] * k
    dev_up_l = spisok
    full_counter = 0

    def __init__(self):
        self.name = Devices.counter
        self.update_list = [0] * k
        Devices.counter += 1
        self.request_list = [0, []]
        self.values_list = [0] * n
        self.timeslot = timeslot

    def plus_update(self, index, number_of_donor):
        self.update_list[index] = 1
        Devices.update_list[index] += 1
        Devices.dev_up_l[index].append(self.name)
        self.values_list[number_of_donor - 1] += 1
        if sum(self.update_list) == k:
            self.timeslot = timeslot
            Devices.full_counter += 1
            if Devices.full_counter == n:
                global main_flag
                main_flag = False

    def create_request_list(self, name, amount_of_updates, index):
        if self.request_list[0] != timeslot:
            self.request_list[1] = []
            self.request_list[0] = timeslot

        self.request_list[1].append([name, amount_of_updates, self.values_list[name - 1], index])

    def make_request(self, minimum):
        if sum(self.update_list) < k:
            while True:
                for i in range(k):
                    if Devices.update_list[i] == minimum and not self.update_list[i]:
                        self.request_index = i
                        donors_list = []
                        for dev_number in Devices.dev_up_l[self.request_index]:
                            donors_list.append([dev_number, sum(globals()[f'd{dev_number}'].update_list)])
                        donors_list = list(sorted(donors_list, key=lambda x: (x[1], x[0])))
                        self.donor = donors_list[0][0]
                        globals()[f'd{self.donor}'].create_request_list(self.name, sum(self.update_list),
                                                                        self.request_index)
                        return
                minimum += 1

    def process_request(self):
        temp_list = sorted(self.request_list[1], key=lambda x: (-x[2], x[1], x[0]))
        if len(temp_list) > 0:
            number = temp_list[0][0]
            globals()[f'd{number}'].plus_update(temp_list[0][3], self.name)


timeslot = 0

for _ in range(n):
    globals()[f'd{Devices.counter - 1}'] = Devices()
for i in range(k):
    d1.plus_update(i, 1)

while main_flag:
    timeslot += 1
    for i in range(1, n + 1):
        globals()[f'd{i}'].request_list[1] = []
    for i in range(1, n + 1):
        minimum = min(Devices.update_list)
        globals()[f'd{i}'].make_request(minimum)
    for i in range(1, n + 1):
        globals()[f'd{i}'].process_request()

for i in range(2, n + 1):
    print(globals()[f'd{i}'].timeslot, end=' ')

print()

finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))

