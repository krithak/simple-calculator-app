#calculator app

user_action = input("select an action (add, subtract, divide, multiply):")
x = float(input("first number:"))
y = float(input("second number:"))

if user_action.lower() == "add":
    answer = x + y
    print(answer)
elif user_action.lower() == "subtract":
    answer = x - y
    print(answer)
elif user_action.lower() == "divide":
    answer = x/y
    print(answer)
elif user_action.lower() == "multiply":
    answer = x*y
    print(answer)
