import os
import time
import sys
import main_fun as main_function
from user_dash import administration_function
from user_dash import comman_header
from citizen_class import Citizen
import Insert_citizen_data as database_insert
def selectting_user_operation(selection):
    
    if(selection == 1):
        print(selection)
        os.system('cls')
        administration_function()
        administrtion_selection()
    
    elif(selection == 2):
        print(selection)
        
    elif(selection == 3):
        sys.exit()
        
    else:
        
        os.system('cls')
        print("\t\t-------------Invalid Number-----------\n")
        main_function.main_function()
        
        

def administrtion_selection():
    
    try:
        
        user_selection = int(input("Select One Operation :"))
        administration_operation(user_selection)
    
    except Exception as e:
        
        print("An error occurred:", str(e))
        

def administration_operation(selection):
    
    if(selection == 1):
        print(selection)
        
        
    
    elif(selection == 2):
        print(selection)
        
    elif(selection == 3):
        print(selection)
        os.system('cls')
        get_citizen_details()
        
    elif(selection == 4):
        print(selection)
        
    else:
        
        print("Invalid Index")
        
        
        
def get_citizen_details():
    comman_header()
    citizen_name = input("Enter Citizen Name : ")
    citizen_age = int(input("Enter Citizen Age : "))
    nic_number = input("Enter Citizen National ID Card Number : ")
    citizen_state = input("Enter Citizen State : ")
    
    
    if(citizen_age >= 18):
        
        time.sleep(2)
        print("\t\t ---------- Verification Successfully --------------")
        citizen_obj = Citizen(citizen_name,citizen_age,nic_number,citizen_state)
        k = database_insert.Database
        k.insert_citizen_data(citizen_obj)
        
        
    else:
        print("\t\t --------------- Registration Faild -----------------")
        time.sleep(3)
        os.system('cls')
        main_function.main_function()
        
    
    
    
    