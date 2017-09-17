import findVideo
import csv
import time

csvreader = csv.DictReader(open('moviesfulllist.csv'))

year1 = input("Year 1: ")
year2 = input("Year 2: ")

print(time.localtime())

# TESTING

findVideo.findVideo.getYoutubeData('Bangalore Days','2014')
findVideo.findVideo.getDailymotionData('Bangalore Days','2014')

for item in csvreader:

    if int(item['YEAR']) in range(int(year1),int(year2)):



        findVideo.findVideo.getYoutubeData(item['NAME'].strip(),int(item['YEAR']))
        findVideo.findVideo.getDailymotionData(item['NAME'].strip(),int(item['YEAR']))


print(time.localtime())





