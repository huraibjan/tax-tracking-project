from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS  # Import COR
from datetime import datetime
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config['MYSQL_HOST'] = os.getenv('DATABASE_HOST')
app.config['MYSQL_USER'] = os.getenv('DATABASE_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('DATABASE_PASSWORD')
app.config['DATABASE_NAME'] = os.getenv('DATABASE_NAME')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mysql = MySQL(app)

# Creating Database if not exist
def create_database():
    try:
        connection = mysql.connection
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {app.config['DATABASE_NAME']}")
        cursor.close()
    except Exception as e:
        print(f"Error creating database: {str(e)}")

# Initialize Database Table
def init_db():
    query = """
    CREATE TABLE IF NOT EXISTS tax_records (
        id INT AUTO_INCREMENT PRIMARY KEY,
        company VARCHAR(50) NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        payment_date DATE,
        status ENUM('paid', 'unpaid') NOT NULL,
        due_date DATE NOT NULL
    );
    """
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()

# Set Database Context
def set_database_context():
    cur = mysql.connection.cursor()
    cur.execute(f"USE {app.config['DATABASE_NAME']}")
    cur.close()

# Routes
@app.route('/records', methods=['GET'])
def get_records():
    try:
        set_database_context()
        due_date = request.args.get('due_date')
        cur = mysql.connection.cursor()

        if due_date:
            query = "SELECT * FROM tax_records WHERE due_date = %s"
            cur.execute(query, (due_date,))
        else:
            query = "SELECT * FROM tax_records"
            cur.execute(query)

        records = cur.fetchall()
        cur.close()

        result = [
            {
                'id': record[0],
                'company': record[1],
                'amount': float(record[2]),
                'payment_date': record[3].strftime('%m/%d/%Y') if record[3] else None,  # MM/DD/YYYY format
                'status': record[4],
                'due_date': record[5].strftime('%m/%d/%Y')  # MM/DD/YYYY format
            }
            for record in records
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/records', methods=['POST'])
def add_record():
    try:
        set_database_context()
        data = request.json

        # Parse dates from MM/DD/YYYY to YYYY-MM-DD for storage
        payment_date = (
            datetime.strptime(data.get('payment_date'), '%m/%d/%Y').date()
            if data.get('payment_date')
            else None
        )
        due_date = datetime.strptime(data['due_date'], '%m/%d/%Y').date()

        query = """
        INSERT INTO tax_records (company, amount, payment_date, status, due_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur = mysql.connection.cursor()
        cur.execute(query, (data['company'], data['amount'], payment_date, data['status'], due_date))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Record added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
    try:
        set_database_context()
        data = request.json

        # Parse dates from MM/DD/YYYY to YYYY-MM-DD for storage
        payment_date = (
            datetime.strptime(data.get('payment_date'), '%m/%d/%Y').date()
            if data.get('payment_date')
            else None
        )
        due_date = datetime.strptime(data['due_date'], '%m/%d/%Y').date()

        query = """
        UPDATE tax_records
        SET company = %s, amount = %s, payment_date = %s, status = %s, due_date = %s
        WHERE id = %s
        """
        cur = mysql.connection.cursor()
        cur.execute(query, (
            data['company'],
            data['amount'],
            payment_date,
            data['status'],
            due_date,
            id
        ))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Record updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/records/<int:id>', methods=['DELETE'])
def delete_record(id):
    try:
        set_database_context()
        query = "DELETE FROM tax_records WHERE id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Record deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == '__main__':
    # Use application context to initialize the database
    with app.app_context():
        create_database()
        set_database_context()
        init_db()

    # Run the application
    app.run(debug=True)
