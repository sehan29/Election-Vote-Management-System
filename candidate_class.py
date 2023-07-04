from citizen_class import Citizen

class Candidate(Citizen):
    
    def __init__(self,name,nic,age,education_qualification,province,party_number):
        
        
        super().__init__(name,age,nic,province)
        
        self.education_qualification = education_qualification
        self.party_number = party_number
        
        
    def set_qualification(self,qualifications):
        self.education_qualification = qualifications








""" k = Candidate("sdsd","1212","12","2323232","padukka","122221")

p = Citizen

print(k.age) 
k.party_number """

