#! /usr/bin/python3

import os
from PIL import Image

for infile in os.listdir("images"):
    f, _ = os.path.splitext(infile)
    outfile = "/opt/icons/" + f + ".jpg"
    if infile != outfile:
        try:
            with Image.open("images/" + infile) as im:
                im.convert("L")
                im.resize((128, 128))
                im.rotate(90)
                im.save(outfile)
        except OSError as e:
            print("cannot convert", "images/" + infile, e)
