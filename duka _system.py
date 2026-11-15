# DUKA MANAGEMENT SYSTEM - Pro Version by Bwayne Bryane

class Duka:
    def __init__(self, name):
        self.name = name
        # product: [price, stock]
        self.products = {
            "Bread": [150, 20],
            "Milk": [120, 30],
            "Sugar 1kg": [250, 15],
            "Cooking Oil 1L": [350, 10],
        }
        self.total_sales = 0
        self.total_profit = 0

    def show_products(self):
        print(f"\n--- {self.name} STOCK ---")
        for item, (price, stock) in self.products.items():
            print(f"{item} - KES {price} | Stock: {stock}")

    def add_product(self):
        name = input("Product name: ")
        try:
            price = float(input("Price: "))
            stock = int(input("Stock quantity: "))
            self.products[name] = [price, stock]
            print(f"Added {name} successfully!")
        except ValueError:
            print("Price and stock must be numbers!")

    def sell_product(self):
        self.show_products()
        item = input("\nWhat to sell? ")
        if item not in self.products:
            print("Product not found!")
            return
        try:
            qty = int(input("How many? "))
        except ValueError:
            print("Enter a number!")
            return

        price, stock = self.products[item]
        if qty > stock:
            print(f"Only {stock} left in stock!")
            return

        total = price * qty
        # Assume buying price is 80% of selling price for profit
        profit = total * 0.2
        self.products[item][1] -= qty
        self.total_sales += total
        self.total_profit += profit
        print(f"Sold {qty} x {item} = KES {total}")
        print(f"Profit from this sale: KES {profit:.0f}")

    def daily_report(self):
        print(f"\n--- DAILY REPORT: {self.name} ---")
        print(f"Total Sales Today: KES {self.total_sales}")
        print(f"Total Profit Today: KES {self.total_profit:.0f}")
        self.show_products()

def main():
    shop = Duka("Bwayne Duka - Rongai")
    while True:
        print("\n=== DUKA MENU ===")
        print("1. Show Products")
        print("2. Add Product")
        print("3. Sell Product")
        print("4. Daily Report")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            shop.show_products()
        elif choice == "2":
            shop.add_product()
        elif choice == "3":
            shop.sell_product()
        elif choice == "4":
            shop.daily_report()
        elif choice == "5":
            print("Closing shop. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
