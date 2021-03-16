__author__ = 'jianxing.wei@wuage.com '

import time
import urllib.request
def time_it(func):
    def wrapper(*arg,**kw):
        t1 = time.time()
        res = func(*arg,**kw)
        t2 = time.time()
        print("consume time is : " + str(t2-t1))
        return (t2-t1),res,func
    return wrapper

@time_it
def perf_measure(url=""):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    data= response.read()
    print(data)
if __name__ =='__main__':
    url='https://s.wuage.com/?psa=W1.a211.c1.2'
    perf_measure(url)
