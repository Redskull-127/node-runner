import os
import sys

current_dir = os.getcwd()
nodeManager = "pnpm"
setPort = "3000"
try:
    input("Working directory " + current_dir + "\nPress Any Key to continue...")
    code = input("Do you want to open code editor? (y/n): ")
    node = input("pnpm, npm or yarn (default -> pnpm): ")
    browser = input("Do you want to open browser? (y/n): ")
    if node == "npm":
        nodeManager = "npm"
    port = input("Enter port number (default -> 3000): ")
    if port != "":
        setPort = port
    
    if code == "y":
        os.system("code .")
        
    if nodeManager == "pnpm":
        if browser == "y":
            os.system('start http://localhost:' + setPort)
            os.system("pnpm run dev")
        else:
            os.system("pnpm run dev")
    else:
        if browser == "y":
            os.system('start http://localhost:' + setPort)
            os.system("npm run dev")
        else:
            os.system("npm run dev")
    
except SyntaxError:
    print("Something went wrong...")
    print("Working directory " + current_dir + "\nPress Any Key to continue...")
finally:
    print("Thank you for using this script...\nby Meer Tarbani - https://meertarbani.dev")