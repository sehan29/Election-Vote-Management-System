import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")
cursor = con.cursor()


class Retrive_data_1:
    
    def fetch_data_from_id(nic_number):
        
        try:
            
            
            query = "SELECT COUNT(*) FROM citizen_details WHERE c_id = %s"
            cursor.execute(query, (nic_number,))
            result = cursor.fetchone()[0]
            """ print(result) """
            
            if(result > 0):
                mysql_query = f'SELECT * FROM citizen_details WHERE c_id={nic_number};'
                cursor.execute(mysql_query)
                fetch_data = cursor.fetchall()
                """ print(fetch_data) """
                return fetch_data
            
            else:
                
                return "No Index"
                

            
        
        except Exception as e:
            
            print("An error occurred:", str(e)) 

            
            


    def fetch_parties_data():
        
        
        
        
        try:
            
            """ cursor = con.cursor() """
            mysql_query = 'SELECT * FROM party_data;'
            cursor.execute(mysql_query)
            parties_details = cursor.fetchall()  
            print(parties_details)
            
            return parties_details 
            
            
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            con.close()
            cursor.close()
   
            
            