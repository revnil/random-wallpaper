#!/usr/bin/python3
import sys
import urllib.request
import requests
import subprocess

search = sys.argv[1]
url = "https://source.unsplash.com/1920x1080/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url,headers=headers,allow_redirects=True,params=search)
open('default.jpg','wb').write(r.content)

subprocess.Popen('/usr/bin/feh --bg-scale default.jpg', shell=True)
