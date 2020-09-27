from flask import Flask, render_template, url_for

print(__name__)
app = Flask(__name__)

@app.route('/<string:page_name>')
def html_page(page_name):
    """subpages
    """
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return "form submitted holly"