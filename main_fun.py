import os
from user_dash import index
import user_operation as get_selection


def main_function():
    
    index()
    
    try:
        
        user_operation_1 = int(input("Select One Operation : "))
        get_selection.selectting_user_operation(user_operation_1)
    
    except Exception as e:
        
        os.system('cls')
        print("An error occurred:", str(e))
        main_function()



if(__name__ == "__main__"):
    main_function()
    