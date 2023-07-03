from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Retrieve the names from the database
    cursor.execute("SELECT name FROM users")
    names = [row[0] for row in cursor.fetchall()]

    # Close the database connection
    conn.close()

    return render_template('index.html', names=names)


@app.route('/details', methods=['POST'])
def details():
    selected_name = request.form['name']

    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Retrieve the details of the selected person from the database
    cursor.execute("SELECT * FROM users WHERE name=?", (selected_name,))
    user_details = cursor.fetchone()

    # Close the database connection
    conn.close()

    if user_details:
        return render_template('details.html', details=user_details)
    else:
        return "No details found for the selected person."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
