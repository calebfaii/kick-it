from flask import render_template, request
from app import app
from forms import FilterForm
from server import excel_handler


raw_data = excel_handler.load_from_server()
headers = raw_data[0]
table_elements = raw_data[1]


@app.route('/', methods=['GET', 'POST'])
def filterform():
    # form = FilterForm()
    return render_template('index.html')


@app.route('/results', methods=['GET'])
def grid():
    return render_template('results.html',
                           headers=headers,
                           table_elements=table_elements)
