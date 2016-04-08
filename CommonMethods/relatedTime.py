import time, sys
import datetime
reload(sys)
sys.setdefaultencoding('utf8')


NOWTIMEFORMAT = '%Y-%m-%d %X'
REPORTTIMEFORMAT = '%Y%m%d'



def currenttime():
    now = time.strftime(NOWTIMEFORMAT, time.localtime(time.time()))
    # now = time.time()
    return now

def reporttime():
    now = time.strftime(REPORTTIMEFORMAT, time.localtime(time.time()))
    return now


if __name__ == '__main__':
    print reporttime()