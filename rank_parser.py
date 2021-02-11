import camelot
import re
import os
import matplotlib.pyplot as plt

gpas = []
 
def test(school_id):
    tables = camelot.read_pdf('pdfs{}{}'.format(os.sep, school_id), pages='1', flavor='stream')
    data = tables[0].data
    res = ''
    for subdata in data:
        res += subdata[0]

    print ()

    '''
    _name = re.findall(r'学生(?P<name>.*?)（学号', res)
    print ('Hello, %s' %(_name[0]))
    '''
    gpa = re.findall(r'gpa is (?P<gpa>.*?)/', res)
    '''
    print ('Your gpa is %s/4.0' %(gpa[0]))
    rank = re.findall(r'ranked (?P<rank>[\d]+) among (?P<total>[\d]+)', res)
    print ('Your rank is %s/%s' %(rank[0][0], rank[0][1]))
    '''
    
    gpas.append(float(gpa[0]))

for x in os.listdir(path=r'.\pdfs'):
    try:
        print (x)
        test(x)
    except IndexError:
        print ('Index out of range')
    except ValueError:
        print ('Value error')

gpas.sort(reverse=True)
print (gpas)

#Draw
plt.figure(figsize=(10,5))
x = range(1, len(gpas)+1)
plt.plot(x, gpas, 'r--')
plt.savefig('result.jpg')
plt.show()