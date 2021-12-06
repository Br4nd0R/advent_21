import typing as T
from copy import deepcopy


def get_oxygen_generator_rating(binary_nums: T.List[str]) -> str:
    return fancy_filter(binary_nums, keep_type="majority")


def get_co2_scrub_rating(binary_nums: T.List[str]) -> str:
    return fancy_filter(binary_nums, keep_type="minority")


def fancy_filter(binary_nums: T.List[str], keep_type="majority") -> str:
    to_keep = deepcopy(binary_nums)
    for digit_idx in range(len(binary_nums)):
        if len(to_keep) == 1:
            break

        result = more_ones_or_zeros(digit_idx, to_keep)

        # 1's are majority (or tie)
        if result is None or result == 1:
            if keep_type == "majority":
                to_keep = [num for num in to_keep if num[digit_idx] == "1"]
            else:
                to_keep = [num for num in to_keep if num[digit_idx] == "0"]
        # 0's are majority
        else:
            if keep_type == "majority":
                to_keep = [num for num in to_keep if num[digit_idx] == "0"]
            else:
                to_keep = [num for num in to_keep if num[digit_idx] == "1"]

    return to_keep[0]


def more_ones_or_zeros(digit_idx: int, binary_nums: T.List[str]) -> int:
    """Returns 1 or 0 depending on which there are more
    of for the given digit index in the list of binary nums (as strings).
    Returns None if the number of zeros and ones are the same."""
    digit_values = [num[digit_idx] for num in binary_nums]

    ones = digit_values.count("1")
    zeros = digit_values.count("0")

    if ones > zeros:
        return 1
    elif zeros > ones:
        return 0
    else:
        return None


def main():
    with open("input.txt", "r") as f:
        input_nums = f.read().split("\n")

    oxygen_gen_rating = get_oxygen_generator_rating(input_nums)
    co2_scrub_rating = get_co2_scrub_rating(input_nums)

    oxy_base10 = int(oxygen_gen_rating, 2)
    co2_base10 = int(co2_scrub_rating, 2)

    print(f"Oxygen generator rating: {oxygen_gen_rating}")
    print(f"CO2 scrubber rating: {co2_scrub_rating}")
    print(f"Quantity: {oxy_base10 * co2_base10}")


if __name__ == "__main__":
    main()
