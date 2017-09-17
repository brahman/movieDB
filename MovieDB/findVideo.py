
import requests
import json
import difflib
import time

class findVideo():

    @staticmethod
    def getYoutubeData(name,year):


        DEVELOPER_KEY = "AIzaSyDajsUpeoHP6arn27UbqXoAKXpUCtj_JL0"
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"

        movieName = str(name).strip()
        query = movieName + '+malayalam full movie'
        ytId1 = 'https://www.googleapis.com/youtube/v3/videos?id='
        ytId2 = '&part=contentDetails&key=AIzaSyDajsUpeoHP6arn27UbqXoAKXpUCtj_JL0'
        ytId = ''

        ytQ1 = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q='
        ytQ2 = '&key=AIzaSyDajsUpeoHP6arn27UbqXoAKXpUCtj_JL0'

        # Ratings
        # ytR1 = 'https://www.googleapis.com/youtube/v3/videos/getRating?id='
        # ytR2 = '&key=AIzaSyDajsUpeoHP6arn27UbqXoAKXpUCtj_JL0'

        movieTitle = ''
        m = []
        url = []

        v = requests.get(ytQ1+str(query).strip().replace(' ','+').replace('++','+')+ytQ2)


        json_data = json.loads(v.text)


        for i in json_data['items']:

            try:
                movieTitle = str(i['snippet']['title']).lower().replace('malayalam','').replace('full','').replace('movie','').replace('super hit','')
                movieTitle = movieTitle.replace('hd','').replace('film','').replace('upload','').replace('dvd','').replace('online','')
                match = difflib.SequenceMatcher(None, movieTitle, movieName).ratio()


                if str(i['id']['kind']).strip() == 'youtube#video':
                    ytId = str(i['id']['videoId']).strip()
                    r = requests.get(ytId1+ytId+ytId2)
                    # t = requests.get(ytR1 + ytId + ytR2)
                    json_data = json.loads(r.text)


                    for i in json_data['items']:

                        if not ('H') in str(i['contentDetails']['duration']):
                            ''
                        else:

                            m.append(match)
                            url.append('https://www.youtube.com/watch?v=' + ytId)
                            # print(movieTitle, match)
                            # print('https://www.youtube.com/watch?v=' + ytId)
                            # print(i['contentDetails']['duration'])

                if m[0] > 0.3:
                    print(movieName, ' | ',year, ' | ', m[0], ' | ', url[0])
                    break

                else:
                    print(movieName, ' | ',year, ' | ', '', ' | ', 'No Match')
                    break

            except Exception:
                print(movieName, ' | ' ,year, ' | ','', ' | ','Error', ' | ', Exception )
                break



    @staticmethod
    def getDailymotionData(name,year):

        # DEVELOPER_KEY = "AIzaSyDajsUpeoHP6arn27UbqXoAKXpUCtj_JL0"
        # YOUTUBE_API_SERVICE_NAME = "youtube"
        # YOUTUBE_API_VERSION = "v3"

        movieName = str(name).strip()
        query = '"'+ movieName + '+malayalam full movie' + '"'
        ytQ1 = 'https://api.dailymotion.com/videos/?search='
        ytQ2 = '&page=1&limit=3'
        ytId = ''

        m = []
        url = []


        v = requests.get(ytQ1 + str(query).strip().replace(' ', '+').replace('++', '+') + '+' + ytQ2)

        json_data = json.loads(v.text)

        n = 0

        for i in json_data['list']:

            d = requests.get('https://api.dailymotion.com/video/' + str(i['id']).strip() + '?fields=id,title,duration')

            json_data_details = json.loads(d.text)

            try:

                for item in json_data_details:

                    movieTitle = str(json_data_details['title']).lower().replace('malayalam', '').replace('full', '').replace('movie','').replace('super hit', '')
                    movieTitle = movieTitle.replace('hd', '').replace('film', '').replace('upload', '').replace('dvd','').replace('online', '')
                    match = difflib.SequenceMatcher(None, movieTitle, movieName).ratio()

                    url = 'http://www.dailymotion.com/video/' + str(json_data_details['id']).strip()

                if int(json_data_details['duration']) > 1140 and match > 0.35 and n<1:

                    print(movieName  , ' | ',year, ' | ', match , ' | ', '' , ' | ',url)

                    n = n+1

                    break

                    # print(json_data_details['duration'])



            except Exception:
                print(movieName, ' | ', year, ' | ', '', ' | ', 'Error', ' | ', Exception)
                break











