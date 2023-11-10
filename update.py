# installed library mysql-connector-python

import mysql.connector

#creating connection 
class update:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            password = "Akaram@7860",
            database = "bank"
            )
        
    def myupdate(self,table_name,column_name,newvalue,cusid):
        cur = self.conn.cursor()
        if newvalue.isnumeric():
            cur.execute(f"UPDATE{table_name} set {column_name}={int(newvalue)} WHERE CUSTOMERID={cusid}")
        else:
            cur.execute(f"UPDATE{table_name} set {column_name}='{newvalue}' WHERE CUSTOMERID={cusid}")
        self.conn.commit()
        print("update sucessfully")







            