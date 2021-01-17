import os


def print_menu():
    print(" hello in my program")
    print("1) Calculate square")
    print("2) Calculate qube")


def choose_option():
    try:
        user_input = int(input("choose option 1) or 2): "))
        if user_input == 2:
            return calculate_qube()
        elif user_input == 1:
            return calculate_square()
        else:
            return choose_option()
    except ValueError:
        return choose_option()


def calculate_qube():
    try:
        a = float(input("give a number(int/ float): "))
        b = a * a
        print("-------------------")
        print("qube of", str(a), "is", str(b))
        print("-------------------")
    except ValueError:
        print("Incorrect value")
        return calculate_qube()


def calculate_square():
    try:
        a = float(input("give a number (int/ float): "))
        b = a * a * a
        print("-------------------")
        print("square of", str(a), "is", str(b))
        print("-------------------")
    except ValueError:
        print("Incorrect value")
        return calculate_square()


def main():
    while True:
        print_menu()
        choose_option()
        print("\n")
        os.system("cls || clear")


if __name__ == "__main__":
    main()
