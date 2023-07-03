import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")
    

class Database:
    
    def insert_citizen_data(citizen_data):
        
        
        try:
            
            age = str(citizen_data.age)
            cursor = con.cursor()
            mysql_query = 'INSERT INTO citizen_details (name, c_age, c_id, c_province) VALUES(%s,%s,%s,%s);'
            values_of_citizen = (citizen_data.name,age,citizen_data.nic,citizen_data.province)
            cursor.execute(mysql_query,values_of_citizen)
            con.commit()
            
            
            if(0 < cursor.rowcount):
                
                print("Inserted Data should Be printed Here")
                print("\t\t -------- Data Insert Successfully ---------")
            
            else:
                
                print("\t\t --------- Data Insert Unsuccessfully ----------")
                
                
                
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            con.close()
            cursor.close()
            
            
            
