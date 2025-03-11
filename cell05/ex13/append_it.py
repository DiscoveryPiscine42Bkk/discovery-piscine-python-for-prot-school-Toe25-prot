iy = input()


iy = iy.split()

if len(iy) == 0:
    print("none")
else:
   
    print(f"parameter: {len(iy)}")
    
    
    for check in range(len(iy)):
        word_with_ism = iy[check] + "ism"  
        print(f"{word_with_ism}$")