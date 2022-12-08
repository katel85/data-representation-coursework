import mysql.connector

class StudentDAO: 
    host =""  #set some class variables 
    user = ""
    password =""
    database =""

    connection = ""
    cursor =""

    def __init__(self): 
        #these should be read from a config file. this is hard coded below
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="datarepresentation"
        #self.user="datarep",  # this is the user name on my mac
        #self.passwd="password" # for my mac
        
    
    def getCursor(self): # function created to connect to the host username and database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    def closeAll(self): # close connection and cursor. Must be done everytime you make a connection. This ensures connections don't pile up.
        self.connection.close()
        self.cursor.close()
    
    def create(self, values): 
        cursor = self.getCursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self): # apssing back the result
        cursor = self.getCursor()
        sql="select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result

    def findByID(self, id): # fetch the id number 
        cursor = self.getCursor()
        sql="select * from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

    def update(self, values):
        cursor = self.getCursor()
        sql="update student set name= %s, age=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        #print("delete done")

studentDAO = StudentDAO()