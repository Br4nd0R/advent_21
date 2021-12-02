import typing as T


def parse_direction(direction: str) -> T.Tuple[str, int]:
    split = direction.split(" ")
    move_type = split[0]
    value = int(split[1])
    if move_type == "down":
        value *= -1
    return (move_type, value)


with open("input.txt", "r") as f:
    directions = [parse_direction(line) for line in f.read().split("\n")]

aim = 0
depth = 0
horizontal_pos = 0
for direction in directions:
    move_type, value = direction
    if move_type == "forward":
        horizontal_pos += value
        depth += aim * value
    else:
        aim += value

print(f"Depth: {depth}")
print(f"Horizontal position: {horizontal_pos}")
print(f"Multiplied value: {depth * horizontal_pos}")
