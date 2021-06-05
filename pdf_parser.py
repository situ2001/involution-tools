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
    stu_id = re.findall(r'（学号：(?P<id>.*?)）', res)
    _class = re.findall(r'专业(?P<class>.*?)班', res)
    major = re.findall(r'[0-9]级(?P<major>.*?)专业', res)
    _name = re.findall(r'学生(?P<name>.*?)（学号', res)
    gpa = re.findall(r'绩点为：(?P<gpa>.*?)/', res)
    
    return {
        '专业': major[0],
        '班级': _class[0],
        '学号': stu_id[0],
        '姓名': _name[0],
        '绩点': gpa[0]
    }
