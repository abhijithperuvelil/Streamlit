import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="library_db")
        self.c=self.con.cursor()
        print("DataBase Connection Established")
    def list(self):
        query="select * from book"
        self.c.execute(query)
        records=self.c.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return records
        else:
            print("No Records Found")
    def create(self,title,author,price,pages,language):
        # self.title=input("Enter the Title of the Book: ")
        # self.author=input("Enter the Author of the Book: ")
        # self.price=int(input("Enter the Title of the Book: "))
        # self.pages = int(input("Enter the Price of the Book: "))
        # self.language = input("Enter the Language of the Book: ")
        # query="insert into book (title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
        # data=(self.title,self.author,self.price,self.pages,self.language)
        # self.c.execute(query,data)
        # self.con.commit()
        query="insert into book (title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.c.execute(query,data)
        self.con.commit()
        print("Data Inserted")
    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        records=self.c.fetchone()
        return records
    def update(self,id,title,author,price,pages,language):
        query = "update  book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data = (title, author, price, pages, language,id)
        self.c.execute(query, data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False
    def delete (self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        return self.c.rowcount

        #     print("No Record Found")
a= BookListCreateRetrieveUpdateDelete()
# a.list()
# a.create("Alchemist","arun",280,30,"malayalam")
# a.retrieve(1)
# a.delete(4)
a.update(1,"alchemist","jhon",2000,28,"english")
