from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    message = "Travis is a gay ball"
    return render_template('index.html')
