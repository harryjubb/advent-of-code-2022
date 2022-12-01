# Part 1:

# Find the Elf carrying the most Calories. How many total Calories is that
# Elf carrying?

with open("./input.txt", "r") as fo:
    food_item_calories_per_elf = fo.read().split("\n\n")


per_elf_calorie_totals = [
    sum(
        [
            int(food_calorie_value)
            for food_calorie_value in elfs_food_item_calories.split()
        ]
    )
    for elfs_food_item_calories in food_item_calories_per_elf
]


largest_total_food_calories = max(per_elf_calorie_totals)

# "Test"
assert largest_total_food_calories == 67658

print("Part 1:", largest_total_food_calories)

# Part 2

# Find the top three Elves carrying the most Calories. How many Calories
# are those Elves carrying in total?
top_three_food_calories = sorted(per_elf_calorie_totals)[-3:]

assert len(top_three_food_calories) == 3
assert max(top_three_food_calories) == max(per_elf_calorie_totals)

top_three_total_food_calories = sum(top_three_food_calories)

print("Part 2:", top_three_total_food_calories)
