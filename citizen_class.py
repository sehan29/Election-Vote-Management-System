class Citizen:
    
    def __init__(self,name,age,nic,province):
        
        self.__name = name
        self.__age = age
        self.nic = nic
        self.__province = province
        
    
    def set_name(self,name):
        self.name = name   
    
    def set_age(self,age):
        self.age = age
    
    def set_nic(self,nic):
        self.nic = nic
        
    def set_province(self,province):
        self.province = province
        
