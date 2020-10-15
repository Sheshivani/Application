from flask import Flask,request,render_template,redirect,session
import os
from flask_mysqldb import MySQL
#import mysql.connector

app = Flask(__name__)
app.secret_key= os.urandom(24) # secret create after login, save in server and browser's cookies and save in server
# inparticular time but key can expire session in server or browser in case u don't recognize key yet u have again login

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Shivani1@'
app.config['MYSQL_DB']='myuser'

mysql = MySQL(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:       # inside of session 'user_id' name variable is available
        return render_template('home.html')
    else:       # if Not available
        return redirect('/')

@app.route('/login_validator',methods=['POST'])
def login_validator():
    cursor = mysql.connection.cursor()            #To communicated with database
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """
                   .format(email, password))     # to send query to database
    data= cursor.fetchall()                      # To fetch query's data and result save in list form
    print(data)                                  # see data in terminal and Tuple from
    if len(data)>0:                              # To check data entry in login page match to database table
        session['user_id']=data[0][0]
        return redirect('/home')      #if yes open homepage
    else:
        return redirect('/')     # if not to reopen login page

@app.route('/add_user',methods=['POST'])
def add_user():
    cursor = mysql.connection.cursor()
    name=request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')"""
                   .format(name,email,password))  # to send query in database
    mysql.connection.commit() # In relational data,commit to store complete detail's users table and database query save

    cursor .execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email)) # email is common register and
    # login page
    user=cursor.fetchall() #created data can fetch
    session['user_id']=user[0][0]  # user fetch data'id is stored in session,generate session key

    return redirect ('/home')    #

@app.route('/logout')
def logout():
    session.pop('user_id') # session stored element in dictionary type, so pop delete dictionary element('user_id')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
