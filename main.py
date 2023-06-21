import sys

from mod_loader import download_mod


if len(sys.argv) == 1:
    url = input("enter the url of the mod profile: ")
elif len(sys.argv) == 2:
    url = sys.argv[1]

download_mod(url)
