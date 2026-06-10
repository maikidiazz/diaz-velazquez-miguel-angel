
student = {}

student["name"] = input("Ingresa tu nombre:")
student["programming"] = int(input("Programming skills:  (1-10): "))
student["design"] = int(input("Design skills:  (1-10): "))
student["communication"] = int(input("Communication skills:  (1-10): "))
student["english"] = int(input("English skills:  (1-10): "))
student["teamwork"] = int(input("Teamwork skills:  (1-10): "))

total_score = student["programming"] + student["design"] + student["communication"] + student["english"] + student["teamwork"]
average_score = total_score / 5

try:
    if average_score >= 8:
        print(f"{student['name']}, you are an excellent candidate for the internship.")

    elif average_score >= 5:
        print(f"{student['name']}, you have potential, but there is room for improvement.")

    else:
        print(f"{student['name']}, you may need to work on your skills to be a strong candidate for the internship.")
        
except ZeroDivisionError:
    print("Error: Division by zero. Please ensure all skill ratings are provided and valid.")

print("\nStudent Information:") 
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")