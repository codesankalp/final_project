#!/usr/bin/env python3
import requests
import os, glob
from PIL import Image

url = "http://localhost/upload/"

for f in glob.glob(os.getcwd()+"/supplier-data/images/*.jpeg"):


	with open(f,'rb') as opened:
		r = requests.post(url, files={'file':opened})
