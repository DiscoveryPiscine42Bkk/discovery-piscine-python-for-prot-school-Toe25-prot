import sys


original_array = [2, 8, 9, 48, 8, 22, -12, 2]


print(f"{original_array}$")


new_array = [x + 2 for x in original_array if x > 5]


print(f"{new_array}$")