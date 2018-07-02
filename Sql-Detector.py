import requests

targets = [] 

with open('lol.txt','r') as f:
    for line in f:
        url = str(line.replace('\n',''))
        targets.append(url)

for url in targets:
    if 'http://' in url:
        url = url.replace('http://', '')
    elif 'https://' in url:
        url = url.replace('https://', '')
    url = 'http://' + url

    response = requests.get(url + "'").text
    if 'error' in response and 'syntax' in response or 'MySQL' in response:
        print 'Gotcha!!! ' + url
    else:
        print 'No luck here :( ' + url