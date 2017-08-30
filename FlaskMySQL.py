from flask import Flask, request, render_template
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'netrom'
app.config['MYSQL_DB'] = 'EmpData'
mysql.init_app(app)

@app.route('/')
def HomePage():
    return render_template('login.html')

@app.route("/Authenticate", methods=['POST'])
def Authenticate():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        userfound = False
    else:
        userfound = True
    return render_template('loginresult.html', userFound=userfound, userName=username)

if __name__ == '__main__':
    app.run()
