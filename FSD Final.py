#Import all the required modules
import time
from datetime import datetime  
from datetime import timedelta
import os
import getpass
global db
global name
global tpnum

#Decalring Username and Password
account1 = ["admin","admin"]
account2 = ["asd","123"]

#Function for the Login Page
def loginpage():
    uname = input("\nEnter Username: ")
    passw = getpass.getpass("Enter Password: ")
    if uname == account1[0] and passw == account1[1]:
        print("Login Successful")
        home()
    elif uname == account2[0] and passw == account2[1]:
        print("Login Successful")
        home()
    else:
        print("Wrong Username or Password")
        loginpage()

#Function to display the numbers of tenants on each apartment 
def status():
    print("\n[Apartment Availability]")
    print("Apartment A Normal tenant(s):",checkA())
    print("Apartment B Normal tenant(s):",checkB())
    print("Apartment B Master tenant(s):",checkBM())
    home()

#Function to Check the file dbA.txt and count the number of lines. Number of lines representing the number of tenants currently [dbA is database apartment A] 
def checkA():
    if os.path.isfile("dbA.txt"):
        fhand = open("dbA.txt", "r")
        count = 0
        for line in fhand:
            count = count + 1
        return count
    else:
        return 0
    fhand.close()

#Function to Check the file dbB.txt and count the number of lines. Number of lines representing the number of tenants currently [dbA is database apartment B Normal Room] 
def checkB():
    if os.path.isfile("dbB.txt"):
        fhand = open("dbB.txt", "r")
        count = 0
        for line in fhand:
            count = count + 1
        return count
    else:
        return 0
    fhand.close()

#Function to Check the file dbBM.txt and count the number of lines. Number of lines representing the number of tenants currently [dbA is database apartment B Master Room]     
def checkBM():
    if os.path.isfile("dbBM.txt"):
        fhand = open("dbBM.txt", "r+")
        count = 0
        for line in fhand:
            count = count + 1
        return count
    else:
        return 0
    fhand.close()

#Function to display all the available options on the home menu and ask the user for an input then redirect to the selected menu   
def home():
    print("\n[Home]")
    print("1. Check In")
    print("2. Check Out")
    print("3. Check Apartment Availability")
    print("4. Log Out")
    j = input("Select Option: ") 
    if j == "1":
        c_in()
    elif j == "2":
        c_out()
    elif j == "3":
        status()
    elif j == "4":
        print("\nLogged Out Successfully")
        loginpage()
    elif j == "0":
        home()
    else:
        print("Invalid Input")
        home()

#Function to tell the Date. Date(0) is today's date and Date(140) is 140 days after today's date. 
def Date(d):
    xd = (datetime.now().replace(microsecond=0) + timedelta(days=d)).strftime('%d-%m-%Y')
    return xd

#Function to ask the user to input the name of the student
def askname():
    name = input("Enter Student Name: ")
    return name

#Function to ask the user to input the TP number of the student
def asktpnum():
    tpnum = input("Enter TP number: ")
    return tpnum

#Function to open dbA.txt and write the student details to the file            
def writedbA(x, y, z):
    db = open("dbA.txt", 'a')
    content = str(x+" "+y+" "+z+"\n")
    db.write(content)
    db.close()

#Function to open dbB.txt and write the student details to the file            
def writedbB(x, y, z):
    db = open("dbB.txt", 'a')
    content = str(x+" "+y+" "+z+"\n")
    db.write(content)
    db.close()

#Function to open dbBM.txt and write the student details to the file            
def writedbBM(x, y, z):
    db = open("dbBM.txt", 'a')
    content = str(x+" "+y+" "+z+"\n")
    db.write(content)
    db.close()
    
#Function to open LogBook.txt and write the student details to the file            
def writedbH(v, w, x, y, z):
    db = open("LogBook.txt", 'a')
    content = str(v+" "+w+" "+x+" Check " +y+ " Date : "+z+"\n")
    db.write(content)
    db.close()

#Function Check In. Ask user to input which type of apartment and proceed with the check in for that specified Apartment    
def c_in():
    print("\n[Check In]")
    l = input("Select Type of Apartment [A or B] (Type 0 to go back to Home Menu)\nSelect Option: ").lower()
    if l == "0":
        home()   
    elif l == "a" :
        if checkA() >= 2 and checkB() >= 2 and checkBM() >= 1:
            print("All the Apartment are fully Booked")
            home()            
        elif checkA()>= 2:
            print("Apartment A is fully Booked, Try Apartment B")
            c_in()            
        elif checkA() < 2 :
            infoA()
            k = input("\nAre you sure? [Yes or No]\nSelect Option: ").lower()
            if k == "y" or k == "yes":
                name = askname()
                tpnum = asktpnum()
                print(name,"has  to pay RM300 (Deposit) + RM100 (Utilities) + RM300 (1st Rent)")
                print("For a total of RM700")
                paid = input("Confirm  Payment [Yes or No]\nSelect Option: ").lower()
                if paid == "y" or paid == "yes":
                    writedbA(name, tpnum, Date(0))
                    print("Successfully registered at "+Date(0))
                    print(name,"Must Check Out by "+Date(140))
                    writedbH(name, tpnum, "Apartment A", "In", Date(0))
                    home()
                else:
                    print("Registration Fail!")
                    c_in()
            elif k == "n" or k == "no":
                c_in()
            else:
                print("Invalid Input")
                c_in()
            
    elif l == "b" :
        if checkA() >= 2 and checkB() >= 2 and checkBM() >= 1:
            print("All the Apartment are fully Booked")
            home()

        elif checkB() >= 2 and checkBM() >= 1:
            print("Apartment B is fully Booked try Apartment A")
            c_in()
        elif checkB() < 2 or checkBM() <= 0:
            infoB()
            k = input("\nAre you sure? [Yes or No]\nSelect Option: ").lower()

            if k == "y" or k == "yes":
                name = askname()
                tpnum = asktpnum()
                print(name,"has  to pay RM200 (Deposit) + RM100 (Utilities) + RM200 (1st Rent)")
                print("For a total of RM500")
                print("\nFor the master room, student has to pay additional 40% more cost. The total for master room is 820RM")
                master_confirm = input("1. Normal Room\n2. Master Room\nSelect Option: ").lower()
                if (master_confirm == "2"):
                    if (checkBM() <= 0):
                        print ("You have to pay 660RM")
                        paid = input("Confirm  Payment [Yes or No]").lower()
                        if paid == "y" or paid == "yes":
                            writedbBM(name, tpnum, Date(0))
                            print("Successfully registered at "+Date(0))
                            print(name,"Must Check Out by "+Date(140))
                            writedbH(name, tpnum, "Apartment B Normal", "In", Date(0))
                            home()
                        else:
                            print("Registration Fail!")
                            c_in()
                            
                    elif (checkBM() >= 1) and (checkB() < 2):
                        print ("Master room already full, only normal room available")
                        confirmN = input("Confirm Normal Room [Yes or No]\nSelect Option: ").lower()
                        if confirmN == "yes" or confirmN == "y":
                                print ("You have to pay 500 RM")
                                paid = input("Confirm  Payment [Yes or No]\nSelect Option: ").lower()
                                if paid == "y" or paid == "yes":
                                    writedbB(name, tpnum, Date(0))
                                    print("Successfully registered at "+Date(0))
                                    print(name,"Must Check Out by "+Date(140))
                                    writedbH(name, tpnum, "Apartment B Master", "In", Date(0))
                                    home()
                                elif paid == "n" or paid == "no":
                                    print("Registration Fail!")
                                    c_in()
                        else:
                            print("Registration Fail!")
                            c_in()
                                    
                    elif (checkBM() >= 1) and (checkB() >= 3):
                        print ("Apartment B is fully Booked try Apartment A")
                        c_in()
                        
                    else:
                        print("Registration Fail!")
                        c_in()
                        
                elif (master_confirm == "1"):
                    if (checkB() < 2):
                        print ("You have to pay 500RM")
                        paid = input("Confirm  Payment [Yes or No]\nSelect Option: ").lower()
                        if paid == "y" or paid == "yes":
                            writedbB(name, tpnum, Date(0))
                            print("Successfully registered at "+Date(0))
                            print(name,"Must Check Out by "+Date(140))
                            home()
                        elif paid =="n" or paid =="no":
                            print ("registration fails!")
                            c_in()
                            
                    elif (checkB() > 2) or (checkBM() <= 0):
                        print ("Only master room is available\nYou have to pay 820RM")
                        paid = input("Confirm  Payment [Yes or No]\nSelect Option: ").lower()
                        if paid == "y" or paid == "yes":
                            writedbBM(name, tpnum, Date(0))
                            print("Successfully registered at "+Date(0))
                            print(name,"Must Check Out by "+Date(140))
                            home()
                        elif paid == "n" or paid == "no":
                            print("Registration fails!")
                            c_in
                    else:
                        print("Apartment B is fully Booked try Apartment A")
                        c_in()
                else:
                    print("Registration Fails!")
                    c_in()
            elif k == "n" or k == "no":
                c_in()
            else:
                print("Invalid Input")
                c_in()
    else :
        print("Invalid input")
        c_in()

#Function to Check Out. Ask user to enter apartment type and proceed to check out
def c_out():
    print("\n[Check Out]")
    apartype = input("Select Type of Apartment [A or B] (Type 0 to go back to Home Menu)\nSelect Option: ")
    if apartype == "a" or apartype == "A":
        name = input("Name : ")
        TP = input("TP Number : ")
        Cin = input("Check In Date (DD-MM-YYYY) : ")
        res = str(name+" "+TP+" "+Cin)
        e = open("dbA.txt", "r")
        lines2 = e.readlines()
        e.close()
        f = open("dbA.txt")
        lines = f.read().splitlines()
        f.close()
        tenantA = checkA()
        
        #Open the file and re write the contents wihout the specified data (To create the ilussion of deleting the data)
        d = open("dbA.txt", "w")
        for line in lines2:
            if line != res+"\n":
                d.write(line)
        d.close()
        if tenantA > checkA():
            print("Checked Out Successfully")
            writedbH(name, TP, "Apartment A Normal", "Out", Date(0)) #write to the LogBook
            home()
        else:
            print("No Matching Data")
            c_out()

    elif apartype == "b" or apartype == "B":
        apartypeB = input("1. Normal Room\n2. Master Room\nSelect Option: ")
        if apartypeB == "1":
            name = input("Name : ")
            TP = input("TP Number : ")
            Cin = input("Check In Date (DD-MM-YYYY) : ")
            res = str(name+" "+TP+" "+Cin)
            e = open("dbB.txt", "r")
            lines2 = e.readlines()
            e.close()
            f = open("dbB.txt")
            lines = f.read().splitlines()
            f.close()
            tenantB = checkB()
            
            #Open the file and re write the contents wihout the specified data (To create the ilussion of deleting the data)
            d = open("dbB.txt", "w")
            for line in lines2:
                if line != res+"\n":
                    d.write(line)
            d.close()
            if tenantB > checkB():
                print("Checked Out Successfully")
                writedbH(name, TP, "Apartment B Normal", "Out", Date(0))
                home()
            else:
                print("No Matching Data")
                c_out()

        elif apartypeB == "2":
            name = input("Name : ")
            TP = input("TP Number : ")
            Cin = input("Check In Date (DD-MM-YYYY) : ")
            res = str(name+" "+TP+" "+Cin)
            e = open("dbBM.txt", "r")
            lines2 = e.readlines()
            e.close()
            f = open("dbBM.txt")
            lines = f.read().splitlines()
            f.close()
            tenantBM = checkBM()
            
            #Open the file and re write the contents wihout the specified data (To create the ilussion of deleting the data)
            d = open("dbBM.txt", "w")
            for line in lines2:
                if line != res+"\n":
                    d.write(line)
            d.close()
            if tenantBM > checkBM():
                print("Checked Out Successfully")
                writedbH(name, TP, "Apartment B Master", "Out", Date(0))
                home()
            else:
                print("No Matching Data")
                c_out()

    elif apartype == "0":
        home()
    else:
        print("Invalid Input")
        home()

#Function to display Apartment B Details and Pricing        
def infoA():
    print("\nApartment Type A,  2 bedrooms and equiped with kitchen and laundry facilities.")
    print("The monthly rental for the rooms in this apartment type is RM300.")

#Function to display Apartment B Details and Pricing
def infoB():
    print ("\nApartment Type B, 3 bedrooms includes one master bedroom with attached bathroom but does not have kitchen and laundry facilities.")
    print ("The monthly rental for the rooms in this apartment type is RM200 and students staying in the master bedroom will be paying an additional 40%")    

print ("welcome to University Apartment Manager")
print(Date(0))#Display Today's Date
loginpage()
