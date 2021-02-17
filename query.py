import shutil
import os
from rank_downloader import download

def clear_pdfs():
    if os.path.exists('pdfs'):
        shutil.rmtree('pdfs')
    os.mkdir('pdfs')

def query_single(stu_id):
    download(stu_id)

def query_multiple(begin, end):
    for x in range(end - begin + 1):
        stu_id = str(begin + x)
        try:
            download(stu_id)
        except IndexError:
            print ('Index out of range, maybe the student has no gpa or is not found')
            os.remove('pdfs{}{}.pdf'.format(os.sep, stu_id))

clear_pdfs()