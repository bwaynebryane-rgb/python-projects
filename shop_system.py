# BRIAN'S SHOP
shop = {
    "bread": 100,
    "milk": 150,
    "sugar": 200,
    "rice": 300,
    "soda": 80,
    "salt": 50,
    "Bread":100,
    "omo 1kg":150,
    "cooking oil 1kg":300
    "colgate": 120
    "wheat flour": 200
    "maize flour": 180
    "lotion":300
    "Yoghurt":130
    "Tea Leaves ketepa": 65
    "Glucosee":30
    "cocacola ":100
    "energy drink":70
    "water":70
    "vaseline":150
    "club soda":200
    "margarine":250
    "Blueband ":240
    "coffee ":20
    "choco ":10
    "chocolate":20
    
}
cart = []
total = 0


print("=== WELCOME TO BRIAN'S SHOP ===")
print("Items for sale:")
for item, price in shop.items():
    print( f"{item} - KES {price})


while True
     print("\n1. Add to Cart")
     print("2. View Cart")
     print("3. Remove from cart")
     print("4. checkout")
     print("5. Exit ")
     choice = input("Pick 1-5: ")


     if  choice == "1":
         item = input("What to buy? ").lower()
         if item not in shop:
             print("we dont sell that!")
         else:
              qty = int(input(f"How many{items}? "))
              if qty <= 0:
                   print("Qty must be more than 0!")
              else:
                   price = shop[item] * qty
                   cart.append({"item": item, "qty, "price": price})
                   print(f"Added {qty} * {item} = KES {price}")


     elif  choice == "2"
         print("--- YOUR CART ---")
         if len(cart) == 0:
             print("Cart  is empty!")
        else:
            total = 0
            for c in cart:
                 print{f"{c['qty']} * {c['item']} = KES {c['price']}")
                 total +=c["price"]
            print(f"TOTAL: KES {total}")


  elif choice == "3":
      item = input("Remove what? ").lower()
      found = False
      for c in cart:
          if c["item"] == item:
            cart.remove(c)
            print(f'Removed {item}")
            found = True
            break
      if not found:
          print("Not in cart!")


elif choice == "4"
    if len(cart) == 0:
        print(cart empty! Buy something first!")
    else:
         total = sum(c["price"] for c in cart)
         print(f"Your total  is KES {total}")
         if total >= 1000:
               discount = total * 0. 10
               print(f"You get 10% discount!  You save KES {discount}")
               total = discount - discount
               print(f"New total: KES {total}")
        paid = int(input("How much did you pay? KES "))
        if paid < total:
            print(f"Not enough! You need KES {total - paid} more!")
      else:
            change = paid - total
            print(f"Thank you! Your change is KES {change}")
            print("--- RECEIPT ---")
            for c in cart:
                print(f"{c['qty]} * {c['item']} = KES {c['price']}")
            print(f"TOTAL PAID : KES {total}") 
            cart = []
            print("Cart cleared! Karibu tena!")


elif choice == "5":
     print("Goodbye from Brian's Shop!")
     break
else:
     print(" 1-5 only!")
