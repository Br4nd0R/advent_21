import typing as T

with open("input.txt", "r") as f:
    binary_nums = f.read().split("\n")


def strip_first_char(values: T.List[str]) -> T.List[str]:
    chars = []
    for i, value in enumerate(values):
        chars.append(value[0])
        values[i] = value[1:]
    return chars


gamma = ""
epsilon = ""
for digit in range(len(binary_nums[0])):
    digit_values = strip_first_char(binary_nums)

    if digit_values.count("1") > digit_values.count("0"):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma_base10 = int(gamma, 2)
epsilon_base10 = int(epsilon, 2)

print(f">>> Gamma: {gamma} ({gamma_base10})")
print(f">>> Epsilon: {epsilon} ({epsilon_base10})")
print(f">>> Quantity: {gamma_base10 * epsilon_base10}")
