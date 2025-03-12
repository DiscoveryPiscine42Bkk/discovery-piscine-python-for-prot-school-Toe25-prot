import sys

def para(y):
    yu = para.__code__.co_argcount  
    
    if yu != 0:   
       
        if y.strip() == "Number of parameter:": 
            print()
        else:
            word_count = len(y.split())
            print(f"Number of parameter: {word_count}")
    else:
        print("No parameters received.")
    

param_count = len(sys.argv) - 1  


print()


para('')  
