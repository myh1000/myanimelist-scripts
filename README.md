# myanimelist-scripts

some scripts for automated/mass adding to myanimelist.

## mangahere --> myanimelist
first go to mangahere bookmarks and save the html code by viewing source. save as ```1.html```, ```2.html```, etc.

open ```mangahere_title.py``` and edit the range for the number of html pages. Run.

now run ```mangahere.py```.

Install any missing modules
```
pip install "module"
```

The delay can be made shorter/longer if requests are going through/rejected.

If it can't find the manga, it'll open up the search of that manga in the browser. Edit the title in ```titles.txt``` or add "Added: " before that line:
```
Added: No Game No Life
```

## vlc --> myanimelist
wip

adds/updates anime mal that you've watched up to episode X

## open /r/anime
check [myh1000/reddit-vlc](https://github.com/myh1000/reddit-vlc)
