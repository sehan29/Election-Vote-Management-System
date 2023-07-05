            for data in votes:
                print(data)
                mysql_query = "INSERT INTO votes_table (citizen_nic, preference) VALUES(%s,%s);"
                values = (voter_nic,data)
                cursor.execute(mysql_query,values)
            
            con.commit()