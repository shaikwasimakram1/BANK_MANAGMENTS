# installed library mysql-connector-python

import mysql.connector

#creating connection 
class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            password = "Akaram@7860",
            database = "bank"
            )
        
    def personal_details(self,customerid,firstname,lastname,address,phonenumber,aadharnumber,pan):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({customerid},'{firstname}','{lastname}','{address}',{phonenumber},'{aadharnumber}','{pan}')")
        self.conn.commit()
        print("personal informaton has been saved successfully")


    def bank_details(self,acn,cid,ifsc,actype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO BANK_DETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("bank details information has been successfully")



    def transaction_details(self,trsnid,sacc,racc,amt,method):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO TRANSACTION_DETAILS VALUES({trsnid},{sacc},{racc},{amt},'{method}')")
        self.conn.commit()
        print("-----------Transaction details has been saved successfully-----------")


    def account_details(self,acn,trsnid,amt,clsngbal,transtype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO ACCOUNT_DETAILS VALUES({acn},{trsnid},{amt},{clsngbal},'{transtype}')")
        self.conn.commit()
        print("-----------Account details has been saved successfully----------")









