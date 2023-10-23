from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define the username and password
username = "Sued"
password = "Sued_2023"

# Sample list of clients
sample_clients = ["Cliente A", "Cliente B", "Cliente C"]

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
    return render_template('agenda.html', clients=sample_clients)

@app.route('/clientes')
def clientes():
    return render_template('clientes.html', clients=sample_clients)

@app.route('/novo-cliente', methods=['GET', 'POST'])
def novo_cliente():
    if request.method == 'POST':
        new_client_name = request.form.get('client_name')
        if new_client_name:
            sample_clients.append(new_client_name)

    return render_template('novo_cliente.html')

if __name__ == '__main__':
    app.run(debug=True)
