from colorama import init, Fore, Back, Style

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

def beautify_terminal():
    print_banner()

    print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "Hello! This is a beautified terminal.")
    print(Style.RESET_ALL)  # Reset formatting

    print(Fore.RED + "Red text")
    print(Fore.GREEN + "Green text")
    print(Fore.BLUE + "Blue text")
    print(Style.RESET_ALL)  # Reset formatting

    print(Back.CYAN + "Cyan background" + Style.RESET_ALL)
    print(Back.MAGENTA + "Magenta background" + Style.RESET_ALL)

if __name__ == "__main__":
    beautify_terminal()
