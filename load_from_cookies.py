from login import login
import msession
import pickle
import os

def test_connection(url, pattern):
    res = msession.session.get(url, verify=False)
    if pattern in res.text:
        print ('Login successfully')
        return True
    else:
        print ('Failed to login, maybe cookies are expired')
        return False

def load_from_cookies(usrname):
    session = msession.session

    if not os.path.exists('cookies') or not usrname in os.listdir('cookies'):
        print ('No such user, please login first!')
        password = input('Please input the password of {}:'.format(usrname))
        login(usrname, password)

    file_name = 'cookies' + os.sep + usrname
    with open(file_name, 'rb') as cookies:
        session.cookies.update(pickle.load(cookies))

    print ('Testing accessibility to 广大门户... ')
    test_connection(msession.urls.mygzhu, '主页')
    print ('Testing accessibility to 教务系统... ')
    
    if not test_connection(msession.urls.jwxt, '个人信息'):
        print ('Failed, please login again manually')
        session.cookies.clear()
        password = input('Please input the password of {}:'.format(usrname))
        login(usrname, password)