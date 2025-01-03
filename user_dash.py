def index():
    print("-----------------------------------------------------------------")
    print("\t\tELECTION VOTE CALCULATTING SYSTEM")
    print("-----------------------------------------------------------------\n")
    print("1. Election Administration.")
    print("2. Vote.")
    print("3. Election Result.")
    print("4. Exit.")
    print("\n-----------------------------------------------------------------")
            


def administration_function():
    
    print("-------------------------------------------------------------------------------")
    print("\t\tELECTION VOTE CALCULATTING SYSTEM")
    print("-------------------------------------------------------------------------------\n")
    print("1. Register New Party.")
    print("2. Register New Politicle Candidator.")
    print("3. Register New Citizen.")
    print("4. View Registered Parties.")
    print("5. View Registered Politicle Candidator.")
    print("6. View Registered Citizen.")
    print("7. Back.")
    print("\n-----------------------------------------------------------------")
    

def comman_header():
    
    print("----------------------------------------------------------------------------------")
    print("\t\t\tELECTION VOTE CALCULATTING SYSTEM")
    print("----------------------------------------------------------------------------------\n")
    
    
def registered_citizen_template():
    
    print("\nCitizen Registration List\n")
    print("No\t|\tName\t\t|\tAge\t|\tNIC\t|\tProvince")
    print("--------|-----------------------|---------------|---------------|-----------------")
    

def registered_parties_template():
    
    print("No\t|\tParty Name\t|\tPresident Name\t|\tRegistration Number\t")
    print("--------|-----------------------|-----------------------|---------------------------")





    

def votting_panel_header(name,nic,province):

    print("----------------------------------------------------------------------------------")
    print("\t\t\tELECTION VOTE CALCULATTING SYSTEM")
    print("----------------------------------------------------------------------------------\n")
    print("Name : ",name)
    print("NIC Number : ",nic)
    print("Province : ",province)
    print("----------------------------------------------------------------------------------")
    
    

def table_header():
    
    print("\nSelect One Party\n")
    print("-----------------------------------------")
    print("|\tNo\t|\tParty Name\t|")
    print("-----------------------------------------")
    



def table_data(number,party_name):
    print(f"|\t{number}\t|\t{party_name}\t\t|")
    print("-----------------------------------------")



def candidator_table_header():

    print("-------------------------------------------------")
    print("|\tNo\t|\tCandidator Name\t\t|")
    print("-------------------------------------------------")
    


def candidator_details(number,name):

    print(f"\t{number}\t|\t{name}\t\t\t")
    print("-------------------------------------------------")
    
    
  
    
def user_preferance_list(preferance_list):
    
    print("--- Preferance ---\n")
    print("\n-------------------------------------------------")
    print(f"|\t{preferance_list[0]}\t|\t{preferance_list[1]}\t|\t{preferance_list[2]}\t|")
    print("-------------------------------------------------")
    
    

def election_result():
    print("\n1.View Candidators Result.")
    print("2.Final Result (Ghraph).\n")



def candidator_result_header():
    
    print("-----------------------------------------------------------------------------------------------------------------")
    print("|\tID\t|\tName\t\t\t|\tProvince\t\t|\tParty\t|\tVotes\t|")
    print("-----------------------------------------------------------------------------------------------------------------")
    

def candidate_body_details(id,name,province,party,votes):
    print(f"|\t{id}\t|\t{name}\t|\t{province}\t\t|\t{party}\t|\t{votes}\t|")
    print("-----------------------------------------------------------------------------------------------------------------")
    
    
def candidator_header():
    print("Registered Candidates List\n")
    print(f"|\tID\t|\tName\t\t|\tProvince\t\t|\tParty\t|")
    print("-----------------------------------------------------------------------------------------")
    

def registered_candidators(id,name,province,party):
    
    print(f"|\t{id}\t|\t{name}\t|\t{province}\t\t|\t{party}\t|")
    print("-----------------------------------------------------------------------------------------")
    