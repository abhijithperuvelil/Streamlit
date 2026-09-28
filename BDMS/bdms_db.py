from mysql import connector
class DonorCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=connector.connect(user="root",password="root",host="localhost",database="blood_db")
        self.c = self.con.cursor()
        print("DataBase Connection Established")
    def post(self,name,blood_group,phone,city,last_donation):
        query="insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
        data=(name,blood_group,phone,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()
    def get(self):
        query="select * from donor"
        self.c.execute(query)
        records=self.c.fetchall()
        return records
    def get_id(self,id):
        query="select * from donor where id=%s"
        data=(id,)
        self.c.execute(query,data)
        records=self.c.fetchone()
        return records
    def put(self,id,name,blood_group,phone,city,last_donation):
        query="update donor set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data=(name,blood_group,phone,city,last_donation,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False
    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False



