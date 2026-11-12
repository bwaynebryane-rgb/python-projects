print("Welcome To Brian Expense Tracker")

total = 0
expenses = []

while True:
    print("1. Add expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. View Total")
    choice = input("Pick 1, 2, 3, 4: ")

if choice == "1":
       name = input ("What did you spend on? ")
       amount = float(input("How much? "))
       expenses.append(name + " _ " + str(amount))
      total = total + amount
      print(:Expense added!")
elif choice == "2":
      if len(expenses) == 0:
           print("No Expenses Yet:")
   else:
        for e expenses
            print (e)

eliff choice == "3":
      print("Total spent:", total)

elif choice == "4":
     print("Total spent today:",)
     print("Bye Brian! Save your money!")
     break
else:
    print("Pick 1, 2, 3, or 4 only")
