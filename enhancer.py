from colorama import init, Fore, Style

# Initialize colorama to work on Windows terminals as well
init()

def print_banner():
    banner = """
   _   _           _     _  __     __                  
  | | | |         | |   (_)/ _|   / _|                 
  | |_| | __ _ ___| |__  _| |_   | |_ ___  _ __ _   _  
  |  _  |/ _` / __| '_ \| |  _|  |  _/ _ \| '__| | | | 
  | | | | (_| \__ \ | | | | |    | || (_) | |  | |_| | 
  |_| |_|\__,_|___/_| |_|_|_|    |_| \___/|_|   \__,_| 
    """

    print(Fore.YELLOW + Style.BRIGHT + banner + Style.RESET_ALL)

def print_menu():
    print("Select a color to change the terminal:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Cyan")
    print("5. Magenta")
    print("6. White")
    print("0. Exit")

def change_color(choice):
    if choice == "1":
        return Fore.RED
    elif choice == "2":
        return Fore.GREEN
    elif choice == "3":
        return Fore.BLUE
    elif choice == "4":
        return Fore.CYAN
    elif choice == "5":
        return Fore.MAGENTA
    elif choice == "6":
        return Fore.WHITE
    else:
        return None

def beautify_terminal():
    print_banner()

    while True:
        print_menu()
        user_choice = input("Enter your choice (0-6): ")

        if user_choice == "0":
            break

        selected_color = change_color(user_choice)
        if selected_color:
            print(selected_color + f"This is the {selected_color} color!" + Style.RESET_ALL)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    beautify_terminal()


