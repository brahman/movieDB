__author__ = 'brahma'

import requests
import bs4
import csv



class einthusan():

    @staticmethod
    def getpagehtml():
        pagenumber = 1

        while pagenumber > 0:

            try:

                einthusanurl = "https://einthusan.tv/movie/results/?decade=1980&find=Decade&lang=malayalam&page=" + str(pagenumber)
                siteRaw = requests.get(einthusanurl)
                soup = bs4.BeautifulSoup(siteRaw.text, "html.parser")

                r = soup.findAll('a')

                for string in r:
                    t = str(string)
                    # print(p)
                    if t.find('"title"') > 0:

                        t= t.replace('<a class="title" href="','')
                        t =t.replace('</h3></a>', '')
                        t = t.replace('</h3 >< span', '|')
                        t =t.replace('"><h3>', '|')

                        print(t)

                # prints YEAR
                # p = soup.findAll('p')
                #
                # for string in p:
                #     q = str(string)
                #     if q.find('<span>Malayalam') > 0:
                #
                #         q= q.replace('<p>','')
                #         q =q.replace('<span>Malayalam</span></p>', '')
                #         # print(q)





                        #print(pagenumber)
                pagenumber = pagenumber - 1
            except:
                print('Error')

    @staticmethod
    def createpagehtml(filename):

        csvreader = csv.DictReader(open(filename + ".csv"))

        #custom variables for creating html
        text1 = ' - <a href="'
        text2 = '" target="_blank" rel="noopener">watch online</a>'
        for item in csvreader:

            name = item['Name']
            URL = item['URL']

            print(name + text1+ URL+ text2)
            print('                       ')





















