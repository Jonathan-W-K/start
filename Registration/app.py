from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Define a function to fetch registered data from the database
def get_registered_users():
    conn = sqlite3.connect('Django default.db')  # Replace 'your_database.db' with your actual database file
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM registered_users')  # Assuming your table name is 'registered_users'
    users = cursor.fetchall()
    conn.close()
    return users

# Define a route to render the table
@app.route('/')
def display_registered_users():
    users = get_registered_users()
    return render_template('registered_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
