import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")
    

    

class Database:
    
    def insert_candidate_data(candidate_data):
        
        try:
            
            cursor = con.cursor()
            mysql_query = "INSERT INTO candidator_table (candidator_nic, party_id) VALUES(%s,%s)"
            values_of_citizen = (candidate_data.nic,candidate_data.party_number)
            cursor.execute(mysql_query,values_of_citizen)
            con.commit()
            last_raw_id = cursor.lastrowid
            
            
            
            #To insert qualifications into another table
            #More Qualification
            for data in candidate_data.education_qualification:
                print(data)
                mysql_query = "INSERT INTO candidator_qualifications (candidator_id, qualifications) VALUES(%s,%s);"
                qualification_values = (candidate_data.nic,data)
                cursor.execute(mysql_query,qualification_values)
            
            con.commit()
            qq = cursor.lastrowid
                
                
                
            print(last_raw_id)
            print(qq)
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            
            con.close()
            cursor.close()