with open('input.txt', 'r') as fin:
    stats = fin.readline()
    content = fin.read()

while '  ' in content:
    content = content.replace('  ', ' ')
while '\n \n' in content:
    content = content.replace('\n \n', '\n\n')
content = content.split('\n\n')
# passed 11
# test = (content,)
# print(*content, sep='\n')
# exit()

w, h, c = map(int, stats.split())

y = 0
x = 0

artefacts = []
pics_coords = []
serial_flag = False
ser_x = 0
ser_y = 0


def new_str():
    global x, y, line_hi
    y += line_hi
    line_hi = h
    x = 0
    delet_list = []
    for i in range(len(artefacts)):
        if artefacts[i][2] <= y:
            delet_list.append(i)
    counter = 0
    for i in delet_list:
        del artefacts[i - counter]
        counter += 1


def process_artefacts(wid, space):
    space = space * c
    global artefacts, x, serial_flag

    counter_trick = 1
    while len(artefacts) > 0 or counter_trick > 0:
        counter_trick = 0
        for i in range(len(artefacts)):
            if artefacts[i][0] - x >= wid + space:
                x += wid + space
                serial_flag = False
                return
            if artefacts[i][1] >= x:
                x = artefacts[i][1]
                space = 0
        if w - x < wid + space:
            new_str()
            space = 0
        else:
            x += wid + space
            serial_flag = False
            return
    x += wid + space
    serial_flag = False


def process_pict(pict):
    global line_hi, x, y
    wed = []
    for i in pict[pict.find('width=') + 6:]:
        if i.isdigit():
            wed.append(i)
        else:
            break
    wed = int(''.join(wed))
    hi = []
    for i in pict[pict.find('height=') + 7:]:
        if i.isdigit():
            hi.append(i)
        else:
            break
    hi = int(''.join(hi))

    if 'layout=embedded' in pict:
        process_artefacts(wed, [1, 0][not x])
        if line_hi < hi:
            line_hi = hi
        now_x = x - wed
        now_y = y

    elif 'layout=surrounded' in pict:
        process_artefacts(wed, 0)
        global artefacts
        artefacts.append((x - wed, x, y + hi))
        artefacts = sorted(artefacts, key=lambda x: x[1])
        now_x = x - wed
        now_y = y

    elif 'layout=floating' in pict:
        dx = []
        for i in pict[pict.find('dx=') + 3:]:
            if i.isdigit() or i == '-':
                dx.append(i)
            else:
                break
        dx = int(''.join(dx))
        dy = []
        for i in pict[pict.find('dy=') + 3:]:
            if i.isdigit() or i == '-':
                dy.append(i)
            else:
                break
        dy = int(''.join(dy))
        global serial_flag, ser_x, ser_y
        now_x = [(x + dx), (ser_x + dx)][serial_flag]
        if now_x < 0:
            now_x = 0
        if now_x + wed > w:
            now_x = w - wed
        now_y = [(y + dy), (ser_y + dy)][serial_flag]
        ser_x = now_x + wed
        ser_y = now_y
        serial_flag = True

    pics_coords.append((now_x, now_y))


for i in content:
    i = i.replace('\n', ' ')
    # print(i)

    line_hi = h
    flag = False
    pict = ''
    word_l = 0
    for j in i:
        if j == '(':
            flag = True
        if flag:
            pict += j
        if not flag and j != ' ':
            word_l += 1
        if not flag and word_l and j == ' ':
            process_artefacts(word_l * c, [1, 0][not x])
            word_l = 0
        if j == ')':
            flag = False
            process_pict(pict)
            pict = ''
    if word_l:
        process_artefacts(word_l * c, [1, 0][not x])
    new_str()

    serial_flag = False

for i in pics_coords:
    print(*i)
