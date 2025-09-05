#Create a Dictionary of Student Marks
marks = {"Shreya": 85,
         "Amruta": 76,
         "Priyanka": 92,
         "Siddhika": 90,
         "Parinita": 88}

name = input("Enter the student's name: ")

if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print(f"Sorry, no records found for '{name}'.")