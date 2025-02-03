import os
import ctypes
import getpass
import hashlib

class UltraView:
    def __init__(self):
        self.accounts = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_account(self, username, password):
        if username in self.accounts:
            print(f"Account for {username} already exists.")
        else:
            self.accounts[username] = self.hash_password(password)
            print(f"Account for {username} successfully added.")

    def switch_account(self, username):
        if username not in self.accounts:
            print(f"No account found for {username}.")
            return
        
        current_user = getpass.getuser()
        if current_user == username:
            print(f"Already logged in as {username}.")
            return
        
        print(f"Switching to account: {username}")
        # This is a placeholder for the actual account switch
        # On a real system, you might use something like os.system(f"runas /user:{username} <command>")
        # Ensure proper security measures are in place before executing such commands
        # os.system(f"tsdiscon")  # This would disconnect the current session on some systems

    def authenticate(self, username, password):
        if username in self.accounts:
            hashed = self.hash_password(password)
            if self.accounts[username] == hashed:
                print(f"Authentication successful for {username}.")
                self.switch_account(username)
            else:
                print("Incorrect password.")
        else:
            print(f"No account found for {username}.")

    def list_accounts(self):
        print("Available accounts:")
        for user in self.accounts.keys():
            print(f"- {user}")

if __name__ == "__main__":
    uv = UltraView()
    while True:
        print("\nUltraView Account Manager")
        print("1. Add Account")
        print("2. Switch Account")
        print("3. List Accounts")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter new account username: ")
            password = input("Enter new account password: ")
            uv.add_account(username, password)
        elif choice == '2':
            username = input("Enter the username to switch to: ")
            password = input("Enter the password: ")
            uv.authenticate(username, password)
        elif choice == '3':
            uv.list_accounts()
        elif choice == '4':
            print("Exiting UltraView.")
            break
        else:
            print("Invalid option. Please try again.")