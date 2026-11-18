class Employee:
    company = "DataPulse Analytics"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"Company    : {Employee.company}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary     : ${self.salary:,.2f}")
        print("-----------------------------")

    def annual_bonus(self):
        bonus = self.salary * 0.10
        print(f"Annual bonus for {self.name}: ${bonus:,.2f}")
        print("-----------------------------")


print("=== Enter Employee 1 ===")
name1 = input("Employee name: ")
department1 = input("Department: ")
salary1 = float(input("Monthly salary: "))

print("\n=== Enter Employee 2 ===")
name2 = input("Employee name: ")
department2 = input("Department: ")
salary2 = float(input("Monthly salary: "))

employee1 = Employee(name1, department1, salary1)
employee2 = Employee(name2, department2, salary2)

employee1.display_info()
employee1.annual_bonus()
employee2.display_info()
employee2.annual_bonus()
