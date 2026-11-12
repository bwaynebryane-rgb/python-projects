print("Welcome To Brian Password Checker")

while True:
  password = input("Enter a password (or type exit): ")

if password == "exit":
    print("Bye Brian!")
    break

score = 0

if len(pasword) >= 8:
    score = score + 1
else:
  print{"Too short ! Use 8+ character")

  if has_number = False
  for char in password:
      if char.isdigit():
            has_number = True
     if has_number:
        score = score +1
   else:
        print("add number! ")

has_upper = false
for char in password:
       if char.isupper():
            has_upper = True
      if has_upper:
           score = score + 1
else:
    print("Add a CAPITAL letter!")

  print("Your password stregth:"), score, "out of 3")
if score = 3:
       print("strong password!")
elif score == 2 :
    print("medium password!")
else:
    print("weak password - Try Again")
