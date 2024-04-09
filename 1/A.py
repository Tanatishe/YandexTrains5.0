Vs, Vr = map(int, input().split())
Ms, Mr = map(int, input().split())
Vmin = Vs - Vr
Vmax = Vs + Vr
Mmin = Ms - Mr
Mmax = Ms + Mr

if (Vmin >= Mmin and Vmin <= Mmax) or (Vmax >= Mmin and Vmax <= Mmax) or (Mmin >= Vmin and Mmin <= Vmax) or (
        Mmax >= Vmin and Mmax <= Vmax):
    answer = max(Mmax, Vmax) - min(Mmin, Vmin) + 1
else:
    answer = 2 * Vr + 2 * Mr + 2

print(answer)
