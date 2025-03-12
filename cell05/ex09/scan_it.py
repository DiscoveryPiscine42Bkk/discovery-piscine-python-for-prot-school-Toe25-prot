import sys




if len(sys.argv) == 1:
    print("none$")
else:
    word_count = 0

    for arg in sys.argv:

        if " " in arg:
            
            word_count += 1
        else:
            
            word_count += 1

    
    print(f"{word_count - 1}")
