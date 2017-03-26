## WeCycle

Got a puncture on your bike?

WeCycle is a community of cyclists to find help when they need it the most. 

### Features

- Find the nearest bike shops to user location

- Broadcast a message, asking nearby cyclists for help when bike shops are closed

- Allow users to report problems they find on their commute (road closures, etc)

### DETAILS

A REST api was developed using Python Flask, Materialize CSS and Google Maps API. Here is where the relevant stuff is:

```
|- app 
  |- \__init\__.py (Contains all relevant routes)
  |- models.py (model a bikeShop to database)
  |- templates/ (Webpages)
    |- Index.html (main page)
  |- static/ (CSS and javascript libraries)
|- data (Data :D )
|- ~~HackCity2~~ (This folder contains some mock HTML/CSS files, not really used in the app)
```
