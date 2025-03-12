import sys


sys.argv = ["the best one of my"]


if len(sys.argv) > 0:
    
    result = " ".join(sys.argv[0:]).upper() 
else:
    result = "none"


print(f"{result}$")