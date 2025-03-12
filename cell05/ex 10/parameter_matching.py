def para (y,) :
    
    if yu != 1 : 
        print("none")
    
    else :
        ty = input("what was the parameter? : ")
        if ty == y  :
            print("good job")

        else : 
            print("Nope sorry...")

yu = para.__code__.co_argcount

para('hello')

