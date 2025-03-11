iy = input()

iy = iy.split()


z_characters = [char for word in iy for char in word if char.lower() == 'z']

if len(z_characters) == 0:
    print("none")
else:
    print("".join(z_characters))