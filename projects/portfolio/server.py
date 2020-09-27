from flask import Flask, render_template, url_for, request, redirect
import csv

print(__name__)
app = Flask(__name__)

@app.route('/')
def root_page():
    """home
    """
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    """subpages
    """
    return render_template(page_name)

def write_to_db(data):
    """write_contact_to_database
    """
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', 'a') as   database:
        file = database.write(f'\n{email}, {subject}, {message}')  

def write_to_csv(data):
    """write_contact_to_csv
    """
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', 'a', newline='') as   db:
        csv_writer = csv.writer(db, delimiter=',', quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank.html')
        except:
            return 'oops, something wrong!'
    else:
        return "something went wrong, Try again!"