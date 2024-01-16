#!/opt/homebrew/bin/python3

import subprocess
import os

template = open('cv.tex').read()
fonts = [font.strip() for font in open('ro.txt').readlines()]

os.chdir('output')
for font in fonts:
  s = template.replace("__FONT__", font)
  tex = f'{font}.tex'
  with open(tex, 'w') as out:
    out.write(s)
  command = ["lualatex", tex]

  print(command)
  output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  print(output.stdout)
  os.remove(f'{font}.log')
  os.remove(f'{font}.aux')
  os.remove(f'{font}.out')
  os.remove(tex)