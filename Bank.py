# Simple Banking System in Python

accounts = {}  # Store accounts in format: {account_number: {"name": str, "balance": float}}

def create_account():
    acc_no = input("Enter new account number: ")
    if acc_no in accounts:
        print("❌ Account already exists!")
        return
    name = input("Enter account holder's name: ")
    accounts[acc_no] = {"name": name, "balance": 0.0}
    print(f"✅ Account created successfully for {name}!")

def deposit():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("❌ Account not found!")
        return
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("❌ Invalid amount!")
        return
    accounts[acc_no]["balance"] += amount
    print(f"✅ Deposited ₹{amount:.2f}. New Balance: ₹{accounts[acc_no]['balance']:.2f}")

def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("❌ Account not found!")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("❌ Invalid amount!")
        return
    if amount > accounts[acc_no]["balance"]:
        print("❌ Insufficient balance!")
        return
    accounts[acc_no]["balance"] -= amount
    print(f"✅ Withdrawn ₹{amount:.2f}. Remaining Balance: ₹{accounts[acc_no]['balance']:.2f}")

def check_balance():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("❌ Account not found!")
        return
    print(f"💰 Account Holder: {accounts[acc_no]['name']}")
    print(f"💰 Current Balance: ₹{accounts[acc_no]['balance']:.2f}")

def close_account():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("❌ Account not found!")
        return
    del accounts[acc_no]
    print("✅ Account closed successfully!")

def main():
    while True:
        print("\n===== Banking System Menu =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Close Account")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            close_account()
        elif choice == "6":
            print("👋 Thank you for using our banking system!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Run the program
main()
