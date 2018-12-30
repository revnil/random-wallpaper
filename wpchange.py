#!/usr/bin/python3
import sys
import requests
import subprocess
import argparse


def change_wallpaper():

  parser = argparse.ArgumentParser(description="Changes the wallpaper.")
  parser.add_argument("-s", "--search", help="search for random wallpaper based on your input.")
  args = parser.parse_args()

  if args.search:
    #search = sys.argv[1]
    search = sys.argv[1]
    url = "https://source.unsplash.com/1920x1080/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get(url,headers=headers,allow_redirects=True,params=search)
    open('default.jpg','wb').write(r.content)

    subprocess.Popen('/usr/bin/feh --bg-scale default.jpg', shell=True)
  else
    exit(1)

if __name__ == '__main__':
    change_wallpaper()