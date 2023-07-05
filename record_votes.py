import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="",database="election_data")
    

    

class Save_Votes:
    
    def insert_vote_data(voter_nic,votes):
        
        try:
            
            cursor = con.cursor()
            mysql_update = f"UPDATE citizen_details SET vote_status = 1 WHERE c_id = {voter_nic};"
            cursor.execute(mysql_update)
            con.commit()



            for data in votes:
                
                mysql_query = "INSERT INTO votes_table (citizen_nic, preference) VALUES(%s,%s);"
                values = (voter_nic,data)
                cursor.execute(mysql_query,values)
            
            con.commit()
            
            return True
                
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            
            
            con.close()
            cursor.close()
            
