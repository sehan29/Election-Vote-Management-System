import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")


class Retrive_Party:
    
    def fetch_parties_data(party_id):
        
        
        try:
            
            cursor = con.cursor()
            mysql_query = f'SELECT reg_no FROM party_data WHERE id = {party_id};'
            cursor.execute(mysql_query)
            x = cursor.fetchall()     
            """ print(x)     """
            
            return x
                 
             
                    
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
    
    def fetch_candidators(party_reg_no):
        
        try:
            cursor = con.cursor()
            mysql_query = f'SELECT candidator_nic FROM candidator_table WHERE party_id = {party_reg_no};'
            cursor.execute(mysql_query)
            candidators_id = cursor.fetchall()
            
            return candidators_id
            """ print(candidators_id)   """   
            
        
        except Exception as e:
            print("An error occurred:", str(e))
    
    
    
    def fetch_candidators_according_to_province(can_id,province):
        
        
        
        try:
            
            cursor = con.cursor()
            query = "SELECT COUNT(*) FROM citizen_details WHERE c_id = %s AND c_province = %s;"
            cursor.execute(query, (can_id,province))
            result = cursor.fetchone()[0]
            """ print(result) """
            
            if(result > 0):
                mysql_query = 'SELECT name, c_id FROM citizen_details WHERE c_id = %s AND c_province = %s;'
                cursor.execute(mysql_query,(can_id,province))
                fetch_data = cursor.fetchall()
                return fetch_data
            
            else:
                
                return 'None'
        
        except Exception as e:
            
            print("An error occurred:", str(e)) 
            
            
            
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""         try:
            cursor = con.cursor()
            mysql_query = 'SELECT name FROM citizen_details WHERE c_id = %s AND c_province = %s;'
            print(mysql_query)
            cursor.execute(mysql_query,(can_id,province))
            details = cursor.fetchall()
            
            print(details)     
            
        
        except Exception as e:
            print("An error occurred:", str(e)) """
            