# mini project time 
# mini calculator

run = True 
while run:
    print("Select operation.")
    print("1.Addittion")
    print("2.Subtraction")
    print("3.Multiplication") 
    print("4.Division")
    print("5.Exit")
    
    choice = input("Enter choice(1/2/3/4/5): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("result:", num1, "+", num2, "=", num1 + num2)
        elif choice == '2':
            print("result:", num1, "-", num2, "=", num1 - num2)
        elif choice == '3':
            print("result:", num1, "*", num2, "=", num1 * num2)
        elif choice == '4':
            if num2 != 0: # !! means not  in python 
                print("result:", num1, "/", num2, "=", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
    elif choice == '5':
        run = False
        print("Exiting the calculator. Goodbye!")
            