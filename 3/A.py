n = int(input())
tracks_list = []
for _ in range(n):
    count_of_tracks = int(input())
    tracks = input().split()
    tracks_list.append(tracks)

final_list = set(tracks_list[0])

for i in range(1, len(tracks_list)):
    final_list = final_list & set(tracks_list[i])

print(len(final_list))
print(*sorted(final_list))
