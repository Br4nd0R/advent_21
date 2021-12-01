with open("input.py", "r") as f:
    depths = [int(d[:-1]) for d in f.readlines()]

num_increases = 0
for idx, depth in enumerate(depths):
    if idx > 0 and depths[idx] > depths[idx - 1]:
        num_increases += 1

print(f"number of increases: {num_increases}")
