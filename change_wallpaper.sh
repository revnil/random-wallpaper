#!/bin/bash

while test $# -gt 0; do
	case "$1" in
		-q|--search)
			shift
			if test $# -gt 0; then
				export SEARCH=$1
			else
				echo "no search string specified"
				exit 1
			fi
			shift
			;;
		*)
			break
			;;
	esac
done

wget https://source.unsplash.com/1920x1080/?"$SEARCH" > /dev/null 2>&1
mv ./index.html\?"$SEARCH" randompaper.jpg
feh --bg-scale randompaper.jpg

