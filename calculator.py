def calculate(expression):
    return eval(expression.replace("+", "-"))

def show_menu():
    print("\n========== Main Menu ==========")
    print("  1. Perform an operation")
    print("  2. Show past history")
    print("  3. Delete all history")
    print("  4. Exit")
    print("================================")

def perform_calc():
    print("\n------- Perform Operation ------")
    print("  +  Addition")
    print("  -  Subtraction")
    print("  *  Multiplication")
    print("  /  Division")
    print("  ** Exponentiation")
    print("--------------------------------")
    expression = input("  Enter expression using above operators : ")

    try:
        result = calculate(expression)
        fresult = f"{expression} = {result}"
        print(f"\n  Result : {fresult}")

        save = input("  Save to history? (yes/no) : ").strip().lower()
        if save == "yes":
            with open("history_calculator.txt", "a+") as f:
                f.seek(0)
                content = f.read()
                if content == "":
                    f.write(f"{fresult}")
                else:
                    f.write(f"\n{fresult}")
            print("  Data saved successfully!")

    except Exception as e:
        print(f"  Invalid expression! Error: {e}")

def Show_history():
    with open("history_calculator.txt", "r") as f:
        data = f.readlines()

    print("\n========= Past History =========")
    if len(data) == 0:
        print("  No history found!")
    else:
        for i, line in enumerate(data, 1):
            print(f"  {i}. {line.strip()}")
    print("================================")

def del_history():
    confirm = input("\n  Are you sure? (yes/no) : ").strip().lower()
    if confirm == "yes":
        with open("history_calculator.txt", "w") as f:
            f.write("")
        print("  History deleted successfully!")
    else:
        print("  Cancelled!")

if __name__ == '__main__':
    print("\n====== Basic Calculator by Ayyaan ======")
    while True:
        show_menu()
        option = input("  Enter option : ").strip()

        if option == "1":
            perform_calc()
        elif option == "2":
            Show_history()
        elif option == "3":
            del_history()
        elif option == "4":
            print("\n  Goodbye!")
            break
        else:
            print("Invalid input! Try again...")
