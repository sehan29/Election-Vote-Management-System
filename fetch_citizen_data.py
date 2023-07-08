import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")



class Retrive_data:
    
    def fetch_data():
        
        try:
            
            cursor = con.cursor()
            mysql_query = 'SELECT * FROM citizen_details;'
            cursor.execute(mysql_query)
            x = cursor.fetchall()   
            
            name_new=""
            age_new=""
            id_new=""
            province=""
            id_primary =""
            for data in x:
                
                
                len_id = len(str(data[0]))
                name_len = len(str(data[1]))
                age_len = len(str(data[2]))
                nic_len = len(str(data[3]))
                province_len = len(str(data[4]))
                
                for i in range(12):
                    
                    if(i>len_id):
                        
                        id_primary = id_primary + " "
                
                
                for i in range(27):
                    
                    if(i>name_len):
                        
                        name_new = name_new + " "

                for i in range(16):
                    
                    if(i>age_len):
                        
                        age_new = age_new + " "
                        
                for i in range(17):
                    
                    if(i>nic_len):
                        
                        id_new = id_new + " "

                for i in range(20):
                    
                    if(i>province_len):
                        
                        province = province + " "
                
                
                print(str(data[0])+id_primary+str(data[1])+name_new+str(data[2])+age_new+str(data[3])+id_new+str(data[4])+province)
                print("--------|-----------------------|---------------|---------------|-----------------",end="\n")
                name_new = ""
                age_new=""
                id_new=""
                province=""
                id_primary =""
                        
                    
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            con.close()
            cursor.close()
            
            
    
    def fetch_parties_data():
        
        
        try:
            
            cursor = con.cursor()
            mysql_query = 'SELECT * FROM party_data;'
            cursor.execute(mysql_query)
            x = cursor.fetchall()   
            
            name_new=""
            age_new=""
            id_new=""
            id_primary =""
            for data in x:
                
                
                len_id = len(str(data[0]))
                party_len = len(str(data[1]))
                president_len = len(str(data[2]))
                reg_len = len(str(data[3]))
                
                for i in range(12):
                    
                    if(i>len_id):
                        
                        id_primary = id_primary + " "
                
                
                for i in range(30):
                    
                    if(i>president_len):
                        
                        name_new = name_new + " "

                for i in range(25):
                    
                    if(i>reg_len):
                        
                        age_new = age_new + " "
                        
                for i in range(25):
                    
                    if(i>party_len):
                        
                        id_new = id_new + " "


                
                print(str(data[0])+id_primary+str(data[1])+id_new+str(data[2])+name_new+str(data[3]))
                print("--------|-----------------------|-----------------------|---------------------------",end="\n")
                name_new = ""
                age_new=""
                id_new=""
                id_primary =""
                        
                    
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            con.close()
            cursor.close()
            
            
    
        
 