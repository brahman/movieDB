__author__ = 'brahma'

import requests
import bs4
import re
import csv



class imDb():

    @staticmethod
    def getRawData(startpage,endpage):

        n1 = int(startpage)
        n2 = int(endpage)

        filenamer = 'malayalam.csv'
        csvfile = open(filenamer, 'a', newline='')
        rawriter = csv.writer(csvfile)
        rawriter.writerow(['INFO'])

        for i in range(n1,n2):

            pno = str(i)

            imdbUrl = "http://www.imdb.com/search/title?title_type=feature&primary_language=ml&view=advanced&sort=year,desc&page="+pno

            print("Processing page", pno , "of", n2)

            siteRaw = requests.get(imdbUrl)
            soup = bs4.BeautifulSoup(siteRaw.text, "html.parser")
            movieDiv = soup.findAll('div')

            name = ''
            director = ''
            year = ''
            genre = ''
            plot = ''
            rating = ''
            actors = ''
            movieInfo = ''


            for item in movieDiv:

                movieAll = str(item)

                if movieAll.find("lister-item mode-advanced") > 0:

                    movieSoup = bs4.BeautifulSoup(movieAll, "html.parser")

                    a = movieSoup.findAll('a')

                    for string1 in a:
                        atag = str(string1)

                        if atag.find('adv_li_tt')>0:
                            atag = str(atag).replace('<a href="', '|http://www.imdb.com')
                            atag = str(atag).replace('?ref_=adv_li_tt">', ' | ')
                            atag = str(atag).replace('</a>', '')
                            # print("Name and URL |",atag.strip())
                            name = atag.strip()


                        elif atag.find('adv_li_dr_0')>0:
                            atag = str(atag).replace('<a href="', '|http://www.imdb.com')
                            atag = str(atag).replace('?ref_=adv_li_dr_0">', ' | ')
                            atag = str(atag).replace('</a>', '')
                            # print("Director |",atag.strip())
                            director = atag.strip()

                        elif atag.find('adv_li_st') > 0:
                            atag = str(atag).replace('<a href="', '|http://www.imdb.com')
                            atag = str(atag).replace('">', '|')
                            atag = str(atag).replace('</a>', '')
                            # print("Cast |",atag.strip())
                            actors = actors + "," + atag.strip()

                    s = movieSoup.findAll('span')

                    for string2 in s:
                        stag = str(string2)
                        if stag.find('lister-item-year')>0:
                            match = re.search(r'\d\d\d\d', str(stag))
                            if match:
                                ''
                                # print('Year |', match.group(),' | ')
                                year = str(match.group()).strip()
                            else:
                                ''
                                # print('did not find')
                        elif stag.find('class="genre')>0:
                            stag = str(stag).replace('<span class="genre">', '')
                            stag = str(stag).replace('</span>', '')
                            stag = str(stag).replace(' ','')
                            # print("Genre |",stag.strip())
                            genre = stag.strip().replace(' ','')

                    m = movieSoup.findAll('meta')

                    for string3 in m:
                        mtag = str(string3)
                        if mtag.find('ratingValue')>0:

                            mtag = str(mtag).replace('<meta content="', '')
                            mtag = str(mtag).replace('" itemprop="ratingValue"/>', '')
                            # print("IMDB Rating |",mtag.strip())
                            Rating = mtag.strip()

                    p = movieSoup.findAll('p')

                    for string4 in p:
                        ptag = str(string4)
                        if ptag.find('text-muted') > 0:
                            ptag = str(ptag).replace('<p class="text-muted">', '')
                            ptag = str(ptag).replace('</p>', '')

                            if len(ptag.strip()) > 75:
                                match1 = re.search(r'</span>', str(ptag))
                                if match1:
                                    ''
                                else:
                                    plot = ptag.strip()

                                # print("Summary |", ptag.strip())
                                # if not ('class="runtime' or 'class="sort-num_votes-visible"') in ptag:
                                #     plot = ptag.strip()



                    # print(name,'|', Rating ,'|', plot,'|',  genre ,'|',  director ,'|',  actors  )

                    movieInfo = year + '|' + name + '|'+Rating + '|'+plot + '|'+genre + '|' + director + '|'+actors

                    rawriter.writerow([movieInfo])


                    name = ''
                    director = ''
                    year = ''
                    genre = ''
                    plot = ''
                    rating = ''
                    actors = ''
                    movieInfo = ''

