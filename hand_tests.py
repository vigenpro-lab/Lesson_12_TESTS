from functions import hello_who, salary

if hello_who("Max") != "Hello, Max":
    print("Error")
else:
    print("Good")

if salary(4, 100) != 800:
    print("Error")
else:
    print("Good")