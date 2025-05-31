import json
import os
import datetime
import csv

directory = 'SONGS/'

originals_csv = []
with open(directory+'ORGanized List - Originals (Confirmed).csv') as f:
    csvfile = csv.DictReader(f)
    for line in csvfile:
        originals_csv.append(line)

covers_csv = []
with open(directory+'ORGanized List - Identified Covers.csv') as f:
    csvfile = csv.DictReader(f)
    for line in csvfile:
        covers_csv.append(line)

data=[]
for roots, dirs, files in os.walk(directory):  
    for file in files:
        if file[-4:]=='.org':
            root_slash = roots.replace('\\', '/')
            try:
                author = root_slash[6:6+root_slash[6:].index('/')]
            except ValueError:
                author = root_slash[6:]
            isCover = 2
            if len([element for element in originals_csv if element['ORGMaker']==author and element['Filename']==file]) != 0: #check if this author and filename exists in the originals(confirmed) list
                isCover = 0
            cover_info = [element for element in covers_csv if element['ORGmaker']==author and element['Filename']==file]
            source = ""
            source_song = ""
            if len(cover_info) != 0:
                source = cover_info[0]['Source'] #assuming only one match exists
                source_song = cover_info[0]['Song']
                isCover = 1
            data.append({
                "filename": file,
                "path": root_slash,
                # "title": "",
                "author": author,
                "source": source,
                "source song": source_song,
                "isCover": isCover, #0=original, 1=cover/remix, 2=unsure
                # "date uploaded": "",
                "date created": datetime.datetime.fromtimestamp(min(os.stat(os.path.join(roots,file)).st_ctime, os.stat(os.path.join(roots,file)).st_mtime)).isoformat(),
                # "comments": "",
                # "tags": []
            })

to_write = 'let song_index = ' + json.dumps(data, indent=2)
with open("song_index.js", "w") as f:
    f.write(to_write)