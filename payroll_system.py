#BRIAN'S PAYROL SYSTEM
#Build byBrian - Nov -14 - payroll for top tier
#This calculates,salary, tax, bonus for employees


employees = []

def calculate_tax(salary)
    if salary <= 20000:
         return salary *  0.1
    elif sala

   salary <= 50000:
        return salary * 0.2
  else:
       return salary *0.3
def calculator_bonus(years, salary)"
if year >= 5:
    return salary * 0.15
elif years >= 2:
     return salary * 0.10
else:
     return 0

 
print("=== BRIAN'S PAYROLL SYSTEM ===")


While True:
    print"\n1. add employe")
    print("2. view payroll Report")
    print("3. Search Employee")
    print9"4('Exit")
    choice = input("Pick 1 -4:"

    if choice == "2":
        name = input("Employee name: ")
        role = input("Role (manager/staff/intern): ").lower()
        salary = float(input("Basic Salary KES: "))
        years = int(input("Years worked: "))
        tax = calculate_tax(salary)
        bonus = calculate_bonus(years, salary)
        net = salary - tax + bonus
        employees.append({"name"})
        print(f"Added{name} | Net Pay: KES  {net}")

     elif choice == "2":
         print("---PAYROLL REPORT ---")
         if len(employees) == 0:
             print("No employees yet!")
     else:
          total_score = 0
          for e in employees:
             print(f"{e['name"]} | {e['role']} | salary: {e['salary']} | Tax: {e['tax']} Bonus: {e['bonus']} NET: {e['net']}")
             total_pay += {e["net"]
         print(f"TOTAL PAYROLL TO PAY: KES {total}_pay}")
         print(f"TOTAL EMPLOYEES: {len(employees)}")

    elif choice == "3"
          search = input("Search name: ")
          found = false
          for e in employees:
              if search in e["name"].lower()
              found = false
              for e in employees:
                  if search in e["name"].lower():
                      print(f"FOUND: {e["name"]} | Net Pay: KES {e['net']} | Role: {e['role']}")
                        found = True
              if not found:
                        print("Employee not found!")


             elif choice == "4":
                 print("payroll closed. Goodbye Brian!")
                 break
            else:
                 print("Pick 1-4 only!" 
