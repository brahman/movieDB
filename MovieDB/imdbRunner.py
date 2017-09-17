__author__ = 'brahma'

import imdbCrawler

try:

    n1 = int(input("start page:"))
    n2 = int(input("end page:"))

    imdbCrawler.imDb.getRawData(n1,n2)



except Exception as x:

    print(x)

    print('Input needs to be an integer',x)


















