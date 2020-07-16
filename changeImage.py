#!/usr/bin/env python3

import os, glob
from PIL import Image
size = 600, 400
for f in glob.glob(os.getcwd()+"/supplier-data/images/*"):
  try:
    im = Image.open(f).convert('RGB')
    print(f)
    print(im.format)
    new_name = os.path.basename(f)
    new_name = new_name.split('.')[0]
    print(new_name)
    im.resize((size)).save(os.getcwd()+"/supplier-data/images/{}.jpeg".format(new_name))
  except:
    continue

