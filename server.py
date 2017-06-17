from mysqlconnection import MySQLConnection
from flask import Flask, redirect, render_template, request, session, flash
import re

app = Flask(__name__)
app.secret_key = open('secret-key.txt', 'r').read().strip()

db = MySQLConnection(app, 'emails')

@app.route('/')
def index():
	return render_template('index.html')


def add(email):
	query = 'insert into emails(email) values(:email)'
	params = {'email': email}
	msg = db.query_db(query, params)
	
	return(msg)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
@app.route('/process', methods=['POST'])
def process():
	email = request.form['email']
	if EMAIL_REGEX.match(email):
		session['valid'] = True
		session['email'] = email
		msg = add(email)
		print(msg)
		return redirect('/success')
	else:
		session['valid'] = False
		flash('Email address invalid')
		return redirect('/')


@app.route('/success')
def success():
	if session['valid']:
	 	query = "select email, DATE_FORMAT(created_at,'%m/%d/%y %I:%i%p') as created_at, id from emails"
	 	emails = db.query_db(query)
	 	emails = [(record['email'], record['created_at'], record['id']) for record in emails]
	 	for i in range(0):
	 		emails += emails # make a long list to test scrolling
	 	print(emails)
	 	return render_template('success.html', emails=emails, email=session['email'])
	else:
		flash('Email address invalid')
		return redirect('/')

@app.route('/remove/<user_id>')
def remove(user_id):
	query = 'delete from EMAILS where id=:id'
	params = {'id': user_id}
	db.query_db(query, params)
	return redirect('/success')

app.run(debug=True)
