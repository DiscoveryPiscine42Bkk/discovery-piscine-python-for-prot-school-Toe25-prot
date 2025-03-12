import sys

sys.argv = ["The best of my"]

if len(sys.argv) > 0:
    
    result = " ".join(sys.argv[0:]).lower()  
else:
    result = "none"


print(f"{result}$")