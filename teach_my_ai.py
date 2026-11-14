# BRIAN'S TEACHABLE AI
print ("Mambo! Naitwa Brian Ai. Teach Me!")


brain = {}


while True:
     you = input("You: ").lower()

     if you =="bye":
         print(f"AI:{Bye! I will remember what you taught me!")
         break

     if you in brain:
        print(f"AI: {brain[you]"}
  else:
       print("AI: I don't know that yet. What should I say?'
       answer = input("Teach me: ")
       brain[you] = answer
       print("AI: Got it! I learned that!")
        
