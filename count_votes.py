import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")



class Votes:
    
    def fetch_votes(can_nic):
        
        try:
            
            cursor = con.cursor()
            
            query = "SELECT COUNT(*) FROM votes_table WHERE preference = %s;"
            cursor.execute(query, (can_nic,))
            result = cursor.fetchone()[0]
            
            """ print(result) """
            return result
            

            
            
            

    
                        
                    
        
        
        except Exception as e:
            print("An error occurred:", str(e))
        
            


"""             mysql_query = 'SELECT COUNT(citizen_nic) FROM votes_table WHERE preference = %s;'
            cursor.execute(mysql_query,(can_nic,))
            count_of_votes = cursor.fetchall()   
            print(count_of_votes)
             """
    

        
 