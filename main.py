def menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Show Total Spent")
    print("5. Delete Expense")
    print("6. Exit")

def load_expenses():
    try:
        with open("expenses.txt", "r") as f:
            lines=f.readlines()
        expenses=[]
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            expenses.append([parts[0], int(parts[1]), parts[2]])
        return expenses
    except:
        return []

def save_expenses(expenses):
    with open("expenses.txt", "w") as f:
        for exp in expenses:
            f.write(exp[0]+","+str(exp[1])+","+exp[2]+"\n")
    
def add_expense(expenses):
    category=input("Enter category: ").strip().title()
    if category=="":
        print("Category cannot be empty")
        return
    try:
        amount=int(input("Enter amount: "))
    except ValueError:
        print("Invalid amount")
        return
    if amount<=0:
        print("Amount must be positive")
        return
    date=input("Enter date (YYYY-MM-DD): ").strip()
    if date=="":
        print("Date cannot be empty")
        return
    elif len(date)!=10:
        print("Invalid date format")
        return
    expenses.append([category, amount, date])
    save_expenses(expenses)
    print("Expense added")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found")
        return
    for i in range(len(expenses)):
        print(str(i+1)+". "+expenses[i][0]+" - "+str(expenses[i][1])+" - "+expenses[i][2])
    
def filter_by_category(expenses):
    if not expenses:
        print("No expenses found")
        return
    category=input("Enter category: ").strip().title()
    found=False
    for exp in expenses:
        if exp[0]==category:
            print(exp[0]+" - "+str(exp[1])+" - "+exp[2])
            found=True
    if not found:
        print("No matching expenses")
    
def show_total(expenses):
    total=0
    for exp in expenses:
        total+=exp[1]
    print("Total spent:", total)

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index=int(input("Enter number to delete: "))-1
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower()!="y":
            print("Cancelled")
            return
    except ValueError:
        print("Invalid input")
        return
    if 0<=index<len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
        print("Deleted")
    else:
        print("Invalid index")

expenses=load_expenses()
while True:
    menu()
    choice = input("Choose: ")
    if choice=="1":
        add_expense(expenses)
    elif choice=="2":
        view_expenses(expenses)
    elif choice=="3":
        filter_by_category(expenses)
    elif choice=="4":
        show_total(expenses)
    elif choice=="5":
        delete_expense(expenses)
    elif choice=="6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")