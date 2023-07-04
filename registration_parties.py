import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")
    

class Database:
    
    def insert_party_data(party_data):
        
        try:
            
            cursor = con.cursor()
            mysql_query = 'INSERT INTO party_data (party_name, name_president, reg_no) VALUES(%s,%s,%s);'
            values_of_citizen = (party_data.commity_name,party_data.president_of_commity,party_data.reg_id)
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
            