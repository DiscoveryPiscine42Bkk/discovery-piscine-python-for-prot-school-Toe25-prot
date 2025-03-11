iy = input()

iy = iy.split()

if len(iy) == 0 : 
    print("none")
else :
  print(F"parameter: {len(iy)}")
  for check in range(len(iy)) :
     print(F"{iy[check]} : {len(iy[check])}")
