import requests

def GetHTTP(chatid):
    httpprx = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
    with open(f'{chatid}HTTP.txt', 'w') as file:
        file.write(httpprx.replace('\r', ''))

def GetSocks4(chatid):
    socks4prx = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
    with open(f'{chatid}SOCKS4.txt', 'w') as file:
        file.write(socks4prx.replace('\r', ''))

def GetHTTPS(chatid):
    httpsprx = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all').text
    with open(f'{chatid}HTTPS.txt', 'w') as file:
        file.write(httpsprx.replace('\r', ''))

