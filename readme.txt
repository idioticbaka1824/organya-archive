This is a static archive, based on the first two folders in the Organya Master List (compiled by @rde on Discord). Hopefully this format makes it easier to search for, preview, and download orgs.
The Organya master list is at https://docs.google.com/spreadsheets/d/151dLFqDK-_UhSLz_0fOfvAvfcbgendqfZiwVZ26ZLnw/

song_index.js contains a list of dictionary objects that contain metadata regarding each org song contained in the SONGS folder. Its format is pretty much self-explanatory. This list was compiled using build_index.py, which traverses the directory, finds org files, and notes their name/author/etc. The author info as the script reads it hinges on the fact that the downloads from the master list are organised in folders by author name.
Whether or not the org in question is a cover/remix, and what the source is, comes from two csv files that are just two sheets downloaded from the Organya Master List. build_index.py reads these and incorporates that info when compiling the song_index. Then index.html just searches this metadata when you make a query and returns all matching songs, which you can then select.
If any source info needs updating I'd probably just manually add entries to the csv files and then run the python script again.
One thing not accounted for is when a song is original but still comes from some source game or series (because the composer also made that source material). This would need to be added by hand to song_index.js itself.

Enter text in the input areas above the table headers, and click Search to find orgs you want. Click on a row to select that org, then click the green play button to play. You can search under multiple columns at a time (this takes a logical intersection of the queries). Searching with nothing entered in any input area will return all 4000+ songs in the archive (this may take while).
Note that you can vertically resize the search results table as well as this whole text header section.

If you have feedback regarding this web tool, contact me anywhere listed in https://idioticbaka1824.github.io/contact.html
