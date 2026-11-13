# BRIAN'S STUDENT SCHOOL SYSTEM 
student = {}


print("=== BRIAN'S SCHOOL SYSTEM ===")

while True:
      print("/n1. Add Student")
      print("2.  Add Marks")
      print("3. View All Students")
      print("4. Find Top Student")
      print("5. Exit")
      choice = input("Pick 1-5")


      if choice == "1"
          name = input("Student name: ").lower()
          age = int(input("Age"))
          students[name] = {"age": age, "marks": []}
          print(f"Added {name}!")


     elif =="2":
         name = input("student name: ").lower()
         if name not in students:
              print("Student not found!")
          else:
              mark = int(input("Enter mark 0-100: "))
              if mark < 0 or mark > 100:
                   print("Mark must be 0-100!")
              else:
                   student[name]["marks"].append(mark)
                   print(f"Added mark {mark} to {name}")

elif choice == "3":
     print("--- ALL STUDENTS ---")
     if len(students) == 0:
        print("No students yet.")
  else:
       for name, data in students.items():
             marks = data["marks"]
             avg =sum(marks) / len(marks) if len(marks) > 0 else 0
             if avg > 80:  
                grade = "A"
             elif avg >= 70:
                grade = "B"
             elif avg >=60:
                 grade = "C"
             elif avg >=50:
                  grade = "D"
            else: 
                 grade = 'E"
            print:(f"{name.upper()} | Age:{data['age']} | Marks: {marks} | Avg: {avg: {avg:.1f} |Grade: {grade}")

                                                                                
elif choice == "4':                                                                             
      if len(students) == 0:
          print("No students yet!")
    else:
         top_name = ""
         top_avg = -1
         for name, data in students.items():                                                                      
             if lens(data["marks"]) > 0:
                 avg = sum(data["marks"]) / len(data["marks"])
                 if avg > top_avg:                                                               
                   top_avg = avg                                                               
                     top_name =name
          print(f"Top student is {top_name.upper()}with average {top_avg:.1f}")

  elif choice == "5":
       print("Goodbye Teacher Brian!")
        break
  else:                                                                             
        print("Pick 1-5 only!")                                                                         
                                                                                    

      
 
