from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret123'   # required for login session

# Dummy login credentials
USERNAME = "sanyukta"
PASSWORD = "1234"

tasks = []
completed_tasks = []

# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            session['user'] = username
            return redirect('/home')
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')


# Home (Task Manager)
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/')
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)


# Add task
@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'user' not in session:
        return redirect('/')

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect('/home')

    return render_template('add.html')


# Edit task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if 'user' not in session:
        return redirect('/')

    if request.method == 'POST':
        tasks[id] = request.form['task']
        return redirect('/home')

    return render_template('edit.html', task=tasks[id])


# Complete task
@app.route('/complete/<int:id>')
def complete(id):
    if 'user' not in session:
        return redirect('/')

    completed_tasks.append(tasks[id])
    tasks.pop(id)
    return redirect('/home')


# Delete completed
@app.route('/delete_completed/<int:id>')
def delete_completed(id):
    if 'user' not in session:
        return redirect('/')

    completed_tasks.pop(id)
    return redirect('/home')


# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)