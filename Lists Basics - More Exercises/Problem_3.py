# 3. Car Race

map_race = input().split()
map_race.pop((len(map_race) - 1) // 2)

time_left_ricer = 0
time_right_ricer = 0

race_map_len = len(map_race)

left_side = map_race[:race_map_len // 2]
right_side = map_race[race_map_len // 2:]

left_side = [int(time) for time in left_side]
right_side = [int(time) for time in right_side]

for time in left_side:
    if time != 0:
        time_left_ricer += time
    else:
        time_left_ricer -= time_left_ricer * 0.2

for time in right_side:
    if time != 0:
        time_right_ricer += time
    else:
        time_right_ricer -= time_right_ricer * 0.2

winner = "left" if time_left_ricer < time_right_ricer else "right"
winner_time = min(time_left_ricer, time_right_ricer)

print(f"The winner is {winner} with total time: {round(winner_time, 1):.1f}")
