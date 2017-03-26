## WeCycle

WeCycle is an app designed to bring the London cycling community closer
By being able to find help or assist other cyclists when they most needed.

### Features

-  A google map which shows your location and the location of the nearest Cycle shops for the event of a puncture, pumping some air on your wheels, etc…

- Alternatively, one can broadcast a help message to other cyclists nearby that are using the app so that  they can assist when other means are difficult, for instance when cycle shops are closed,

- A means to flag road issues on the Google map for other cyclist to check, for instance, broken glass on the road, an accident, road works, bumps, etc….

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
### IMAGES

Find nearest bike shops

![](index.png?raw=true)

Ask other users for help

![](people_around.png?raw=true)

Menu

![](menu.png?raw=true)
