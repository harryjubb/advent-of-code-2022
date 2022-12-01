with open("./input.txt", "r") as fo:
    input_text = fo.read().split("\n\n")

calorie_group_sums = [
    sum([int(entry) for entry in group.split()]) for group in input_text
]

largest_group_sum = max(calorie_group_sums)
print(largest_group_sum)

# "Test"
assert largest_group_sum == 67658