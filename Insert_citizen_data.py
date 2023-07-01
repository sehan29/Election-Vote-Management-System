import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")
    

    

class Database:
    
    def insert_citizen_data(self,citizen_data):
        
        try:
            
            cursor = con.cursor()
            mysql_query = "INSERT INTO table_name name, age, nic, province VALUES(%s,%s,%s,%s)"
            values_of_citizen("asas","asas","asasa","sas")
            cursor.execute(mysql_query,values_of_citizen)
            con.commit()
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            cursor.close()