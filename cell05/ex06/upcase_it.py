import sys


sys.argv = ["initiation"]


if len(sys.argv) > 0:
    
    result = " ".join(sys.argv[0:]).upper() 
else:
    result = "none"


print(f"{result}$")