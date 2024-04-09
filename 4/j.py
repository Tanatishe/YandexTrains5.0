import math
from copy import deepcopy

with open('input.txt', 'r') as file:
    N, H = file.readline().split()
    N = int(N)
    H = float(H)
    coords = []
    for i in range(N + 1):
        line = file.readline()
        line = line.replace('–', '-')
        line = list(map(int, line.split()))
        coords.append(line)

coords.append([coords[0][0] - 0.000000000000001, 20000])
coords.sort(key=lambda x: (x[0], -x[1]))
coords.append([coords[-1][0] + 0.000000000000001, 20000])
counter_epta = 0
flag = False


def find_distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance


class Hole:
    holes = []
    potenc_hki = []
    coords = coords
    wid = coords[-1][0] - coords[0][0]
    image_sqre = wid * H
    counter = 1

    def __init__(self, l_border, r_border):
        self.name = Hole.counter
        Hole.counter += 1
        self.filld_sqrs = []
        self.l_border = l_border
        self.r_border = r_border
        self.body = deepcopy(Hole.coords[l_border:r_border + 1])
        self.wid = self.body[-1][0] - self.body[0][0]
        self.image_sqre = self.wid * H
        self.is_triangle = True
        self.is_trap = True
        self.is_dead = False
        self.deep = 30000
        Hole.holes.append(self.name)
        Hole.holes.sort()

    def left_join(self, vnesh_ind):
        elem2 = globals()[f'hole{Hole.holes[vnesh_ind - 1]}']
        elem2.image_sqre += self.image_sqre
        elem2.body += self.body[1:]
        elem2.body.sort()
        elem2.deep = min(elem2.deep, self.deep)
        elem2.is_trap = True
        global counter_epta
        Hole.holes.remove(self.name)
        self.is_dead = True
        counter_epta = 0
        global counter2
        counter2 += 50

    def right_join(self, vnesh_ind):
        elem2 = globals()[f'hole{Hole.holes[vnesh_ind + 1]}']
        elem2.image_sqre += self.image_sqre
        elem2.body += self.body[:-1]
        elem2.body.sort()
        elem2.deep = min(elem2.deep, self.deep)
        elem2.is_trap = True
        global counter_epta
        Hole.holes.remove(self.name)
        self.is_dead = True
        counter_epta = 0
        global counter2
        counter2 += 50

    def fill_trap(self, vnesh_ind):
        self.body.sort()
        for ind, point in enumerate(self.body[1:-2],1):
            A = self.body[ind - 1]
            B = point
            C = self.body[ind + 1]
            D = self.body[ind + 2]
            if C[1] == point[1] and D[1] == point[1]:
                del self.body[ind + 1]
                global counter_epta
                global flag
                flag = True
                counter_epta = 0
                return
            first_triangl = 0
            second_triangl = 0
            h_small = min(A[1], D[1]) - B[1]
            h_big = max(A[1], D[1]) - B[1]
            BC = C[0] - B[0]
            s_kvadrat = BC * h_small
            if A[1] > D[1]: BE = find_distance_between_points(B, A) * h_big / h_small
            else:  pass
            if A[1] > 15000:
                first_triangl == 0
            elif A[1] < D[1]:
                first_triangl = (B[0] - A[0]) * h_small / 2
            else:
                first_triangl = math.sqrt(BC**2 - h_small**2) * h_small / 2

            if D[1] > 15000:
                second_triangl = 0
            elif A[1] > D[1]: second_triangl = (D[0] - C[0]) * h_small / 2
            else: second_triangl =  first_triangl = math.sqrt(BC**2 - h_small**2) * h_small / 2

            sqr_trap = s_kvadrat + first_triangl + second_triangl

            if A[1] > D[1]:
                AB = find_distance_between_points(A, B)
                AHb = math.sqrt(AB ** 2 - h_big ** 2)
                Ehs = h_small * AHb / h_big
                E = [B[0] - Ehs, D[1]]
            else:
                AD = find_distance_between_points(A, D)
                h_bigD = math.sqrt(AD**2 - h_big**2)
                Ehs = h_small * h_bigD / h_big
                E = [C[0] + Ehs, A[1]]

            if sqr_trap > self.image_sqre:
                new_h = h_small * self.image_sqre / (s_kvadrat - first_triangl + second_triangl)
                old_h = B[1] - self.deep
                new_deep = old_h + new_h
                Hole.potenc_hki.append(new_deep)
                Hole.image_sqre -= sqr_trap
                self.sqr_trap = sqr_trap
                self.is_trap = False

            elif A == self.body[0] and A[1] < C[1]:
                Hole.image_sqre -= sqr_trap
                self.image_sqre -= sqr_trap
                del self.body[ind]
                del self.body[ind + 1]
                self.body.append(E)
                self.body.sort()
                self.left_join(vnesh_ind)
            elif D == self.body[-1] and A[1] > C[1]:
                Hole.image_sqre -= sqr_trap
                self.image_sqre -= sqr_trap
                del self.body[ind]
                del self.body[ind]
                self.body.append(E)
                self.body.sort()
                self.right_join(vnesh_ind)
            else:
                Hole.image_sqre -= sqr_trap
                self.image_sqre -= sqr_trap
                del self.body[ind]
                del self.body[ind]
                self.body.append(E)
                self.body.sort()

    def find_tri(self, vnesh_ind):
        for ind, point in enumerate(self.body[:-1]):
            p1 = self.body[ind - 1]
            p2 = self.body[ind + 1]
            if p1[1] > point[1] and p2[1] > point[1]:
                A, C = [[p1, p2], [p2, p1]][not p1[1] < p2[1]]
                B = point
                self.deep = B[1]
                h = A[1] - B[1]
                AB = find_distance_between_points(A, B)
                BC = find_distance_between_points(B, C)
                BD = BC * h / (C[1] - B[1])
                X = [B[0], A[1]]
                BX = h
                AX = find_distance_between_points(A, X)
                XD = math.sqrt(BD ** 2 - BX ** 2)
                AD = AX + XD
                D = [A[0] + AD, A[1]] if (p1[1] < p2[1]) else [A[0] - AD, A[1]]
                self.s_tri = BX * AD * 0.5

                if self.s_tri > self.image_sqre:
                    new_h = h * math.sqrt(self.image_sqre / self.s_tri)
                    Hole.potenc_hki.append(new_h)
                elif p1 == self.body[0] and p1[1] < p2[1]:
                    Hole.image_sqre -= self.s_tri
                    self.image_sqre -= self.s_tri
                    del self.body[ind]
                    self.body.append(D)
                    self.body.sort()
                    self.left_join(vnesh_ind)
                elif p2 == self.body[-1] and p1[1] > p2[1]:
                    Hole.image_sqre -= self.s_tri
                    self.image_sqre -= self.s_tri
                    del self.body[ind]
                    self.body.append(D)
                    self.body.sort()
                    self.right_join(vnesh_ind)
                else:
                    Hole.image_sqre -= self.s_tri
                    self.image_sqre -= self.s_tri
                    del self.body[ind]
                    self.body.append(D)
                    self.body.sort()
                    self.is_triangle = False
                return

    @classmethod
    def find_holes(cls):
        c = cls.coords
        l_flag = False
        r_flag = False
        for ind, val in enumerate(c[1:], 1):

            if c[ind - 1][1] > val[1] and not l_flag:
                if r_flag or ind == (len(c) - 1):
                    globals()[f'hole{Hole.counter - 1}'] = Hole(l_border, ind - 1)
                    r_flag = False
                l_border = ind - 1
                l_flag = True

            if c[ind - 1][1] < val[1] and l_flag:
                r_flag = True
                l_flag = False

            if ind == (len(c) - 1):
                globals()[f'hole{Hole.counter - 1}'] = Hole(l_border, ind)


counter2 = 200


def main():
    Hole.find_holes()
    global counter_epta
    global counter2

    counter_epta = 0
    while counter2 > 0:
        flag = False

        if globals()[f'hole{Hole.holes[counter_epta]}'].is_triangle:
            globals()[f'hole{Hole.holes[counter_epta]}'].find_tri(counter_epta)
        elif globals()[f'hole{Hole.holes[counter_epta]}'].is_trap:
            globals()[f'hole{Hole.holes[counter_epta]}'].fill_trap(counter_epta)
        if flag:
            continue
        counter_epta += 1
        if counter_epta == (len(Hole.holes)):
            counter_epta = 0
        counter2 -= 1

    print(max(Hole.potenc_hki))


main()
