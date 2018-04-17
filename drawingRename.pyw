import os.path
from shutil import move
from builtins import str

outPath = ("") # path to final folder
tempPath = (outPath + "") # path to temp final
output = (outPath + "\\Renamer\\output.txt")

rename = []
release = []
for path, subdir, files in os.walk(tempPath):
    for filename in files:
        f = os.path.join(str(filename))
        if "_" in f and "-" in f and ".txt" in f.lower():
            release.append(f)
        else:
            rename.append(f)

for f in rename:
    if "pre" in f.lower():
        rev = "PRELIMINARY"
    else:
        rev = f.split('.')[0]
        rev = list(rev)
        rev = rev[int(len(rev)-1)]
    pn = list(f.split('.')[0])
    pn = ''.join(pn[:-1])
    pn = (pn + "_" + rev + ".pdf")
    oldPn = (tempPath + "\\" + f)
    sourcePath = (tempPath + "\\" + pn)
    release.append(pn)
    os.rename(oldPn, sourcePath)
    
for f in release:
    destination = (outPath + "\\" + f)
    move(sourcePath, destination)