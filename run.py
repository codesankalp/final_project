#! /usr/bin/env python3
import os
import requests
import glob
url = "http://35.224.8.35/fruits/"

for f in glob.glob(os.getcwd()+"/supplier-data/descriptions/*.txt"):
        ls = []
        for line in open(f):
                line = line.strip()
                ls.append(line)
        image = ((f.split('/')[-1]).split('.'))[0] + '.jpeg'
        print(image)


        content = {"name": ls[0], "weight": int((ls[1].split())[0]), "description":ls[2], "image_name":image}
        print(content)
        r = requests.post(url, data=content)




