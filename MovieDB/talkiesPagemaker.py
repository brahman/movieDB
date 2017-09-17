import csv
import difflib

class talkies():

    @staticmethod
    def compareEinthusan():

        e = []
        eurl = []
        imdb = []

        csvreader = csv.DictReader(open('einthu.csv'))

        csvreader1 = csv.DictReader(open('imdblist2000s.csv'))
        count = 0

        for i in csvreader:
            e.append(i['NAME'])
            eurl.append(i['URL'])


        for item in csvreader1:
            imdb.append(item['NAME'])

        for j,l in zip(e,eurl):
            for k in imdb:
                match = difflib.SequenceMatcher(None, j,k).ratio()
                if match > 0.9:
                    print(k,'|',l,'|', match)

    @staticmethod
    def createTalkiesHtml(year):

        csvreader = csv.DictReader(open('DB4.csv'))
        year = int(year)

        for item in csvreader:

            count = 0

            if int(item['YEAR']) == year:


                try:
                    name = "<h3>" + item['NAME'] + "</h3>"
                    watchonline = "Watch Online :"
                    youtubeLink = ""
                    dmLink = ""
                    einthLink = ""

                    if not ('youtube.com') in str(item['Youtube']):
                        ''
                    else:
                        youtubeLink = "<a href=" + str(item['Youtube'])+ '"' + ">Youtube</a>"
                        count = count + 1

                    if not ('dailymotion.com') in str(item['Youtube']):
                        ''
                    else:
                        dmLink = watchonline + "<a href=" + str(item['Dailymotion'])+ '"' + ">Daily Motion</a>"
                        count = count + 1

                    if not ('einthusan.tv') in str(item['Einthusan']):
                        ''
                    else:
                        einthLink = "<a href=" + str(item['Einthusan'])+ '"' + ">Einthusan</a>"
                        count = count + 1

                    if count > 0:

                        print(name)
                        print(watchonline + "   " + youtubeLink + "   " + dmLink + "   " + einthLink)

                        if not item['PLOT']:
                            ""
                        else:
                            print (item['PLOT'])




                        if float(item['RATING']) > 0:

                            print ("IMDB Rating :"+"<a href=" + str(item['URL'])+ '">' + item['RATING'] +"</a>")

                        # if not item['DIRECTORS']:
                        #     ""
                        # else:
                        #     print ("Directed By :" + item['DIRECTORS'])
                        #
                        # if not item['ACTORS']:
                        #     ""
                        # else:
                        #     print ("Cast :"+ item['ACTORS'])

                except Exception:
                   ''








