from flask import render_template, request
from app import app
app.debug = True


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    gender_options = ['M', 'F']
    scholarship_options = ['Yes', 'No']
    medication_options = ['Yes', 'No']
    insurance_options = ['Yes', 'No']
    return render_template('index.html',
                           scholarship_options=scholarship_options,
                           gender_options=gender_options,
                           medication_options=medication_options,
                           insurance_options=insurance_options)
