from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# Predefined user credentials
users = {
    "testuser": "password123"  # You can replace with your preferred username and password
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials, please try again."

    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        items = [f"test{i}" for i in range(1, 21)]  # Create 20 items: test1, test2, ..., test20
        return render_template('home.html', items=items)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
