import camelot
import re
import os
 
def get_data_from_pdf(stu_id):
    tables = camelot.read_pdf('pdfs{}{}'.format(os.sep, stu_id), pages='1', flavor='stream')
    data = tables[0].data
    res = ''
    for subdata in data:
        res += subdata[0]
    
    return res

def get_details(res):
    _name = re.findall(r'学生(?P<name>.*?)（学号', res)
    gpa = re.findall(r'gpa is (?P<gpa>.*?)/', res)
    
    return {
        'name': _name[0],
        'gpa': gpa[0]
    }
