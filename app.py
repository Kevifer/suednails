from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define the username and password
username = "Sued"
password = "Sued_2023"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        entered_username = request.form['username']
        entered_password = request.form['password']

        if entered_username == username and entered_password == password:
            # Successful login, redirect to agenda page
            return redirect(url_for('agenda'))

        # Failed login
        return "Invalid credentials. Please try again."

    return render_template('login.html')

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

if __name__ == '__main__':
    app.run(debug=True)
