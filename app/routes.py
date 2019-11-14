from flask import render_template, request
from app import app
from server import excel_handler
raw_data = excel_handler.load_from_server()
headers = raw_data[0]
table_elements = raw_data[1]


@app.route('/', methods=['GET', 'POST'])
def dropdown_values():
    gender_options = ['M', 'F']
    scholarship_options = ['Yes', 'No']
    medication_options = ['Yes', 'No']
    insurance_options = ['Yes', 'No']
    if request.method == "POST":
        if request.form['submit'] == "Search for Sober Houses":
            return render_template('results.html',
                                   headers=headers,
                                   table_elements=table_elements)
    return render_template('index.html',
                           scholarship_options=scholarship_options,
                           gender_options=gender_options,
                           medication_options=medication_options,
                           insurance_options=insurance_options)


@app.route('/results', methods=['GET'])
def grid():
    return render_template('results.html',
                           headers=headers,
                           table_elements=table_elements)
