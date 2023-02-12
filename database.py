import mysql.connector as c


con=c.connect(host="localhost",user="root",passwd="1234",database="tajakka")
if con.is_connected():
    cursor = con.cursor()
    var= True
else:
    print("not connected")
    var =False

class Database:

    def __init__(self):
        if var == True :
            sql="""
                CREATE TABLE IF NOT EXISTS Employee(
                    id text,
                    name text,
                    age text,
                    doj text,
                    email text,
                    gender text,
                    contact text,
                    address text
                );
            """
            cursor.execute(sql)
            con.commit()
            print("table created successfully")

    def insert(self,e_id,e_name,e_age,e_doj,e_email,e_gender,e_contact,e_address):
        query="""
        INSERT INTO Employee(id,name,age,doj,email,gender,contact,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        record=(e_id,e_name,e_age,e_doj,e_email,e_gender,e_contact,e_address)
        # query="""
        # INSERT INTO Employee(id,name,age,doj,email,gender,contact,address) VALUES (5,'taj',20,'2011-11-11','tajakka2002@gmail.com','female','01753861142','house2,road 31,block D');
        # """
        cursor.execute(query,record)
        con.commit()
        print("inserted successfully\n")

    def update(self,e_id,e_name,e_age,e_doj,e_email,e_gender,e_contact,e_address):
        query = """
                 update employee set name=%s, age=%s, doj=%s, email=%s, gender=%s, contact=%s, address=%s where id=%s
                """

        record = (e_name,e_age,e_doj,e_email,e_gender,e_contact,e_address,e_id)
        cursor.execute(query, record)
        con.commit()
        print("updated successfully\n")

    def search(self,e_id):
        query = """
                    SELECT * from Employee WHERE id=%s
                """

        record = None
        cursor.execute(query,(e_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0] )
            print("Name = ", row[1])
            print("Age = ", row[2])
            print("Join Date  = ", row[3])
            print("Email  = ", row[4])
            print("Gender  = ", row[5])
            print("Contact  = ", row[6])
            print("Address  = ", row[7])
        con.commit()
        print("-----------------------------------------------------------")
        if len(record)==0:
            print("No results found\n")
        else :
            print("search results are given\n")

    def fetch(self):
        query = """
                            SELECT * from Employee
                """
        cursor.execute(query)
        record = cursor.fetchall()
        print("Total number of employees: ", cursor.rowcount)
        # i=int(0)
        # t=[[],[]]
        for row in record:
            print("Id = ", row[0] )
            print("Name = ", row[1])
            print("Age = ", row[2])
            print("Join Date  = ", row[3])
            print("Email  = ", row[4])
            print("Gender  = ", row[5])
            print("Contact  = ", row[6])
            print("Address  = ", row[7],"\n")
            # t=t.insert(i,[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
            print("-----------------------------------------------------------")
        if len(record) == 0:
            print("No results found\n")
        else:
            print("search results are given\n")
            # print(tabulate(t, headers=["Id", "Name", "Age", "Join Date", "Email", "Gender", "Contact", "Address"]))
            # print(t)
    def remove(self,e_id):
        query = """
                     Delete from Employee where id=%s
                """
        cursor.execute(query,(e_id,))
        con.commit()
        print('number of rows deleted ', cursor.rowcount)

