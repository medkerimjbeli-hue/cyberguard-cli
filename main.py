from password_analyzer import run_analyzer
from password_generator import run_generator
from integrity_checker import run_integrity_checker
from log_analyzer import run_log_analyzer


def display_banner(): #Banner Displaying Function
    print(r"""
   ______      __               ______                      __
  / ____/_  __/ /_  ___  _____ / ____/___  __  ______  ____/ /
 / /   / / / / __ \/ _ \/ ___// / __/ __ \/ / / / __ \/ __  /
/ /___/ /_/ / /_/ /  __/ /   / /_/ / /_/ / /_/ / / / / /_/ /
\____/\__, /_.___/\___/_/    \____/\____/\__,_/_/ /_/\__,_/
     /____/

       [ CYBERGUARD CLI v1.0 ]
       Defensive Security Toolkit
       Made By : Mohamed Kerim Jbeli
       =========================
""") 



def display_menu(): #Main Menu Displaying Function
    print("\n[1] Password Strength Analyzer")
    print("[2] Secure Password Generator")
    print("[3] File Integrity Checker")
    print("[4] Log Analyzer")
    print("[0] Exit")


def stay_or_exit(): #Returns True to stay in the same tool, False to leave it.
    print("\n[1] Stay")
    print("[0] Exit")
    while True:
        choice = input("\nSelect an option: ").strip()
        if choice == "1":
            return True
        elif choice == "0":
            return False
        else:
            print("\nInvalid choice. Please try again.")


def run_tool(tool): #Runs a tool repeatedly until the user picks Exit.
    while True:
        tool()
        if not stay_or_exit():
            break


def main(): #Main Function
    tools = { #Tools Declaration
        "1": run_analyzer,
        "2": run_generator,
        "3": run_integrity_checker,
        "4": run_log_analyzer,
    }

    display_banner() #Calling the banner displayer

    while True: #Main loop
        display_menu() #Calling the menu displayer
        choice = input("\nSelect an option: ").strip() #Getting the user's option
        #Block 'if' to test user's input validity
        if choice in tools:
            run_tool(tools[choice])

        elif choice == "0":
            print("\nExiting CyberGuard. Stay secure!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__": #Ruuning the script
    main() 
