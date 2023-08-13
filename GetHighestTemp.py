import metoffer
import pprint
from datetime import datetime
import enum
from math import floor
from decimal import Decimal, ROUND_HALF_UP


# NAVY, BABYNAVY, DENIM, NEON, FRUITS, CERISE, CUPID, PINK, ORANGE, PUMPKIN, LEMON = range(11)
colourBracket = 4
lowestTemp = 1
highestTemp = 36

class Colour(enum.Enum):
    NAVY = 0
    BABYNAVY = 1
    DENIM = 2
    NEON = 3
    FRUITS = 4
    CERISE = 5
    CUPID = 6
    PINK = 7
    ORANGE = 8
    PUMPKIN = 9
    LEMON = 10


def getColour(max_value):
    x = Decimal(max_value).to_integral_value(rounding=ROUND_HALF_UP)
    index = floor(((x - 1) / colourBracket) + 1)
    # bound value of index
    if index < 0:
        index = 0
    elif index > 10:
        index = 10

    return index


def ReformatTime(datetime, hourOrDay):
    time = str(datetime.time())
    date = str(datetime.date())

    hour = int(time[:2])
    minute = time[3:5]
    second = time[6:8] 

    year = str(int(date[:4]))
    month = str(int(date[5:7]))
    day = str(int(date[8:10]))

    daymonth = day + "/" + month  
    if hour > 12:
        hour = hour - 12
        hour = str(hour) + "pm"
    elif hour == 0:
        hour = "12am"
    else:
        hour = str(hour) + "am"

    #######
    if hourOrDay == "day":
        return daymonth

    elif hourOrDay == "time": # hour is default
        return hour

    else: # both is default
        both = daymonth + ", " + hour
        return both



def rawDataGetter(location):
    M = metoffer.MetOffer(API_KEY)
    if location == "bristol":
        x = M.nearest_loc_obs(51.455911, -2.588890) # YEOVILTON (Bristol 1)
    else: # burnley is the default
        x = M.nearest_loc_obs(53.790032, -2.242613) # STONYHURST (Burnley 1)
        location = "burnley"
    y = metoffer.Weather(x)

    min_value = 100
    min_time = 0
    max_value = -50
    max_time = 0
    curr_val = 0
    tally = 0
    counter = 0

    all_temps = ""

    for i in range(24):
        counter = counter + 1
        curr_val = (y.data[i]["Temperature"][0])
        curr_time = y.data[i]["timestamp"][0]

        tally = tally + curr_val

        if curr_val >= max_value:
            max_value = curr_val
            max_time = curr_time

        if curr_val <= min_value:
            min_value = curr_val
            mix_time = curr_time

        # all temperatures log
        colourIndex = getColour(max_value)
        all_temps = all_temps + str(ReformatTime(curr_time, " ")) + " | " + str(curr_val) + "°C | " + Colour(getColour(curr_val)).name
        if i == 23:
            all_temps = all_temps + "\n"
        else:
            all_temps = all_temps + ",\n"
        ############################

    data = [location, y, counter, max_time, max_value, colourIndex, all_temps]
    return data



def GetTempMinimum(location) -> str: 
    data = rawDataGetter(location)

    max_time = data[3] 
    colourIndex = data[5]

    return str(ReformatTime(max_time, "day") + " - " + Colour(colourIndex).name)



def GetTemp(location, all) -> str:
    data = rawDataGetter(location)

    location = data[0]
    y = data[1]
    counter = data[2]
    max_time = data[3]
    max_value = data[4]    
    colourIndex = data[5]
    all_temps = data[6]

    if all:
        output = str("Temperatures recorded in " + location.title() + 
        " from " + ReformatTime(y.data[0]["timestamp"][0], " ") +
        " to " + ReformatTime(y.data[counter-1]["timestamp"][0], " ") + "```\n" +
        all_temps + "```")

    else:
        colourIndex = getColour(max_value)
        output = str("Location: " + location.title() + 
        "\nRecorded on " + ReformatTime(max_time, "day") + " at " + ReformatTime(max_time, "time") + 
        "\nThe highest temperature recorded was " + str(max_value) + "°C" + 
        "\nColour of row is "+ Colour(colourIndex).name + ", colour number " + str(colourIndex + 1))

        # Location: Bristol
        # Recorded on 19/3 at 12am
        # The highest temperature recorded was 12.9°C
        # Colour of row is FRUITS, colour number 5

    return output


def getColourSquare():
    return "test!"
