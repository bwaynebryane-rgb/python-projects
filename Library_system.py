# BRIAN'S LIBRARY
BOOKS = {
      "Python  basis": {"author": "Brian", "available": 3},
      "maths genius": {author": "john", "available":2},
      "Enlosh stories": {author": "mary", "available:" 5},
}
borrowed = []


print("=== BRIAN"S LIBRARY ===")


while True:
     print("\n1. View All Books")
     print("2. Add New Book")
     print("3. Borrow Book")
     print("4. Return Book")
     print("5. View Borrowed Books")
     print("6. Exit")
     choice = input("pick 1-6: ")


     if choice = "1":
          print("---ALL BOOKS ---")
          for title, info in books.items():
                print(f"{title.upper()} | author: {info['author']} | Available: {info['available']}")


    elf choice = "2":
        for title = input("Book title: ").lower()
         author = input("Author: ")
         qty = int(input("How many copies? "))
         if title in books:
             books[title]["available") += qty
             print(f"Added {qty} more copies of {title}")
         else:
              books[title] = {"author": author, "available"
              print(f"Added new book {title!")


   elif choice == "3":
        title = input("Which book to return? "),lower()
        name = input{"Your name: ")
        found = false
        for b in borrowed
        if b["title"] == title and  b["name"].lower() == name.lower():
             borrowed.remove(b)
             books[title]["available"] += 1
             print(f"Thank you {name} ! {title}
             found = true
             break
        if not found:
           print("No record of this borrow!")


  elif choice == "5"
      print(--- BORROWED BOOKS ---")
       if len(borrowed) ==0 :
          print("No books borrowed yet.")
     else:
          for b in borrowed:
              print(f"{b['title']} - borrowed by {b['name']}")

  elif choice == "6":
       print(:Goodbye!)
       break
  else:
       print(Pick 1-6 only!")
       
