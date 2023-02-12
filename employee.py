from database import *
def menu():
    print ("-----------------------------------------------------------")
    print ("-----------------------------------------------------------")
    print ("|             Employee Management System                  |")
    print ("-----------------------------------------------------------")
    print ("-----------------------------------------------------------")
    print ("\n")
    # print ("***********************************************************")
    print ("-->                  1.Add Employee                     <--")
    # print ("***********************************************************")
    # print ("***********************************************************")
    print ("-->              2.Update Employee Records              <--")
    # print ("***********************************************************")
    # print ("***********************************************************")
    print ("-->               3.Search Employee Records             <--")
    # print ("***********************************************************")
    # print ("***********************************************************")
    print ("-->               4.Display Employee Records            <--")
    print ("-->                5.Remove Employee                    <--")
    print ("-->                   6.Exit                            <--")
    print ("\n")
    print ("\n")
    print ("-->        Choose one of the options [1/2/3/4/5/6]      <--")
    print ("\n")
    db=Database()
    while True:
        option=int(input("-----------Please Enter your desired option here -----------\n"))
        if option==7 :
            break

        elif option ==1 :
            id=int(input("Enter Employee ID : "))
            name= input("Enter  Name : ")
            age=int(input("Enter  age : "))
            doj= input("Enter your date of join : ")
            email= input("Enter your email id : ")
            gender= input("Enter your gender : ")
            contact= input("Enter your contact No : ")
            address= input("Enter your address : ")
            db.insert(id,name,age,doj,email,gender,contact,address)

        elif option == 2:
            id = int(input("Enter Employee ID : "))
            name = input("Enter  Name : ")
            age = int(input("Enter  age : "))
            doj = input("Enter your date of join : ")
            email = input("Enter your email id : ")
            gender = input("Enter your gender : ")
            contact = input("Enter your contact No : ")
            address = input("Enter your address : ")
            db.update(id, name, age, doj, email, gender, contact, address)

        elif option == 3:
            id = int(input("Enter Employee ID : "))
            db.search(id)

        elif option == 4:
            db.fetch()

        elif option == 5:
            id = int(input("Enter Employee ID : "))
            db.remove(id)


# print ("***********************************************************")

menu()