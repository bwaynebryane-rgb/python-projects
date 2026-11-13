# BRIAN'S BANK - Full ATM System by Brian
#Features: Login, Deposit,Withdraw,Balance, History, Interest


accounts = {
         "brian": {"pin": "1234"' "balance": 5000,"history": []}'
         "tracy": {"pin"1111","balance": 2000, "history,": []},

         }

         print("== WELCOME TO BRIAN'S BANK ===")

         username = input("Enter username: ").lower()
         pin = input("Enter PIN: ")


         if username not if accounts or accounts [username]["pin'] != pin:
             print("Wrong username or PIN! access Denied.")
         else:
             print("Welcome back, {username.upper()}!)
             balance = accounts [username]["balance"]
             history = accounts[username]['history"]


             while True:
                 print("/n--- MENU ---")

               . print("1. Check Balaance")
                . print("2. Deposit Money")
                . print("3. Withdraw Money")
                 .print("4. Send Money")
                 .print("5. View Transaction History")
                 .print("6. Calculate Interest (1 Year - 10%)")
                 .Exit")

                 choice = input("Pick 1-7: ')


                 if choice ==="1":
                     print(f"Your balance is: KES {balance}")



                 elif choice == "2":
                      amount = int(input("How much to deposit? KES ")
                      if  amount <= 0:
                          print("Amount must be more than 0!"))
                    else: 
                        balance += amount
                        history.append("Deposited  KES {amount}")
                        print("f"Deposited! New balance : {balance}")


                    elif choce = "3":
                         amount = int(input("How much to withdraw? KES "))
                         if amount <= 0:
                             print("Amount must be more than 0!")
                         elif amount > balance:
                             print("Not enough money!")
                         else:
                              balance -= amount
                              history.append(f"Withdraw KES {amount}")
                              printf"Withdrawn! New balance: KES{balance}")


                    elif choice = "4":
                        receiver = input("Send to who? ")
                        amount = Int(input("How Much? KES "))
                        if amount > balance 
                            print("Not enough money!")
                        elif amount <= 0:
                             print("Invalid amount!")
                        else:
                            balane -= amount
                            history.append(f"Sent KES {amount} to {receiver}")
                            print(f"Sent KES {amount} to {receiver}! Balance : KES {balance}")



                            elif choice == "5"
                                print("---YOUR HISTORY ---")
                                if len(history) == 0:
                                    print("No transactions yet.")
                                else:
                                    for items in history:
                                        print("-=, item)


                          elif choice == "6":
                               interest = balance * 0.10
                               print("f"If you save KES {balance} for 1 year at 10%, you get KES {interest} interest!")
                               print("f" total after 1 year : {balance + interest}")


                          elif choice == "7":
                               print(f"Thanks ypu {username}! Your final balance in KES {balance}")
                               print("Goodbye from Brian's Bank!")
                               break
                          else:
                              print("Pick 1-7 only!")
                  


          
                 
