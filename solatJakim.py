#!/usr/bin/python
# importing the requests library, use pip install requests
import requests
import json
import datetime
import sys, getopt
"""

Still working on this code
example usage for now
printPrayerTimes()
print ('\n\n')
printPrayerTimes('asr')

"""


# defining the api-endpoint  
JAKIM_API = "https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=duration&zone=SGR01"


#setting the date for POST data
datenow= datetime.datetime.now()
datestart = datenow.strftime("%Y-%m-%d")
dateend = datestart
data = {'datestart':datestart, 
        'dateend':dateend}

  
# sending post request and saving response as response object 
r = requests.post(url = JAKIM_API, data = data) 
  
# extracting response text  
pastebin_url = r.text
solatinfo_dict = json.loads(pastebin_url)

waktuBM = {"imsak":"Imsak","fajr":"Subuh","syuruk":"Shuruk","dhuhr":"Zohor","asr":"Asar","maghrib":"Maghrib","isha":"Isyak"}

def printPrayerTimes(waktu='all'):
    if (waktu=='all'):
        print("Waktu solat bagi " + solatinfo_dict['prayerTime'][0]['hijri'] + "\n")
        print(waktuBM['imsak']+" : " + solatinfo_dict['prayerTime'][0]['imsak'])
        print(waktuBM['fajr']+" : " + solatinfo_dict['prayerTime'][0]['fajr'])
        print(waktuBM['syuruk']+" : " + solatinfo_dict['prayerTime'][0]['syuruk'])
        print(waktuBM['dhuhr']+" : " + solatinfo_dict['prayerTime'][0]['dhuhr'])
        print(waktuBM['asr']+" : " + solatinfo_dict['prayerTime'][0]['asr'])
        print(waktuBM['maghrib']+" : " + solatinfo_dict['prayerTime'][0]['maghrib'])
        print(waktuBM['isha']+" : " + solatinfo_dict['prayerTime'][0]['isha'])      
    elif waktu == 'hijri':
        print("Waktu solat bagi " + solatinfo_dict['prayerTime'][0]['hijri'] + "\n")
    else:
        print(waktuBM[waktu]+" : " + solatinfo_dict['prayerTime'][0][waktu])
        
def main(argv):
    waktu = 'all';
    try:
        opts, args = getopt.getopt(argv,"hwd",["waktu="])
    except getopt.GetoptError:
        print 'solatJakim -w <waktusolat>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'solatJakim -w <imsak|fajr|syuruk|dhuhr|maghrib|isha>'
            sys.exit()
        elif opt in ("-w", "--waktu"):
            waktu = argv[1]
            printPrayerTimes(waktu)
        elif opt in ("-d", "--islamicDate"):
            printPrayerTimes('hijri')
  
if __name__== "__main__":
    main(sys.argv[1:])

