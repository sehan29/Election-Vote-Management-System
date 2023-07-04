import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")
    

    

class Database:
    
    def insert_candidate_data(candidate_data):
        
        try:
            
            cursor = con.cursor()
            mysql_query = "INSERT INTO candidator_table name, age, nic, province VALUES(%s,%s,%s,%s)"
            values_of_citizen("asas","asas","asasa","sas")
            cursor.execute(mysql_query,values_of_citizen)
            con.commit()
            last_raw_id = cursor.lastrowid
            
            
            
            #To insert qualifications into another table
            #More Qualification
            print(last_raw_id)
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            
            con.close()
            cursor.close()