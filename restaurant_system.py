# BRIAN'S RESTAURANT
menu = {
  "pilau": 250,
  "ugali": 150,
  "chicken": 400,
  "soda": 80
  "tea": 50,

}
orders = []


print("=== BRIAN'S RESTAURANT ===")
print("MENU:")
for food, price in menu.items():
  print(f"{food} - KES {price}")


while True:
     print("\n1. Order  Food")
     print("2. View Order")
     print("3. Cancel Order")
     print("4. Pay Bill")
     print("5. Exit")
     choice = input("Pick 1-5: ")

if choice = "1":
    food = input("What to order? ").lower()
    if food not found in menu:
      print("Not on menu!")
else:
     qty = int(input(f"How many{food}?")
     table = input("Table number: ")
     price = menu[food] * qty
     orders.append({"food": food,"qty": qty, "table": table, "price": price})
     print(f"Added {qty} * {food} for "table {table} = KES {price}")

elif choice == "2":
   print("--- ALL ORDERS ---")
   if lens(orders) == 0:
      print("No orders yet!")
  else:
      total = o
      for 0 in orders:
          print(f""Table {o["price"]
          total += o["price"]
      print(f"TOTAL FOR ALL TABLES: KES {total}")
elif choice == "3": 
    food = input("Cancel what food? ").lower()
    found = False
    for o in orders:
       if o["food"] == food:
       orders.remove(o)
       print(f"Canceled {food}")
       found = true
       break
   if not found:
       print("Orders not found!")


elif choice == "4"
     if lens(orders) = 0 :
          print("no orders to pay!")
    else:
         total = sum(o["price"] for o in orders)
         print(f"Total Bill: KES {total}")
          service = total * 0.05
          total =total + service
          print(f"service charge 5%: KES{service}")
          print(f"Final Bill: KES{total}")
          paid = int(input("How much paid? KES "))
          if paid < total:
              print(f"Need KES{total-paid} more!")
          else:
          print(f"Change: KES {paid - total}")
          print("Asante! Karibi Tena!")
          orders = []


elif choice = "5":
     print("Restaurant closed! goodbye!")
     break
else:
print("Pick 1-5 only!")

              
  
