import mysql.connector

#connection code
con=mysql.connector.connect(
    host="localhost",
    user="Username",
    password="Your_my_SQL_Password",
    database="expense_db"
)
cur=con.cursor()

#1.expenses added
def add_expense():
    amt=float(input("Enter the amount:"))
    catg=input("entery category:")
    desc=input("Enter details: ")
    query="""
    INSERT INTO expenses(amount,category,description)
    VALUES(%s,%s,%s)
    """
    values=(amt,catg,desc)
    cur.execute(query,values)
    con.commit()
    print("Expenses added successfully")

def view_expense():
    cur.execute("select * from expenses ")
    records=cur.fetchall()
    if not records:
        print("No records found")
    else:
        print("-" * 60)
        print(f"{'ID':<5}{'AMOUNT':<12}{'CATEGORY':<15}{'DESCRIPTION':<25}")
        print("-" * 60)

        for i in records:
            print(f"{i[0]:<5}{i[1]:<12}{i[2]:<15}{i[3]:<25}")

        print("-" * 60)
def total_spending():
    cur.execute("SELECT SUM(amount) as totalspending FROM expenses  ")
    record=cur.fetchone()
    print("total spending",record[0])
    
def delete_expenses():
    cur.execute("select * from expenses ")
    records=cur.fetchall()
    print("-" * 60)
    print(f"{'ID':<5}{'AMOUNT':<12}{'CATEGORY':<15}{'DESCRIPTION':<25}")
    print("-" * 60)
    for i in records:
        print(f"{i[0]:<5}{i[1]:<12}{i[2]:<15}{i[3]:<25}")
    print("-" * 60)
    
    student_id=int(input("Enter id to delete:"))
    query="""
    DELETE FROM expenses WHERE ID=%s
    """
    val=(student_id,)
    cur.execute(query,val)
    con.commit()
    
    if cur.rowcount > 0:
        print("Deleted Successfully")
    else:
        print("Expense ID not found")
    
def update_expense():
    student_id=int(input("Enter the id:"))
    amt=float(input("Enter the amount:"))
    catg=input("Enter category:")
    desc=input("Enter details: ")
    query="""
    UPDATE expenses SET amount=%s,category=%s,description=%s
    WHERE ID=%s
    """
    values=(amt,catg,desc,student_id)
    cur.execute(query,values)
    con.commit()
    if cur.rowcount > 0:
        print("Updated Successfully")
    else:
        print("Expense ID not found")

print("----------Expense Tracker------------------")

while True:
    print("1-Add your Expense\n 2-View your Expenses\n 3-total Spending\n 4-Delete the Expense \n 5-Update your Expense\n 6-Exit")
    op=int(input("Enter your Choice:"))
    if op==1:
        add_expense()
    elif op==2:
        view_expense()
    elif op==3:
        total_spending()
    elif op==4:
        delete_expenses()
    elif op==5:
        update_expense()
    elif op==6:
        break
    else:
        print("invalid!")
