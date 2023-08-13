# Io's temperature blanket number scraper

<img src="https://64.media.tumblr.com/1625e221d4b2b958e7bb33ba471730f6/d091ab06cc06b2d1-3f/s75x75_c1/9e3f34e5e3cb21d11c48e583633097737fb06ea2.gif" width="50px" align="center">

## The problem
Temperature blankets are a popular craft activity for many crochet/knit enthusiasts. They involve, across one year, creating a blanket/scarf where each row represents a day of the year. That row has a certain colour, which corresponds with a certain temperature range. 365 rows later, and you have a blanket (or scarf) which shows the change in temperatures across one year. (AKA you'll probably end up with a nice rainbow gradient going from blue in January to red in July and then back to blue again in December, although the colour range used is of course down to personal preference)

The problem, however, is this: pulling raw data every single day can be a nuisance. It only makes sense to automate it.


## The objective
This project describes a Discord bot, written in Python, that will, for every day of a year:
- Automatically pull the maximum recorded temperature from the previous 24 hours for a given area
- Compare that value with user defined colour brackets
- List maximum value and colour in a selected channel on your Discord server for later access


## How?
This project uses MetOffer, a Python module that pulls data from the MetOffice website. (Meaning the project is currently limited to the UK - this may change if anyone but me wants to use this bot!)


## Notes on the current build
The bot can currently only pull data from two observation stations outside of Burnley (my hometown) and Bristol (my uni town). This is because I am the only soul who uses this bot.

The bot is currently automated to record the highest temperature for the day in Bristol from the last 24 hours at half midnight every day. I will make this customisable in the future.

The bot currently has three commands:
- `!temp <location>`
  - Gets the maximum temperature recording from the last 24 hours for `<location>` with corresponding colour
  - Returns data in this format:
```
Location: Bristol
Recorded on 21/1 at 2pm
The highest temperature recorded was 5.0°C
Colour of row is DENIM, colour number 3
```
- `!temp mini <location>`
  - Gets the maximum temperature recording from the last 24 hours for `<location>` with corresponding colour
  - Returns data in this format:
```
18/3 - FRUITS
```
- `!temp all <location>`
  - Gets all temperature recordings from last 24 hours for `<location>` along with times they were recorded at and corresponding colour
  - Returns data in this format:
```
Temperatures recorded in Bristol from 21/1, 10am to 22/1, 9am
21/1, 10am | -2.4°C | NAVY,
21/1, 11am |  0.0°C | NAVY,
21/1, 12am |  2.2°C | BABYNAVY,
21/1, 1pm  |  5.0°C | DENIM,
21/1, 2pm  |  5.0°C | DENIM,
21/1, 3pm  |  4.8°C | DENIM,
21/1, 4pm  |  3.4°C | BABYNAVY... etc
``` 

<img src="https://64.media.tumblr.com/1625e221d4b2b958e7bb33ba471730f6/d091ab06cc06b2d1-3f/s75x75_c1/9e3f34e5e3cb21d11c48e583633097737fb06ea2.gif" width="50px" align="center">
