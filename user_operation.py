import os
import main_fun as main_function

def selectting_user_operation(selection):
    
    if(selection == 1):
        print(selection)
    
    elif(selection == 2):
        print(selection)
        
    elif(selection == 3):
        print(selection)
        
    else:
        
        os.system('cls')
        print("\t\t-------------Invalid Number-----------\n")
        main_function.main_function()
        