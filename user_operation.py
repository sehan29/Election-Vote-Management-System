import os
import time
import sys
import main_fun as main_function
from user_dash import administration_function
from user_dash import comman_header
from user_dash import registered_citizen_template
from user_dash import registered_parties_template
from user_dash import votting_panel_header
from user_dash import table_header
from user_dash import table_data
from user_dash import candidator_table_header
from user_dash import candidator_details
from user_dash import user_preferance_list
from citizen_class import Citizen
import Insert_citizen_data as database_insert
from fetch_citizen_data import Retrive_data
from politicle_ import Politicle_part
from registration_parties import Database
from candidate_class import Candidate
from insert_candidate_data import Database
from get_user_details_from_id import Retrive_data_1
from filter_candidators import Retrive_Party
from record_votes import Save_Votes



def selectting_user_operation(selection):
    
    if(selection == 1):
        print(selection)
        os.system('cls')
        administration_function()
        administrtion_selection()
    
    elif(selection == 2):
        print(selection)
        os.system('cls')
        make_vote()
        
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
        get_party_details()
        
    
    elif(selection == 2):
        print(selection)
        os.system('cls')
        get_candidator_details()
        
    elif(selection == 3):
        print(selection)
        os.system('cls')
        get_citizen_details()
        
    elif(selection == 4):
        print(selection)
        os.system('cls')
        view_registered_parties()
        
             
    elif(selection == 5):
        print(selection)
        
    elif(selection == 6):
        print(selection)
        os.system('cls')
        view_registered_citizen()
        
    elif(selection == 7):
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
        
    
    
    
def view_registered_citizen():
    comman_header()
    registered_citizen_template()
    Retrive_data.fetch_data()
    
    


def get_pary_details():
    
    comman_header()
    party_name = input("Enter Party Name : ")
    reg_id = input("Registered ID Of Party : ")
    president_name = input("Enter President Name of Party : ")
    politicle_object = Politicle_part(party_name,president_name,reg_id)
    database_obj = Database
    database_obj.insert_party_data(politicle_object)
    
   
   
def view_registered_parties():
    comman_header()
    registered_parties_template()
    obj = Retrive_data
    obj.fetch_parties_data()
    
    
def get_candidator_details():
    
    candidator_qualification = []
    comman_header()
    candidator_name = input("Enter Candidator Name : ")
    candidator_age = input("Enter Candidator Age : ")
    nic_number = input("Enter Candidator National ID Card Number : ")
    citizen_state = input("Enter Candidator State : ")
    obj = Retrive_data
    obj.fetch_parties_data()
    party_reg_number = input("Enter Party Registration Number : ")  
    qualification_status = input("If You have Education Qualification Press [Y], OtherWise Press [N] : ")
        
    while True:
      
        if(qualification_status == 'y' or qualification_status == 'Y'):
            
            qualifications = input("Enter Candidator Education Qualification : ")
            candidator_qualification.append(qualifications)
        
        else:
            break
        
        qualification_status = input("If You have More Education Qualification Press [Y], OtherWise Press [N] : ")
        
    
    candidator_obj = Candidate(candidator_name,nic_number,candidator_age,candidator_qualification,citizen_state,party_reg_number)
    db_candidate_obj = Database
    citizen_obj = database_insert.Database
    db_candidate_obj.insert_candidate_data(candidator_obj)
    citizen_obj.insert_citizen_data(candidator_obj)
    
    
    
    

def make_vote():
    
    
    retrive_obj = Retrive_data_1
    comman_header()
    get_nic_number = input("Enter Your NIC Number : ")
    user_data = retrive_obj.fetch_data_from_id(get_nic_number)
    
    
    if(user_data == "No Index"):
        
        print("----- Invalid Index Number -----")
    
    else:
        
        os.system('cls')
        """ print(user_data) """
        votting_panel_header(user_data[0][1],user_data[0][3],user_data[0][4])
        select_one_party(user_data[0][4],user_data[0][3])


def select_one_party(province,voter_nic):
    
    user_preferance =[]
    party_obj = Retrive_Party
    fetch_candidator = Retrive_Party
    accourding_to_province = Retrive_Party
    parties_fetch_obj = Retrive_data_1
    votes_obj = Save_Votes
    party_details = parties_fetch_obj.fetch_parties_data()
    
    table_header()
    
    for data in party_details:
        
        table_data(data[0],data[1])
    
    
    select_party = int(input("Select The Party Number : "))
    party_reg_number = party_obj.fetch_parties_data(select_party)
    candidator_id = fetch_candidator.fetch_candidators(party_reg_number[0][0])
    
    candidator_table_header()
    
    
    for data in candidator_id:
        
        
        details = accourding_to_province.fetch_candidators_according_to_province(data[0],province)
        
        
        if(details == 'None'):
            
            pass
        
        else:
            
            candidator_details(details[0][1],details[0][0])
            
            
    
    for i in range(0,3):
        
        prefreance = input(f"Enter Candidator Number {i+1} : ")
        user_preferance.append(prefreance)
    
    user_preferance_list(user_preferance)
    
    
    save_statues = input("Do You Want To Submit Data (Y/N) : ")
    
    if(save_statues == 'y' or save_statues == 'Y'):
        
        succes_val = votes_obj.insert_vote_data(voter_nic,user_preferance)
        
        if(succes_val):
            
            print("\n\t\t ---------- Records Saved Succesfully ------------\n\n")
        else:
            
            print("\n\t\t ---------- Records Saved Unsucces ---------------\n\n")
            
            main_function.main_function()
        
 
    
    else:
        
        main_function.main_function()
        print("Return To the Main Menu")
    
        
            

    
    
    
    