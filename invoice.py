import pymysql
from tabulate import *
db=pymysql.connect("localhost","root","root","invoice" )
cur = db.cursor()

ab=[]

    
def  display(e_id,b,q):
    print()
    cur.execute("select * from user where email_id=%s",(e_id))
    a = cur.fetchone()
    cur.execute("select * from product where bill_id=%s",(b))
    b=cur.fetchone()
    print("=================================================================================")
    print()
    print("-------------------------------------INVOICE-------------------------------------")
    print()
    print("Id : ",a[0])
    print("Name : ",a[1])
    print("Address :",a[2])
    print("Mobile no : ",a[3])
    print("Email Id : ",a[4])
    print("Bill Id : ",b[0])
    while b is not None:
        ab.append(list(b[2:6]))
        a=b[6]
        b=cur.fetchone()
    headers = [ "Item","Quantity","Unit price","Amount"]
    print(tabulate(ab, headers, tablefmt="orgtbl"))
    print("Total Amount : ",a)
    print()
    print("================================================================================")
    print()

def detail_cus():
    global n,s,mob,e
    n=input("Name :")
    s=input("Address :")
    mob=int(input("Mobile :"))
    e=input("Email id :")
    print()
    cur.execute("insert into user (customer_name,address,mobile_no,email_id) values (%s,%s,%s,%s)",(n,s,mob,e))
    db.commit()

def detail_prod():
    global i,q,u,a,e_id,b
    e_id=input("Email id : ")
    cur.execute("select * from user where email_id=%s",(e_id))
    d=cur.fetchone()
    if(d == None):
        print("Not found!")
    else:
        b=int(input("Enter bill id : "))
        q=int(input("Enter no of items:"))
        t_a=0
        for i in range(q):
            i=input("Item :")
            q=int(input("Quantity :"))
            u=int(input("Unit Price :"))
            a=u*q
            t_a=t_a+a
            cur.execute("insert into product (email_id,bill_id,item,quantity,unit_price,amount) values (%s,%s,%s,%s,%s,%s)",(e_id,b,i,q,u,a))
        cur.execute("update product set total_amount=%s where bill_id=%s",(t_a,b))
        display(e_id,b,q)
        
    db.commit()
    

def main():
    print("******************************** Invoice Generator ************************************")
    print()
    while(True):
        print("If you are an existing user then press Y/y and if not press N/n.")
        print("If you want to exit press E/e.")
        n=input("")
        print()
        if(n == "Y" or n=="y"):
            detail_prod()
        elif(n == "N" or n=="n"):
            detail_cus()
        elif(n == "E" or n == "e"):
            break;
        else:
            print("Invalid")
            print()
main()
