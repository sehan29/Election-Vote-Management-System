#To Register a Politicle part

class Politicle_part:
    
    def __init__(self,commity_name,president_of_commity,reg_id):
        
        self.commity_name = commity_name
        self.president_of_commity = president_of_commity
        self.reg_id = reg_id
    
    
    def set_commity_name(self,name):
        
        self.commity_name = name

    def set_president_name(self,name):
        
        self.president_of_commity = name
        
    def set_reg_id(self,id):
        self.reg_id  = id