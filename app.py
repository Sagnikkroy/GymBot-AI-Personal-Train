from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        # Insert user data into the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        # Check if the email already exists in the database
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = c.fetchone()

        if existing_user:
            # If user already exists, show error message
            conn.close()
            return 'Email already exists, please try a different one.'
        
        # If user doesn't exist, insert new record
        c.execute("INSERT INTO users (name, phone, email, password) VALUES (?, ?, ?, ?)", 
                  (name, phone, email, password))
        conn.commit()

        # Verify if the data was inserted
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        new_user = c.fetchone()

        conn.close()

        if new_user:
            return 'Sign Up successful! You can now Sign In.'
        else:
            return 'There was an error during Sign Up. Please try again.'

    return render_template('signup_signin.html')


# Sign In Route
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check user credentials
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            return redirect(url_for('dashboard'))  # Redirect to a dashboard or home page
        else:
            return 'Invalid credentials, please try again.'

    return render_template('signup_signin.html')

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    return "Welcome to your Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
