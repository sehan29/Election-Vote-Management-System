class Citizen():
    
    def __init__(self,name,age,nic,province):
        
        self.name = name
        self.age = age
        self.nic = nic
        self.province = province
        
    
    def set_name(self,name):
        self.name = name   
    
    def set_age(self,age):
        self.age = age
    
    def set_nic(self,nic):
        self.nic = nic
        
    def set_province(self,province):
        self.province = province
        
    def get_name(self):
        
        print(self.name)
        
