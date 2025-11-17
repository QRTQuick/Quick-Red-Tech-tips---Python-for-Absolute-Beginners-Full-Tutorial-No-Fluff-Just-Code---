age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")  
else:
    print("You are a minor.")
    
# or
age = int(input("Enter your age: ")) ; print("You are an adult." if age >= 18 else "You are a minor.")