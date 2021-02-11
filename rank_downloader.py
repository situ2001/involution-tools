import shutil
from load_from_cookies import load_from_cookies
import msession
import re
import camelot
import os
import sys

session = msession.session
args = sys.argv

load_from_cookies(args[1])

url = msession.urls.rank

def output(stu_id):
    data_post = {
        'pk': '114514',
        'pk_1': '1919810',
        'xh': stu_id,
        'xh_1': '114514',
        'xnm': '9999',
        'xnm_1': '9999',
        'xqn': '12',
        'xqn_1': '12'
    }

    res = session.post(url, data=data_post)

    content = res.text

    sessionID = re.findall(r'this.currentSessionID = \'(?P<ID>.*?)\';', content)

    url_pdf_download = 'http://jwxtbb.gzhu.edu.cn/WebReport/ReportServer?op=export&sessionID={}&format=pdf&extype=ori'.format(sessionID[0])

    res_pdf = session.get(url_pdf_download)

    with open ('pdfs{}{}.pdf'.format(os.sep, stu_id), mode='wb') as f:
        for chunk in res_pdf.iter_content(chunk_size=10240):
            f.write(chunk)

    tables = camelot.read_pdf('pdfs{}{}.pdf'.format(os.sep, stu_id), pages='1', flavor='stream')
    data = tables[0].data
    res = ''
    for subdata in data:
        res += subdata[0]

    print()

    #processing
    _name = re.findall(r'学生(?P<name>.*?)（学号', res)
    print ('%s, ' %(_name[0]), end='')
    gpa = re.findall(r'gpa is (?P<gpa>.*?)/', res)
    print ('your GPA is %s/4.0' %(gpa[0]), end='')
    rank = re.findall(r'ranked (?P<rank>[\d]+) among (?P<total>[\d]+)', res)
    print (', rank is %s/%s' %(rank[0][0], rank[0][1]))

begin = int(args[2])
end = int(args[3])

print ('Begin downloading...')

if os.path.exists('pdfs'):
    shutil.rmtree('pdfs')

os.mkdir('pdfs')

for x in range(end - begin + 1):
    stu_id = str(begin + x)
    try:
        output(stu_id=stu_id)
    except IndexError:
        print ('Index out of range')