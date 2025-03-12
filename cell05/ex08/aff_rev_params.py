import sys

sys.argv = ['Python','piscine','hello']
args = sys.argv[0:]


reversed_args = args[::1]


for arg in reversed_args:
    print(f"{arg}$")