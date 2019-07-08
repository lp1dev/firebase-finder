#!python3

from sys import argv
import requests

DB_URL="https://%s.firebaseio.com/.json"

with open(argv[1]) as f:
    names = f.readlines()    
    for name in names:
        name = name.replace('\n', '').replace(' ', '%20')
        r = None
        try:
            r = requests.get(DB_URL %name)
        except requests.exceptions.ConnectionError as e:
            continue
        if r.status_code == 200:
            print("%s: found and fetched data %s" %((DB_URL %name), r.text))
        elif r.status_code == 404 or r.status_code == 400:
            print('%s: unknown database' %name)
        elif r.status_code == 403:
            print('%s: unknown database' %name)
        elif r.status_code == 401:
            print('%s: database found but unreadable' %(DB_URL %name))
        else:
            print(r.text)
            print(r.status_code)
            print('%s: database doesn\'t seem to be readable' %name)
