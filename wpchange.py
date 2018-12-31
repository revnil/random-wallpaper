#!/usr/bin/python3
import os
import sys
import requests
import subprocess
import argparse
import time


def change_wallpaper():

    parser = argparse.ArgumentParser(description="Changes the wallpaper.")
    parser.add_argument("-s", "--search", help="search for random wallpaper based on your input.")
    args = parser.parse_args()
    timestr = time.strftime("%Y%m%d-%H%M%S")

    os.chdir(os.path.dirname(__file__))
    if args.search:
        search = sys.argv[2]
        url = "https://source.unsplash.com/1920x1080/"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(url, headers=headers, allow_redirects=True, params=search)

        # Replace empty spaces with hyphens, convert filename to lowercase, and add a timestamp to the filename
        filename = search.replace(' ', '-').lower() + '-' + timestr + '.jpg'
        open(filename, 'wb').write(r.content)

        # Change the wallpaper with feh
        subprocess.Popen('/usr/bin/feh --bg-scale ' + filename, shell=True)
    else:
        parser.print_help()
        exit(1)


if __name__ == '__main__':
    change_wallpaper()
