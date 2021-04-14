from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#aby2L"F4Q8z\n\xec]'


@app.route('/hello_flask')
def hello_flask():
    return render_template('hello_flask.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_confirm', methods=['POST'])
def login_confirm():
    id_ = request.form['id_']
    pw_ = request.form['pw_']
    if (id_ == 'admin' and pw_ == 'admin') or (id_ == 'user' and pw_ == 'user'):
        session['id'] = id_
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


host_addr = "0.0.0.0"
port_num = "8080"
if __name__ == "__main__":
    app.run(host_addr, port_num)
