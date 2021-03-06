from flask import Flask, render_template, request
import sqlite3
#import sqlachemy
import datetime


#Connection to DataBase
'''
conn = sqlite3.connect('DATABASE.db') 
c = conn.cursor()

def create_table(): 
	c.execute('CREATE TABLE IF NOT EXISTS Employee (ID INT(6) primary key, Name varchar(20) not null,Mail varchar(30),Mobile INT(10))')
'''
app = Flask(__name__,template_folder='template')

@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html')

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
	id1 = request.form['id1']
	fname = request.form['fname']
	lname = request.form['lname']
	mobile = request.form['mb']
	email = request.form['email']
	Insert_Data(id1,fname,lname,mobile,email)
	print ("ID : " + id1 +"\nFirst Name : " + fname+"\nLast Name : " + lname + "\nMobile : "+ mobile +"\nEmail : "+ email)
	return "Data sent. Please check your program log"

@app.route('/fetchid')
def Display_By_ID(id1):
	conn = sqlite3.connect('DATABASE.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Employee WHERE ID=={}".format(id1))
	data = c.fetchall()
	for i in data:
		print(i)
	return "Hello!"

def Insert_Data(id1,fname,lname,mobile,email):
	conn = sqlite3.connect('DATABASE.db')
	c = conn.cursor()
	c.execute("INSERT INTO Employee (ID, FName, LName, Mail, Mobile) VALUES(?,?,?,?,?)", (id1, fname, lname, email, mobile))
	conn.commit()

def Display_All_Data():
	conn = sqlite3.connect('DATABASE.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Employee")
	data = c.fetchall()
	for i in data:
		print(i)

def create_table():
	conn = sqlite3.connect('DATABASE.db')
	c = conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS Employee (ID INT(6) primary key, FName varchar(20) not null,LName varchar(20) not null,Mail varchar(30),Mobile INT(10))')


@app.route('/showall')
def example():
	conn = sqlite3.connect('DATABASE.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Employee")
	data = c.fetchall()
	return render_template('Output_All.html', output_data = data)


if __name__ == '__main__':
	create_table()
	app.run(debug=True)