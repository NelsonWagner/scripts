import os, emailer
from collections import Counter

drive1 = "" # Enter paths for the two drives you'll be scanning
drive2 = ""
output = "" # Paths for script to dump text files
outputPath = "" # Path for text file that has full file paths
duplicates = 0
drive1ListRaw = []
drive2ListRaw = []
fileList = []

class File():
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
        self.filePath = self.path + "\\" + self.filename
        self.list = self.filename.split('.')
        self.list = list(reversed(self.list))
        self.extension = self.list[0]

for dir, subdir, files, in os.walk(drive2):
    for file in files:
        if not '' in file.lower() and not '' in file and '' in file.lower() and not '' in dir.lower(): # Insert conditions to filter unwanted files
            drive2ListRaw.append(file)
            temp = {'filename': file, 'path': dir}
            fileList.append(temp)
            
for dir, subdir, files, in os.walk(drive1):
    for file in files:
        if not '' in dir.lower() and not '' in dir.lower() and not '' in dir.lower() and not '' in dir.lower(): # Insert conditions to filter unwanted files
            if '' in file.lower():
                drive1ListRaw.append(file)
                temp = {'filename': file, 'path': dir}
                fileList.append(temp)

dupeRaw = drive1ListRaw + drive2ListRaw
dupeList = [k for k,v in Counter(dupeRaw).items() if v>1]
duplicatePath = []
for d in dupeList:
    for f in fileList:
        if d == f['filename']:
            duplicatePath.append(File(f['filename'], f['path']))

a = open(output, "w+")
for file in dupeList:
    a.write("%s\n" % file.upper())
a.close()

b = open(outputPath, "w+")
for file in duplicatePath:
    b.write("%s\n" % file.filePath.upper())
b.close()

attachment = [output, outputPath] # Attachments to hand the emailer

print("Files Written to Output")

message = ("") # message to be sent in HTML
emailer(message, "Duplicate Files", "", attachment, 'yes') # insert any email addresses separated by ';'

os.remove(output)
os.remove(outputPath)