def index():
    print("-----------------------------------------------------------------")
    print("\t\tELECTION VOTE CALCULATTING SYSTEM")
    print("-----------------------------------------------------------------\n")
    print("1. Election Administration.")
    print("2. Vote.")
    print("3. Exit.")
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
    
    print("-----------------------------------------")
    print("|\tNo\t|\tParty Name\t|")
    print("-----------------------------------------")
    



def table_data(number,party_name):
    print(f"|\t{number}\t|\t{party_name}\t\t|")
    print("-----------------------------------------")

