import sys


sys.argv = [ "Code Ninja", "Numerique", "42"]


if len(sys.argv) > 1:
    
    result = sys.argv[0]
else:
    result = "none"


print(f"{result}$")