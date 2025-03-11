number_1 = int(input("enter  the first number"))
number_2 = int(input("enter the second number"))

result = number_1 * number_2
print(number_1,"x",number_2,result)

if result < 0 : 
    print("the resilt is negative")
elif result > 0 :
    print("the result is positive")
elif result == 0 : 
    print("the result is positive and negative")
