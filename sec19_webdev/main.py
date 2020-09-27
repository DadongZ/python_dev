from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<username>/<int:post_id>')
def hello_user(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return 'Blog page'

@app.route('/blog/2020/cats')
def blog2020():
    return 'This page is about cats'
