#!/usr/bin/python
# importing the requests library, use pip install requests
import requests
import json
import datetime
import sys, getopt

default_zone = 'SGR01'

waktuBM = {"imsak":"Imsak","fajr":"Subuh","syuruk":"Syuruk","dhuhr":"Zohor","asr":"Asar","maghrib":"Maghrib","isha":"Isyak"}
zones = {
    'JHR01':'JHR01 - Pulau Aur dan Pulau Pemanggil',
    'JHR02':'JHR02 - Johor Bahru, Kota Tinggi, Mersing',
    'JHR03':'JHR03 - Kluang, Pontian',
    'JHR04':'JHR04 - Batu Pahat, Muar, Segamat, Gemas Johor',
    'KDH01':'KDH01 - Kota Setar, Kubang Pasu, Pokok Sena (Daerah Kecil)',
    'KDH02':'KDH02 - Kuala Muda, Yan, Pendang',
    'KDH03':'KDH03 - Padang Terap, Sik',
    'KDH04':'KDH04 - Baling',
    'KDH05':'KDH05 - Bandar Baharu, Kulim',
    'KDH06':'KDH06 - Langkawi',
    'KDH07':'KDH07 - Puncak Gunung Jerai',
    'KTN01':'KTN01 - Bachok, Kota Bharu, Machang, Pasir Mas, Pasir Puteh, Tanah Merah, Tumpat, Kuala Krai, Mukim Chiku',
    'KTN03':'KTN03 - Gua Musang (Daerah Galas Dan Bertam), Jeli',
    'MLK01':'MLK01 - SELURUH NEGERI MELAKA',
    'NGS01':'NGS01 - Tampin, Jempol',
    'NGS02':'NGS02 - Jelebu, Kuala Pilah, Port Dickson, Rembau, Seremban',
    'PHG01':'PHG01 - Pulau Tioman',
    'PHG02':'PHG02 - Kuantan, Pekan, Rompin, Muadzam Shah',
    'PHG03':'PHG03 - Jerantut, Temerloh, Maran, Bera, Chenor, Jengka',
    'PHG04':'PHG04 - Bentong, Lipis, Raub',
    'PHG05':'PHG05 - Genting Sempah, Janda Baik, Bukit Tinggi',
    'PHG06':'PHG06 - Cameron Highlands, Genting Higlands, Bukit Fraser',
    'PLS01':'PLS01 - Kangar, Padang Besar, Arau',
    'PNG01':'PNG01 - Seluruh Negeri Pulau Pinang',
    'PRK01':'PRK01 - Tapah, Slim River, Tanjung Malim',
    'PRK02':'PRK02 - Kuala Kangsar, Sg. Siput (Daerah Kecil), Ipoh, Batu Gajah, Kampar',
    'PRK03':'PRK03 - Lenggong, Pengkalan Hulu, Grik',
    'PRK04':'PRK04 - Temengor, Belum',
    'PRK05':'PRK05 - Kg Gajah, Teluk Intan, Bagan Datuk, Seri Iskandar, Beruas, Parit, Lumut, Sitiawan, Pulau Pangkor',
    'PRK06':'PRK06 - Selama, Taiping, Bagan Serai, Parit Buntar',
    'PRK07':'PRK07 - Bukit Larut',
    'SBH01':'SBH01 - Bahagian Sandakan (Timur), Bukit Garam, Semawang, Temanggong, Tambisan, Bandar Sandakan, Sukau',
    'SBH02':'SBH02 - Beluran, Telupid, Pinangah, Terusan, Kuamut, Bahagian Sandakan (Barat)',
    'SBH03':'SBH03 - Lahad Datu, Silabukan, Kunak, Sahabat, Semporna, Tungku, Bahagian Tawau  (Timur)',
    'SBH04':'SBH04 - Bandar Tawau, Balong, Merotai, Kalabakan, Bahagian Tawau (Barat)',
    'SBH05':'SBH05 - Kudat, Kota Marudu, Pitas, Pulau Banggi, Bahagian Kudat',
    'SBH06':'SBH06 - Gunung Kinabalu',
    'SBH07':'SBH07 - Kota Kinabalu, Ranau, Kota Belud, Tuaran, Penampang, Papar, Putatan, Bahagian Pantai Barat',
    'SBH08':'SBH08 - Pensiangan, Keningau, Tambunan, Nabawan, Bahagian Pendalaman (Atas)',
    'SBH09':'SBH09 - Beaufort, Kuala Penyu, Sipitang, Tenom, Long Pa Sia, Membakut, Weston, Bahagian Pendalaman (Bawah)',
    'SGR01':'SGR01 - Gombak, Petaling, Sepang, Hulu Langat, Hulu Selangor, S.Alam',
    'SGR02':'SGR02 - Kuala Selangor, Sabak Bernam',
    'SGR03':'SGR03 - Klang, Kuala Langat',
    'SWK01':'SWK01 - Limbang, Lawas, Sundar, Trusan',
    'SWK02':'SWK02 - Miri, Niah, Bekenu, Sibuti, Marudi',
    'SWK03':'SWK03 - Pandan, Belaga, Suai, Tatau, Sebauh, Bintulu',
    'SWK04':'SWK04 - Sibu, Mukah, Dalat, Song, Igan, Oya, Balingian, Kanowit, Kapit',
    'SWK05':'SWK05 - Sarikei, Matu, Julau, Rajang, Daro, Bintangor, Belawai',
    'SWK06':'SWK06 - Lubok Antu, Sri Aman, Roban, Debak, Kabong, Lingga, Engkelili, Betong, Spaoh, Pusa, Saratok',
    'SWK07':'SWK07 - Serian, Simunjan, Samarahan, Sebuyau, Meludam','SWK08':'SWK08 - Kuching, Bau, Lundu, Sematan',
    'SWK09':'SWK09 - Zon Khas (Kampung Patarikan)',
    'TRG01':'TRG01 - Kuala Terengganu, Marang, Kuala Nerus',
    'TRG02':'TRG02 - Besut, Setiu',
    'TRG03':'TRG03 - Hulu Terengganu',
    'TRG04':'TRG04 - Dungun, Kemaman',
    'WLY01':'WLY01 - Kuala Lumpur, Putrajaya',
    'WLY02':'WLY02 - Labuan'
}

def setDefaultZone(zone):
    global default_zone
    default_zone = zone

def printZone():
    for zone in zones:
        print(zones[zone])
    
def printPrayerTimes(waktu='all'):
    # defining the api-endpoint  
    JAKIM_API = "https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=duration&zone="+default_zone


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
    
    if (waktu=='all'):
        print("Bagi Tahun " + solatinfo_dict['prayerTime'][0]['hijri'] + '. Waktu solat bagi kawasan:')
        print(zones[default_zone]) 
        print(waktuBM['imsak']+" : " + solatinfo_dict['prayerTime'][0]['imsak'])
        print(waktuBM['fajr']+" : " + solatinfo_dict['prayerTime'][0]['fajr'])
        print(waktuBM['syuruk']+" : " + solatinfo_dict['prayerTime'][0]['syuruk'])
        print(waktuBM['dhuhr']+" : " + solatinfo_dict['prayerTime'][0]['dhuhr'])
        print(waktuBM['asr']+" : " + solatinfo_dict['prayerTime'][0]['asr'])
        print(waktuBM['maghrib']+" : " + solatinfo_dict['prayerTime'][0]['maghrib'])
        print(waktuBM['isha']+" : " + solatinfo_dict['prayerTime'][0]['isha'])      
    elif waktu == 'hijri':
        print("Tahun Islam " + solatinfo_dict['prayerTime'][0]['hijri'])
    else:
        print(waktuBM[waktu]+" : " + solatinfo_dict['prayerTime'][0][waktu])
        
def main(argv):
    global waktu,default_zone
    waktu='all'
    try:
        opts, args = getopt.getopt(argv,"hwdzk",["waktu="])
    except getopt.GetoptError:
        print('Needs args for correct usage refer to: solatJakim -h')
        exit(2)
    if len(opts)==0:
        setDefaultZone('SGR01')
        printPrayerTimes();
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('solatJakim -w <all|imsak|fajr|syuruk|dhuhr|maghrib|isha> -z [default_zone=SGR01]')
            print('solatJakim -w <all|imsak|fajr|syuruk|dhuhr|maghrib|isha>')
            print('solatJakim [default waktu=all,default_zone=SGR01]')
            print('\n')
            print('Supported zones are : ')
            printZone();
            sys.exit(2)
        elif opt in ("-w", "--waktu"):
            waktu = args[0]
            if len(args)<=1:
                printPrayerTimes(waktu)
                exit(2)
            else:
                if args[1] == '-z':
                    try:
                        if args[2] not in zones:
                            print("Invalid Zones, valid zones with -z are : \n" )
                            printZone()
                        else:
                            setDefaultZone(args[2])
                            printPrayerTimes(waktu)
                    except:
                        print("Missing zone identifier, valid zones are : \n" )
                        printZone()
        elif opt in ("-d", "--islamicDate"):
            printPrayerTimes('hijri')
            exit(2)
        elif opt in ("-z", "--zones"):
            setDefaultZone(args[0])
            print(zones[default_zone])
            exit(2)

if __name__== "__main__":
    main(sys.argv[1:])

