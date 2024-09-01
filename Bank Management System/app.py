from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='bank_management_system',
            user='root',
            password='root'
        )
        if connection.is_connected():
            print("Connection to MySQL database successful.")
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-account', methods=['POST'])
def create_account():
    data = request.json
    name = data['name']
    initial_deposit = data['initialDeposit']
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql_insert_query = """INSERT INTO accounts (name, balance) VALUES (%s, %s)"""
            cursor.execute(sql_insert_query, (name, initial_deposit))
            connection.commit()
            return jsonify(message=f"Account created successfully for {name}.")
        except Error as e:
            return jsonify(error=str(e)), 500
        finally:
            close_connection(connection)
    return jsonify(error="Connection failed."), 500

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    account_id = data['accountId']
    amount = data['amount']
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql_update_query = """UPDATE accounts SET balance = balance + %s WHERE account_id = %s"""
            cursor.execute(sql_update_query, (amount, account_id))
            connection.commit()
            return jsonify(message=f"Deposited ${amount} to account ID {account_id}.")
        except Error as e:
            return jsonify(error=str(e)), 500
        finally:
            close_connection(connection)
    return jsonify(error="Connection failed."), 500

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    account_id = data['accountId']
    amount = data['amount']
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql_check_balance_query = """SELECT balance FROM accounts WHERE account_id = %s"""
            cursor.execute(sql_check_balance_query, (account_id,))
            balance = cursor.fetchone()[0]
            if balance >= amount:
                sql_update_query = """UPDATE accounts SET balance = balance - %s WHERE account_id = %s"""
                cursor.execute(sql_update_query, (amount, account_id))
                connection.commit()
                return jsonify(message=f"Withdrew ${amount} from account ID {account_id}.")
            else:
                return jsonify(error=f"Insufficient balance. Available balance is ${balance}.")
        except Error as e:
            return jsonify(error=str(e)), 500
        finally:
            close_connection(connection)
    return jsonify(error="Connection failed."), 500

@app.route('/check-balance', methods=['GET'])
def check_balance():
    account_id = request.args.get('accountId')
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql_select_query = """SELECT balance FROM accounts WHERE account_id = %s"""
            cursor.execute(sql_select_query, (account_id,))
            balance = cursor.fetchone()[0]
            return jsonify(balance=balance)
        except Error as e:
            return jsonify(error=str(e)), 500
        finally:
            close_connection(connection)
    return jsonify(error="Connection failed."), 500

if __name__ == '__main__':
    app.run(debug=True)
