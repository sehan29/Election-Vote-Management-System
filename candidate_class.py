class Candidate:
    
    def __init__(self,name,nic,age,education_qualification,province):
        
        self.__name = name
        self.__nic = nic
        self.__age = age
        self.__education_qualification = education_qualification
        self.__province = province
        
    
    def set_name(self,name):
        self.__name = name
        
    def set_nic(self,nic):
        self.nic = nic
        
    def set_age(self,age):
        self.__age = age
        
    def set_qualification(self,qualifications):
        
        self.__education_qualification = qualifications
        
    def set_province(self,province):
        self.__province = province