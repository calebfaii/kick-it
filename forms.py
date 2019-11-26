from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    gender_options = SelectField('Gender',
                                 choices=[('M', 'M'), ('F', 'F')])
    scholarship_options = SelectField('Scholarship',
                                      choices=[('Yes', 'Yes'), ('No', 'No')])
    medication_options = SelectField('Medication',
                                     choices=[('Yes', 'Yes'), ('No', 'No')])
    insurance_options = SelectField('Insurance',
                                    choices=[('Yes', 'Yes'), ('No', 'No')])
    submit = SubmitField('Submit')
