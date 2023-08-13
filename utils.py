import re 
from datetime import *
from GetHighestTemp import ReformatTime


CALL_TIME = time(hour=0, minute=30, second=0)

if CALL_TIME.hour > 12:
    callTimeNice = CALL_TIME.hour - 12
    callTimeNice = str(callTimeNice) + "pm"
elif CALL_TIME.hour == 0:
    callTimeNice = "12am"
else:
    callTimeNice = str(CALL_TIME.hour) + "am"

    

TXT_FILE= "channel.txt"


cyclemann = ["cyclemann", "cycle mann", "cycleman", "cycle man", "Archbishop of Banterbury", "archbishop"]

scotland = "🏴󠁧󠁢󠁳󠁣󠁴󠁿"
gaypride = "🏳️‍🌈"
bike = "🚲"

bloo = "https://tenor.com/view/boris-johnson-blue-passport-gif-25621012"


# regex code by ci-w (isla).

# makes the little regex pattern for a sequence of words that you want to match ALL of
# helper function not meant to be used on its own. Io on god do not use this function on its own. 
def regexAnd(words: str):
    words = words.split()
    re_lst = '\\s*'.join('({0})'.format(word) for word in words)
    return re_lst 

# example inputs for makeRegex:
# "i want to match all of these words"
# ["i", "want", "to", "match", "any", "of", "these", "strings"]
# ["i want to match every word in this string", "or every word in this string"]

#"words" can either be a string or a list of strings
# the created regex ignores both spacing and case
def makeRegex(words):
    #if its just a string, put it into a LIST
    if isinstance(words,str):
        words = [words]
    # make baby regex's for sequences of words
    words = [regexAnd(word) if len(word.split())>1 else word for word in words]
    # make regex of all those regex's OR'd together 
    re_lst = '|'.join('({0})'.format(word) for word in words)
    return re.compile(r'\b{0}\b'.format(re_lst), flags=re.IGNORECASE)

# thinking about cat emojis:
# .findall(), remove empty strings, iterate through them