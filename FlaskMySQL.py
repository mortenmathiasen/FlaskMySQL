from flask import Flask, request, render_template
import pymysql.cursors

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='netrom',
                             db='EmpData',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def HomePage():
    return render_template('login.html')

@app.route("/Authenticate", methods=['POST'])
def Authenticate():
    username = request.form['username']
    password = request.form['password']
    cursor = connection.cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    userfound = cursor.fetchone() is not None
    if userfound:
        cursor.execute("SELECT * FROM User");
        allusers = cursor.fetchall();
        return render_template('login-success.html', userName=username, allusers=allusers)
    else:
        return render_template('login-failed.html')


if __name__ == '__main__':
    app.run()
