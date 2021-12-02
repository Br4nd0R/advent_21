import typing as T

with open("input.txt", "r") as f:
    depths = [int(d[:-1]) for d in f.readlines()]


def get_depths(depths: T.List[int]) -> int:
    for i, depth in enumerate(depths):
        if i + 2 <= len(depths) - 1:
            yield depths[i] + depths[i + 1] + depths[i + 2]


num_increases = 0
last_depth = None
for current_depth in get_depths(depths):
    if last_depth and current_depth > last_depth:
        num_increases += 1
    last_depth = current_depth

print(f"number of increases: {num_increases}")
