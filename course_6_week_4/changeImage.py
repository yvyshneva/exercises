#!/usr/bin/env python3

import os
from PIL import Image

images_dir = "supplier-data/images/"

for infile in os.listdir(images_dir):
    f, ext = os.path.splitext(infile)
    if ext.lower() != ".tiff":
      continue

    outfile = images_dir + f + ".jpeg"
    if infile != outfile:
        try:
            with Image.open(images_dir + infile) as im:
                im = im.convert("RGB")
                im = im.resize((600,400))
                im.save(outfile)
        except OSError as e:
            print("cannot convert", images_dir + infile, e)
