# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:04:48 2022

@author: Rk verma
"""


class Food_add_upd_del:
    def __init__(self):         # Add update
        sql = "select * from food;"
        cur.execute(sql)
        res = cur.fetchall()                           # fetching the food id's
        print("\n\t\tMenu\n")           
        l = []
        self.l=l
        menulst_fooditem=[]
        menulst_price=[]
        for i in range(len(res)):
            l.append(res[i][0])
            menulst_fooditem.append(res[i][1])
            menulst_price.append(res[i][2])
        dict_foodmenu={"Food ID" : l, "Food Items" : menulst_fooditem, "Price" : menulst_price}
        headmenu=dict_foodmenu.keys()
        print(tabulate(dict_foodmenu,headers=headmenu,tablefmt='grid'))
        print("1. Add food items and prices to database \n2. Update prices of food items \n3. Delete any food item")
        while True:
            au_inp=input("Enter the number for the respective process or type '0' to proceed to main menu: ")
            if au_inp.isdigit():
                au_inp=int(au_inp)
                if au_inp==1:
                    self.new_food(l)
                elif au_inp==2:
                    self.update_foodcost(l)
                elif au_inp==3:
                    self.delete_fooditems(l)
                elif au_inp==0:
                    break
                    main()
            else:
                print("Please enter an integer value according to the given operation")

    def new_food(self,l):           # adding ne4w food items to menu
        x=input("How many food items do you want to enter : ")
        i = 1
        if x.isdigit():
            x=int(x)
            print("Please enter integer values for food id as well as for price and alphabets or string values for product name.")
            while i<=x:
                serial_no = input('Food ID :')
                dish_name = input('Product Name :')
                price = input('Price :')
                if serial_no.isdigit() and price.isdigit() and dish_name.isalpha():
                    serial_no=int(serial_no)
                    price=int(price)
                    if serial_no<=max(self.l) and serial_no>=min(self.l):
                        print("The entered food id already exists. Please enter a new id...")
                        continue
                    else:
                        qry1 = "INSERT INTO food values({}, '{}', {})".format(serial_no, dish_name, price)
                        cur.execute(qry1)
                        conn.commit()
                        i+=1
                        print("data added")
                else:
                    print("Invalid input! \nPlease check the values before entering...")
        else:
            print("Invalid input! \nPlease enter integer value before entering for the number of items to be stored...")

    def delete_fooditems(self,l):
        while True:
            del_no=input("Enter food id of the respective food item to be deleted or type '0' to go back : ")
            if del_no.isdigit():
                del_no=int(del_no)
            
                if del_no==0:
                    break
                elif del_no<=max(self.l) and del_no>=min(self.l):
                    cur.execute("DELETE FROM food WHERE serial_no={};".format(del_no))
                    conn.commit()
                    print("data successfully deleted")  
            else:
                print("Invalid input! \nPlease enter a valid input.")                
                continue
            

    def update_foodcost(self,l):                   #update food cost
        while True:
            upd_no=input("Enter food id of the respective food item to be updated or type '0' to go back : ")
            if upd_no.isdigit():
                upd_no=int(upd_no)
                if upd_no==0:
                    break
                elif upd_no<=max(self.l) and upd_no>=min(self.l):
                    amt_upd=int(input("Enter the amount to be updated : "))
                    cur.execute("UPDATE food SET price={} WHERE serial_no={};".format(amt_upd,upd_no))
                    conn.commit()
                    print("data successfully updated") 
            else:
                print("Invalid input! \nPlease enter a valid input.")
                continue
            
            
def food_order():                            # food order
    sql = "select * from food;"
    cur.execute(sql)
    res = cur.fetchall()                           # fetching the food id's
    print("\n\t\tMenu\n")           
    l = []
    menulst_fooditem=[]
    menulst_price=[]
    for i in range(len(res)):
        l.append(res[i][0])
        menulst_fooditem.append(res[i][1])
        menulst_price.append(res[i][2])
    dict_foodmenu={"Food ID" : l, "Food Items" : menulst_fooditem, "Price" : menulst_price}
    headmenu=dict_foodmenu.keys()
    print(tabulate(dict_foodmenu,headers=headmenu,tablefmt='grid'))    
    lst_price = []
    lst_fooditem=[]
    lst_foodid=[]
    lst_qty=[]
    net_qty=[]
    conn.commit()

    while True:
        order_sno=input("Enter food number for order, type '1' to proceed or type '0' to cancel: ")
        if order_sno.isdigit():
            order_sno=int(order_sno)
            if order_sno==0:
                break
                main()
            
            elif order_sno<=max(l) and order_sno>=min(l):
                qty=int(input("Enter how much quantity do you want: "))
                sql = "SELECT * FROM food WHERE serial_no={};".format(order_sno)
                cur.execute(sql)
                abc = cur.fetchone()
                lst_foodid.append(abc[0])
                lst_fooditem.append(abc[1])
                lst_price.append(abc[2])
                lst_qty.append(qty)
                net_qty.append(abc[2]*qty)
                continue
            
            elif order_sno==1:
                if len(lst_foodid)==0:
                    #head=["Food ID", "Food Items", "Price"]
                    dict_food={"Food ID" : lst_foodid, "Food Items" : lst_fooditem, "Price" : lst_price, "Quantity" : lst_qty, "Net Quantity" : net_qty}
                    head=dict_food.keys()
                    print(tabulate(dict_food,headers=head,tablefmt='grid'))         #### show lst1 in table
                    print(f"Total price : {sum(net_qty)}")
                    print("Please enter the respective food id for required food")
                    continue

                else:
                    dict_food={"Food ID" : lst_foodid, "Food Items" : lst_fooditem, "Price" : lst_price, "Quantity" : lst_qty, "Net Quantity" : net_qty}
                    head=dict_food.keys()                    
                    now = datetime.now()
                    today = now.strftime("%d/%m/%Y %H:%M:%S")
                    
                    print("Date and time : ", today)
                    print(tabulate(dict_food,headers=head,tablefmt='grid'))         #### show lst1 in table
                    print(f"Total price : {sum(net_qty)}")
                    
                    new_dictfood=dict_food.copy()
                    new_dictfood["Date"] = today
                    with open("t_sales.csv",'a') as f:
                        f.writelines(f"{abc[0]},{abc[1]},{abc[2]},{qty},{abc[2]*qty},{today}\n")
                    print("Order stored into csv file...")
                    break
            else:
                print("Invalid input... Please check the value entered as food id")
        else:
            print("Please enter an integer value...")

######


# display Employee menu
class Employee:
    def __init__(self):
        print("Welcome to Employee Management Record")
        print("Press ")
        print("1 to Add Employee")
        print("2 to Remove Employee ")
        print("3 to Increase Employee Salary")
        print("4 to Display Employees")
        print("5 to Exit")
 
        ch = input("Enter your Choice: ")
        if ch.isdigit():
            ch=int(ch)
            if ch == 1:
                self.Add_Employ()
            elif ch == 2:
                self.Remove_Employ()
            elif ch == 3:
                self.increaseSalary()
            elif ch == 4:
                self.Display_Employees()
            elif ch == 0:
                main()
            else:
                print("Invalid Choice")
        
    def Add_Employ(self): 
        Emp_Id = input("Enter Employee Id : ")     
        # Checking if Employee with given Id Already Exist or Not
        if(self.check_employee(Emp_Id) == True):
            print("Employee aready exists\nTry Again\n")
            Employee()
         
        else:
            Emp_Id = int(input("Enter Employee Id :"))
            Name = input("Enter Employee Name : ")
            Gender = input("Enter Gender: ")
            City = input("Enter City Name: ")
            Post = input("Enter Employee Designation : ")
            Salary = int(input("Enter Employee Salary : "))
            data = (Emp_Id, Name, Gender, City, Post, Salary)
            sql = 'insert into empd values(%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, data)
            conn.commit()
            print("Employee Added Successfully ")
            Employee()

# Function to Promote Employee
    def increaseSalary(self):
        Emp_Id = int(input("Enter Employ's Id"))
     
        # Checking if Employee with given Emp_Id Exist or Not
        if(self.check_employee(Emp_Id) == False):
            print("Employee does not  exists\nTry Again\n")
            Employee()
        else:
            Amount = int(input("Enter increase in Salary: "))
            sql = 'select salary from empd where EMPL_ID=%s'
            data = (Emp_Id,)
            cur = conn.cursor()
            cur.execute(sql, data)
            r = cur.fetchone()
            t = r[0]+Amount
            sql = 'update empd set salary=%s where EMPL_ID=%s'
            d = (t, Emp_Id)        
            cur.execute(sql, d)
            conn.commit()
            print("Employee Salary Increased by",Amount)
            Employee()

    def Remove_Employ(self):
        Emp_Id = input("Enter Employee Id : ")
        # Checking if Employee with given Id Exist or Not
        if(self.check_employee(Emp_Id) == False):
            print("Employee does not exists\nTry Again\n")
            Employee()
        else:
            sql = 'delete from empd where EMPL_ID=%s'
            data = (Emp_Id,)
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            print("Employee Removed")
            Employee()
 
 
# Function To Check if Employee with given Emp_Id Exist or Not
    def check_employee(self,employee_id):
        sql = 'select * from empd where EMPL_ID=%s'
        cur = conn.cursor()
        data = (employee_id,)
        cur.execute(sql, data)
        r = cur.rowcount
        if r == 1:
            return True
        else:
            return False

# Function to Display All Employees from Employee Table
    def Display_Employees(self):
        sql = 'select * from empd'
        cur = conn.cursor()
        cur.execute(sql)
        r = cur.fetchall()
    
        for i in r:
            print("Employee Id : ", i[0])
            print("Employee Name : ", i[1])
            print("Employee Designation : ", i[2])
            print("Employee Salary : ", i[3])
            print("------------------------")
         
        Employee()
   
        


class Customer:
    def __init__(self):
        while True:
            print("1. Enter customer data \n2. Show customer data")
            inpc=input("Enter the number to perform respective function or press '0' for main menu': ")        
            if inpc.isdigit():           
                inpc=int(inpc)        
                if inpc==1:
                    self.cust_enter()               
                elif inpc==2:
                    self.cust_retrieve()
                elif inpc==0:
                    break                
                else:
                    print("Please enter correct value to perform particular operation.")
               
    def cust_enter(self):
        i=1
        o=input("Enter number of customer to be added: ")        
        if o.isdigit():
            o=int(o)
            while i<=o:
                print("Enter integer values for customer id as well as phone number and alphabets for name.\n")
                self.cust_id = input("Enter Customer Id:")
                self.name = input("Enter Customer Name: ")
                self.phone = input("Enter Customer Mobile No.: ")
                i+=1
                if self.cust_id.isdigit() and self.phone.isdigit():
                    self.cust_id=int(self.cust_id)
                    self.phone=int(self.phone)
                    cust = "INSERT INTO customer values({}, '{}', {})".format(self.cust_id, self.name, self.phone)
                    cur.execute(cust)
                    conn.commit()
                    print("Customer data entered successfully")                                               
                else: 
                    print("Please re-enter appropriate values.\n\n")        
        else:
            print("Please enter digit...")
           
    def cust_retrieve(self):
        cur.execute("SELECT * FROM customer;")
        cust_data=cur.fetchall()
        df=pd.DataFrame(data=cust_data,columns=["Customer ID","Name","Phone"])  
        print(df)
        

                
def open_sales_csv():
    df = pd.read_csv('t_sales.csv')
    print(df)

###################### -- Main code
from termcolor import colored     # for colouring strings.
import pandas as pd               # to display data in tabular form.
import psycopg2                   # package to connect python with postgresql
import psycopg2.extras
from tabulate import tabulate
from datetime import date, datetime


conn = psycopg2.connect(database="postgres", user='postgres', password="123456789", host='localhost', port= '5432')
#Creating a cursor object using the cursor() method
cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
qry = ''' CREATE TABLE IF NOT EXISTS food(food_id Integer PRIMARY KEY NOT NULL,
     Food_Item CHAR(20) NOT NULL,
     PRICE Integer NOT NULL
     )'''
cur.execute(qry)
conn.commit()


qry4 =''' CREATE TABLE IF NOT EXISTS Customer(Customer_id Integer PRIMARY KEY NOT NULL,
     CUST_NAME VARCHAR(30) NOT NULL,
     CUST_PHONE BIGINT 
     )'''
cur.execute(qry4)
conn.commit()


qry2 = '''CREATE TABLE IF NOT EXISTS empd(EMPL_ID Integer PRIMARY KEY NOT NULL,
     EMPL_NAME VARCHAR(30) NOT NULL,
     GENDER CHAR(8) NOT NULL,
     CITY VARCHAR(30) NOT NULL,
     EMPL_DESIGNATION VARCHAR(30),
     SALARY INTEGER 
     )'''
cur.execute(qry2)

################################
# food_aud=Food_add_upd_del()
def main():
    while True:
        head_text = colored('RESTAURANT MANAGEMENT SYSTEM', 'red', attrs=['reverse', 'blink'])
        print(head_text)
        print("1. Food Order and Billing \n2. Add or Update Food Items \n3. Employee Management \n4. Customer Management \n5. Open Sales Data")
        inp=input("Enter the number to perform respective function : ")    
        if inp.isdigit():        
            inp=int(inp)    
            if inp==1:
                food_order()
            elif inp==2:
                Food_add_upd_del()
            elif inp==3:
                Employee()
            elif inp==4:
                Customer()
            elif inp==5:
                open_sales_csv()
            elif inp==0:
                break
        else:
            print("invalid input... \nPlease enter a valid input")
            continue
        
################################


print("Welcome to DAIICT Restaurant")
main()