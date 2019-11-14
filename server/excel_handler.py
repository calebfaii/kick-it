from openpyxl import load_workbook


class ExcelHandler(object):
    def __init__(self):
        self.data = None

    def load_data_from_excel(self):
        wb = load_workbook(filename='server/DB.xlsx')
        sheet = wb['Soberhouses']
        raw_data = []
        for row in sheet:
            row_values = [cell.value.encode('ascii', 'ignore') for cell in row]
            raw_data.append(row_values)
        self.data = raw_data

    def get_data(self):
        return self.data


class Soberhouse(object):
    def __init__(self, record):
        self.record = record
        self.institution_name = None
        self.address = None
        self.phone = None
        self.gender = None
        self.scholarships_accepted = None
        self.medication_permitted = None
        self.insurance_accepted = None
        self.set_attributes()

    def set_attributes(self):
        self.institution_name = self.record[0]
        self.address = self.record[1]
        self.phone = self.record[2]
        self.gender = self.record[3]
        self.scholarships_accepted = self.record[4]
        self.medication_permitted = self.record[5]
        self.insurance_accepted = self.record[6]


def load_from_server():
    handler = ExcelHandler()
    handler.load_data_from_excel()
    data = handler.get_data()
    headers = []
    elements = []
    for row in data:
        record_object = Soberhouse(row)
        elements.append(record_object)
    headers.append(elements[0])
    elements.remove(elements[0])
    return [headers, elements]
