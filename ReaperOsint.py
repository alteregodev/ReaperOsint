import phonenumbers as num
import exifread
import requests
import webbrowser
from googlesearch import search
from phonenumbers import geocoder, carrier, timezone

gr = '\033[32m'
wh = '\033[0m'

def get_info_by_ip(ip='127.0.0.1'):
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        if response.get('country') == None:
            print(f'{wh}[{gr}+{wh}] Invalid IP')

        else:
            data = {
                '[IP]': response.get('query'),
                '[Provider]': response.get('isp'),
                '[Organization]': response.get('org'),
                '[Country]': response.get('country'),
                '[Region]': response.get('regionName'),
                '[City]': response.get('city'),
                '[Postal]': response.get('zip'),
                '[Latitude]': response.get('lat'),
                '[Longtitude]': response.get('lon'),
            }

            for k, v in data.items():
                print(f'{wh}[{gr}+{wh}] {wh}{k} : {gr}{v}')

def username_check():
    try:
        username = input(f'{wh}[{gr}+{wh}] Enter username: ')
        print(f'{wh}[{gr}+{wh}] This might take a while...')
        results = {}

        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
            ]

        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)

            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{gr}Username not found!")

        for site, result in results.items():
            print(f"{wh}[{gr}+{wh}] {site}: {gr}{result}")

    except Exception as e:
        print(f"{wh}[{gr}+{wh}] Error : {gr}{e}")
        return

def extract_image_metadata(image_path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)

        if not tags:
            print(f"{wh}[{gr}+{wh}] No EXIF metadata found in this image.\n")
            return

        print(f'{wh}[{gr}+{wh}] {wh}Found EXIF metadata: ')
        for tag, value in tags.items():
            print(f"{wh}[{gr}+{wh}] [{tag}] : {value}")
        print('')

    except FileNotFoundError:
        print(f'{wh}[{gr}+{wh}] No such file in current directory')

banner1 = (f'''{gr}
  /$$$$$$            /$$             /$$          /$$$$$$$                                                   
 /$$__  $$          |__/            | $$         | $$__  $$                                                  
| $$  \ $$  /$$$$$$$ /$$ /$$$$$$$  /$$$$$$       | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$  | $$ /$$_____/| $$| $$__  $$|_  $$_//$$$$$$| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  | $$|  $$$$$$ | $$| $$  \ $$  | $$ |______/| $$__  $$| $$$$$$$$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$ \____  $$| $$| $$  | $$  | $$ /$$     | $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$_____/| $$      
|  $$$$$$/ /$$$$$$$/| $$| $$  | $$  |  $$$$/     | $$  | $$|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
 \______/ |_______/ |__/|__/  |__/   \___/       |__/  |__/ \_______/ \_______/| $$____/  \_______/|__/      
                                                                               | $$                          
                                                                               | $$                          
                                                                               |__/                             
                                                                               
{gr}@ {wh}BY ALTER.EGO \n
{wh}[{gr}1{wh}] Parse phone number                         [{gr}4{wh}] Search Internet
{wh}[{gr}2{wh}] Search IP                                  [{gr}5{wh}] Image Exif metadata
{wh}[{gr}3{wh}] IP Logger                                  [{gr}6{wh}] Username Checker
                                               [{gr}0{wh}] Exit
    ''')

banner2 = (f'''{gr}
{gr}              ...                            
{gr}              ;::::;                           
{gr}            ;::::; :;                          
{gr}          ;:::::'   :;                               {wh}┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
{gr}        ;:::::;     ;.                              
{gr}        ,:::::'       ;           OOO\                       {gr}@ {wh}BY ALTER.EGO
{gr}        ::::::;       ;          OOOOO\                 {wh}discord - {gr}fucksociety.com
{gr}        ;:::::;       ;         OOOOOOOO                   {gr}github/alteregodev
{gr}       ,;::::::;     ;'         / OOOOOOO            
{gr}     ;:::::::::`. ,,,;.        /  / DOOOOOO          {wh}┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
{gr}   .';:::::::::::::::::;,     /  /     DOOOO   
{gr}  ,::::::;::::::;;;;::::;,   /  /        DOOO  
{gr} ;`::::::`'::::::;;;::::: ,#/  /          DOOO 
{gr} :`:::::::`;::::::;;::: ;::#  /            DOOO
{gr} ::`:::::::`;:::::::: ;::::# /              DOO
{gr} `:`:::::::`;:::::: ;::::::#/               DOO
{gr}  :::`:::::::`;; ;:::::::::##                OO
{gr}  ::::`:::::::`;::::::::;:::#                OO
{gr}  `:::::`::::::::::::;'`:;::#                O 
{gr}   `:::::`::::::::;' /  / `:#                  
{gr}    ::::::`:::::;'  /  /   `#              
    ''')

def cycle():
    while True:
        try:
            input('... ')
            print(banner1)
            option = int(input(f'{wh}Enter option: '))
        except ValueError:
            print(f'{wh}You entered something else')
            continue

        if option == 1:
            print(banner2)
            number = input(f'{wh}Enter phone number (Format: {gr}+123456789000{wh}): ')
            parsed = num.parse(number)

            print(f"{wh}[{gr}+{wh}] {wh}[Valid] : {gr}{num.is_valid_number(parsed)}")
            print(f"{wh}[{gr}+{wh}] {wh}[Region] : {gr} {geocoder.description_for_number(parsed, "en")}")
            print(f'{wh}[{gr}+{wh}] {wh}[Carrier] : {gr}{carrier.name_for_number(parsed, "en")}')
            print(f"{wh}[{gr}+{wh}] {wh}[Time Zone] : {gr}{timezone.time_zones_for_number(parsed)}")
            print(f"{wh}[{gr}+{wh}] {wh}[Country code] : {gr}{parsed.country_code}")
            print(f"{wh}[{gr}+{wh}] {wh}[Original number] : {gr}{parsed.national_number}")
            print(f"{wh}[{gr}+{wh}] {wh}[Ratings] : {gr} https://www.shouldianswer.com/phone-number/{number}{wh},{gr} https://www.tellows.com/num/%2B{number}")

        elif option == 2:
            print(banner2)
            ip = input(f'{wh}Enter an IPv4 Adress: ')
            get_info_by_ip(ip)

        elif option == 3:
            webbrowser.open('https://grabify.link')
            print('')

        elif option == 4:
            print(banner2)
            query = input(f'{wh}[{gr}+{wh}] {wh}Enter what to search: ')
            results = int(input(f'{wh}[{gr}+{wh}] {wh}How many results: '))
            for result in search(query, num_results=results):
                print(f'{wh}[{gr}+{wh}] {result}')
            print('')

        elif option == 5:
            print(banner2)
            image_path = input(f'{wh}[{gr}+{wh}] {wh}Enter image path: ')
            extract_image_metadata(image_path)

        elif option == 0:
            exit()

        elif option == 6:
            print(banner2)
            username_check()

        else:
            print(f"{wh}[{gr}+{wh}] {wh}Invalid option\n")

cycle()
