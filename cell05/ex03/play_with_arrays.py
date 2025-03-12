import sys


oldy = [2, 8, 9, 48, 8, 22, -12, 2]


sys.stdout.write(f"{oldy}$\n")


newy = [x + 2 for x in oldy if x > 5]
newy = list(set(newy))


sys.stdout.write(f"{newy}$\n")