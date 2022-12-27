import os, requests, time, random, re, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

v="1.0b"

def update():
    f="webcamX.py"
    data = requests.get(f"https://raw.githubusercontent.com/EvilGeek/WebcamX/master/{f}", verify=False).text
    file = open(f, 'wb')
    file.write(bytes(data, 'utf-8'))
    clear()
    print("Updated Successfull!")
    print("Run The Script Again...")
    print("By using"+BOLD+PURPLE+" python3 webcamX.py"+END+END)
    exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

hList=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13",
"Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (Macintosh; U; Mac OS X 10_6_1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11",
"Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221"]

countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY", 
                 "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
                 "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                 "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                 "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                 "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                 "SY", "TZ", "UG", "UZ", "VC","BJ", ]

def getCamURL(country,):
    urlList=[]
    headers={"user-agent": random.choice(hList)}
    pageReq=requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
    lpage=1
    try:
        lpage= int(re.findall(r'pagenavigator\("\?page=", (\d+)', pageReq.text)[0])
    except IndexError:
        clear()
        print(RED+"Not Available!"+END)
        exit()
    for page in range(lpage):
        req=requests.get(f"http://www.insecam.org/en/bycountry/{country}/?page={page}",headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        info = soup.findAll('div', {'class': "thumbnail-item__preview"})
        for urls in info:
            for url in urls.find_all('img'):
                print(DARKCYAN+url["src"]+END)
                urlList.append(url["src"])
    return urlList

clear()
print(BLUE+"""▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀▄ ▀▀█▀▀ ▀▄▒▄▀ 
▒█░░░ █░░█ █░░█ █▀▀ █░░█ ░░█░░ ░▒█░░ 
▒█▄▄█ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░░▀ ░░▀░░ ▄▀▒▀▄\n\n"""+END)
print(BLUE+"Grab Direct Links to Public Webcams Around the Globe Using this Webcam Scrapper Tool.\nTG : CodentX"+END)
lv = requests.get("https://raw.githubusercontent.com/EvilGeek/WebcamX/master/.version").text
if v.strip() == lv.strip():
    pass
else:
    print(RED+f"Update required! Latest Version:{lv}"+END)
time.sleep(5)
print()

counter=1
for c in countries:
    print(str(counter)+": "+BOLD+c+END)
    counter=counter+1
    

print()
choice=0
try:
    choice=int(input(GREEN+"Choose your Country Code:    "+END))
except ValueError:
	print(RED+"Invalid Input!"+END)
	exit()
except Exception as e:
	print("Error:   \n"+str(e))
	exit()
if choice not in range(len(countries)):
    clear()
    print(RED+"Invalid Choice!"+END)
    exit()
else:
    print("Getting Direct URLs!       ")
    urls=getCamURL(countries[choice-1])
    print()
    if len(urls)>1:
        print(YELLOW+f"Got {len(urls)} URLs"+END)
    else:
    	print(YELLOW+f"Got {len(urls)} URL"+END)