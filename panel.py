import time
import os

# Define ASCII Art
ascii_art = """
 ________  ___  ________  ________  ___       ________          ___  ________          ________  _______   ________          
|\   ___ \|\  \|\   __  \|\   __  \|\  \     |\   __  \        |\  \|\   ___ \        |\   ____\|\  ___ \ |\   ___  \        
\ \  \_|\ \ \  \ \  \|\  \ \  \|\ /\ \  \    \ \  \|\  \       \ \  \ \  \_|\ \       \ \  \___|\ \   __/|\ \  \\ \  \       
 \ \  \ \\ \ \  \ \   __  \ \   __  \ \  \    \ \  \\\  \       \ \  \ \  \ \\ \       \ \  \  __\ \  \_|/_\ \  \\ \  \      
  \ \  \_\\ \ \  \ \  \ \  \ \  \|\  \ \  \____\ \  \\\  \       \ \  \ \  \_\\ \       \ \  \|\  \ \  \_|\ \ \  \\ \  \     
   \ \_______\ \__\ \__\ \__\ \_______\ \_______\ \_______\       \ \__\ \_______\       \ \_______\ \_______\ \__\\ \__\    
    \|_______|\|__|\|__|\|__|\|_______|\|_______|\|_______|        \|__|\|_______|        \|_______|\|_______|\|__| \|__|    
                                                                                                                             
"""

def show_menu():
    print(" ========================")
    print(" 1. Generate")
    print(" 2. Config")
    print(" 3. Quit")
    print(" ========================")

def generate():
    print("Generating, please wait...")
    time.sleep(10000000000)  # Simulate a generation process
    print("Generation complete!")
    input("Press Enter to return to the menu...")

def config():
    config_file = "config.txt"
    print("Opening configuration...")
    print("\n(You can modify settings below)")

    # Create the config file if it doesn't exist
    if not os.path.exists(config_file):
        with open(config_file, "w") as f:
            f.write("This is the default config file.\n")

    # Open the config file in the default text editor
    os.system(f"notepad {config_file}")
    input("Press Enter to return to the menu...")

def main():
    while True:
        # Show ASCII Art
        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_art)

        # Show the menu and get the user input
        show_menu()
        choice = input("Please choose an option: ")

        if choice == "1":
            generate()
        elif choice == "2":
            config()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option (1, 2, or 3).")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()
