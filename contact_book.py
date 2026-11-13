print("Welcome To Brian Contact Book")

contacts = {}

while True:
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Pick 1, 2, 3, 4 or 5: ")

if choice == "1"
        name = input ("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact Saved !")

elif choice == "2"
    if len(contacts) == 0:
      print("No contacts yet!")
else:
     for name, phone in contacts.items():
       print (name, "_", phone)


elif choice == "3"
      search = input("Who to search? ")
      if search in contacts:
            print(search, "_", contacts[search])
      else:
           print("Not found!")

elif choice == "4"
     delete = input("who to delete? ")
    if delete in contacts:
           delete comtacts[delete]
          print ("Deleted")
    else:
         print("Not found!")

elif choice = "5":
       print("Bye Brian!")
       break
else:
     print("Pick 1 to 5 only")
  
