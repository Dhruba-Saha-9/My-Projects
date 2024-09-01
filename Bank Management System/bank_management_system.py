import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='bank_management_system',
            user='root',  # Replace with your MySQL username
            password='root'  # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Connection to MySQL database successful.")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

# Close the database connection
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")

# Create a new bank account
def create_account(connection, name, initial_deposit):
    try:
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO accounts (name, balance) VALUES (%s, %s)"""
        record = (name, initial_deposit)
        cursor.execute(sql_insert_query, record)
        connection.commit()
        print(f"Account created successfully for {name}.")
    except Error as e:
        print(f"Error: '{e}'")

# Deposit money into an account
def deposit(connection, account_id, amount):
    try:
        cursor = connection.cursor()
        sql_update_query = """ UPDATE accounts SET balance = balance + %s WHERE account_id = %s"""
        cursor.execute(sql_update_query, (amount, account_id))
        connection.commit()
        print(f"Deposited ${amount} to account ID {account_id}.")
    except Error as e:
        print(f"Error: '{e}'")

# Withdraw money from an account
def withdraw(connection, account_id, amount):
    try:
        cursor = connection.cursor()
        sql_check_balance_query = """ SELECT balance FROM accounts WHERE account_id = %s"""
        cursor.execute(sql_check_balance_query, (account_id,))
        balance = cursor.fetchone()[0]
        if balance >= amount:
            sql_update_query = """ UPDATE accounts SET balance = balance - %s WHERE account_id = %s"""
            cursor.execute(sql_update_query, (amount, account_id))
            connection.commit()
            print(f"Withdrew ${amount} from account ID {account_id}.")
        else:
            print(f"Insufficient balance. Available balance is ${balance}.")
    except Error as e:
        print(f"Error: '{e}'")

# Check the balance of an account
def check_balance(connection, account_id):
    try:
        cursor = connection.cursor()
        sql_select_query = """ SELECT balance FROM accounts WHERE account_id = %s"""
        cursor.execute(sql_select_query, (account_id,))
        balance = cursor.fetchone()[0]
        print(f"The balance for account ID {account_id} is ${balance}.")
    except Error as e:
        print(f"Error: '{e}'")

# Main function to run the bank management system
def main():
    connection = create_connection()
    if connection is None:
        return

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            create_account(connection, name, initial_deposit)
        elif choice == 2:
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to deposit: "))
            deposit(connection, account_id, amount)
        elif choice == 3:
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw(connection, account_id, amount)
        elif choice == 4:
            account_id = int(input("Enter account ID: "))
            check_balance(connection, account_id)
        elif choice == 5:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

    close_connection(connection)

if __name__ == "__main__":
    main()
