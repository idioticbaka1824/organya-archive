import json
import os
import datetime
data=[]

directory = 'SONGS'
for roots, dirs, files in os.walk(directory):  
    for file in files:
        print(roots, dirs, file)
        root_slash = roots.replace('\\', '/')
        author = root_slash[6:]
        data.append({
            "filename": file,
            "path": root_slash,
            "title": "",
            "author": author,
            "source song": "",
            "date uploaded": "",
            "date created": datetime.datetime.fromtimestamp(os.stat(os.path.join(roots,file)).st_ctime).isoformat(),
            "comments": "",
            "tags": []
        })

with open("song-index.json", "w") as f:
    f.write(json.dumps(data, indent=2))