emp = {101:{"name":"Raj","age":12,"dep":"sales","salary":23000},
       }

def add_emp():
    try:
        emp_id=int(input("Enter the  emolyee id:"))
        if emp_id in emp:
            print("employee id already exists. try  again.")
            return
        name = input("enter the name:")
        age = int(input("enter the age:"))
        dep = input("enter the department:")
        salary = float(input("enter the salary:"))

        emp[emp_id]={
            "name":name,
            "age":age,
            "department":dep,
            "salary":salary
            }
        print("Employee added successfully!")
    except ValueError:
        print("Invalid input!Please enter the correct data types.")

def view_emp():
    if not emp:
        print("No employee record found.")
        return
    for emp_id,details in emp.items():
        print(f"\nID:{emp_id}")
        print(f"Name:{details['name']}")
        print(f"Age:{details['age']}")
        print(f"Department:{details['dep']}")
        print(f"salary:{details['salary']}")
        print("-"*30)

def search_emp():
    try:
        emp_id = int(input("enter employee id to search:"))
        if emp_id in emp:
            details = emp[emp_id]
            print(f"\nID:{emp_id}")
            print(f"name:{details["name"]}")
            print(f"age:{deatils["age"]}")
            print(f"dep:{deatils["dep"]}")
            print(f"salary:{deatils["salary"]}")
        else:
            print("employee not found .")
    except ValueError:
        print("Invalid input!please enter a number.")
            

def main():
    while True:
        print("\n--- Employee Management System---")
        print("1. add employee")
        print("2. view all employee ")
        print("3. search for employee ")
        print("4. exit")

        choice = input("enter the choice (1-4):")

        if choice  =="1":
            add_emp()
        elif choice =="2":
            view_emp()
        elif choice =="3":
            search_emp()
        elif choice=="4":
            print("Existing the program. bye!")
            break
        else:
            print("invalid choice!please select valid option.")

if __name__ == "__main__":
    main()
