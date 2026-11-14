# BRIAN'S PAYROLL EXCEL REPORT
#this creates a CSV file like excel and analyzes it
import csv

employees = [
   {"name": "Brian", "role": "manager", "salary": 60000,years": 6},
   {"name": "Mary", "role": "staff", "salary": 35000, "years": 3},
   {"name": john", "role": "staff", "salary": 25000, "years": 1}
   {"name": sarah", "role": "intern", "salary": 1500, "years": 0}
]

def calculator_tax(salary):
    if salary <= 20000:
        return salary * 0.1
    elif salary <= 50000:
        return salary * 0.3


def calculator_bonus(year,salary):
     if years >= 5:
        return salary * 0.15
    elif years >= 2:
        return salary * 0.10
    else return 0


print("---PAYROLL EXCEL REPORT ===")

with open("payroll.csv", "w" , new line ="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name"' "Role", "salary", "Tax", "Bonus", Net Pay"])
    total_salary = 0
    total_tax = 0
    total_bonus = 0
    total_net = 0
    highest_paid =""
    highest_pay = 0
    for e in employees:
        tax = calculate_tax(e["salary"])
        bonus =calculate_bonus(["years"], e["salary"])
        net = e["salary"] - tax + bonus
        write.writerow([e["name"], e["role"], e["salary"], tax, bonus, net])
        print(f"{e['name']} | {e['role']} | Salary: {e['salary']} | Tax: {tax} |Bonus: {bonus} | NET: {net}")
        total_salary += e["salary"]
        total_tax += tax
        total_bonus += bonus
        total_net += net
        if net > highest pay
            highest_pay = net
            highest_paid = e["name"]
print("\n--- EXCEL SUMMARY ANALYSIS ---")
print(f"Total Employees: {len(employees)}")
print(f"Total salary: KES {total_salary}")
print(f"Total Tax: KES {total_tax}
print(f"Total bonus: KES {total_bonus}
print(f"Net Pay : KES {total_net}
print(f"Avarage Net pay: KES {total_net / len(employees}
print(f"Highest paid: {highest_paid} - KES {highest_pay}")
print("\nCSV file payroll.csv created! Open in Excel!")
    
