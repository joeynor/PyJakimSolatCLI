# Introduction

_PyJakimSolatCLI_ intends to be a CLI driven application to be used on posix shell environments. The application itself is an interface to the JAKIM's official WEBSITE web API in getting solat prayer times for local malaysian zones and states. Hence, it will not be useful for those living outside of Malaysia. The reason why it was localized to JAKIM is to assure the timing used in Malaysia is correct as published by JAKIM. There are manual calculation methods such as the one publish by islamicfinder, or other muslim websites, but, there are sometimes different than the ones publish by JAKIM. This is due to the many other parameters that are not taken into consideration during calculating the prayer times. Trying to get the exact methods used by JAKIM seems impossible for now, so I decided to just use their current API, used by their own website.

Thank You JAKIM for their generosity for providing web api.

# License

BSD license for now, so you can definitely copy and modify in anyway you want.
But if you can please keep the note above about JAKIM and the thank you note.
And if you are really awesome, include me as one of the original writers. 

# Installation

This is a very simple script.
You may need some things installed, particularly python.
```
apt-get install python pip
```
should do the trick

Also you may need to install the requests python library. For this you can use
```
pip install requests
```

Once you have the correct libraries, you get set the script solatJakim.py to an executable and move it somewhere /usr/bin/ to some other name that you would like.

```
chmod 755 solatJakim.py
sudo cp solatJakim.py /usr/bin/solatJakim
```
to run it

```
solatJakim -h 
```
to see the options that it can take. Common args are imsak, fajr, syuruk, dhuhr, asr, maghrib and isha.

It can also support zones.

```
solatJakim -w asr -z SGR03
```
for example, handles for zone 3 in Selangor

# Availability

Because it depends on JAKIM web api, i cannot give guarantee that this code will work forever, it will primarily dependent on JAKIM good will to keep it open to be used by public. I assume they give let you use it for free, cause their website does the same thing so openly.

# Why bother

Of course i can view the prayer times from JAKIM website or using this awesome oneliner bash script from [sharruzzaman](https://gist.github.com/sharuzzaman/9da402680df7f107dafb96d403e0f95a), but I went to all the trouble writing a python code to get it from JAKIM. This is because, I like CLI, and I spend a considerable amount of time on CLI. More importantly, the CLI allows me to tie it to other python scripts, API and conky. Allowing me to code different format of output and integration not otherwise possible. 

# Contributions for Improvements

Contributers are definitely welcome. I envision that this script should provide the same functionality as in the JAKIM web, with probably better or more options. Currently, it is just enough for me to use in my conky app. Other things that I am considering are:

* using proper class methods and abstraction for long term maintenance
* support for different input options like different locations and zones in Malaysia, weekly output, monthly and etc and provide various options for output
* audio support to run mp3/ogg. 
* reminder notification messages to window manager when enters time, possibly can be done with notify-send
* visualization for next prayer, simple GUI on lua, not sure how to do this yet. either a hook to lua graphical support integration, to be used in conky
* systemtray integration 

# Donation
If you're really generous you can obviously contribute, send me a message and ill share you my crypto address




