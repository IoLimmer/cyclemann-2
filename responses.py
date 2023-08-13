import random
import GetHighestTemp
import os
from utils import *


locations = ["bristol", "burnley"]



def write_to_txt(server, channel, location):

    writelist = [server.id, channel.id, location]

    with open(TXT_FILE, "r") as input:
        with open("temp.txt", "w") as output:
            for line in input:
                # print(line[1:19])
                # print(server.id)
                # if int(line[1:19]) == int(server.id):
                if line.strip("\n") != str(server.id):
                    print("banana")
                    output.write(line)

def handle_response_2(message):
    author = message.author
    channel = message.channel
    server = message.guild

    msg = message.content.lower()

    
    # temperature response handler


    if msg[:5] == "!temp":

        # check call time
        if msg == "!temp time":
            response = str("The current call time for weather data is " + str(CALL_TIME))
            return True, response
        
        # get html colour codes 
        if msg == "!temp colours":
            return True, (GetHighestTemp.getColourSquare())

        # set channel
        if msg[:12] == "!temp config": #IN CHOSEN CHANNEL
            if msg[13:] in locations:
                write_to_txt(server, channel, msg[13:])
                return True, str("Channel has been configured! You selected channel `"+str(channel)+"` and your location is `"+msg[13:]+"`")
            else: #default to burnley
                write_to_txt(server, channel, "burnley")
                return True, str("Channel has been configured! You selected channel `"+str(channel)+"` and your location is `burnley`")


        elif msg[:9] == "!temp all":
            if msg[10:] in locations:
                return True, (GetHighestTemp.GetTemp(msg[10:], all = True))
            else:                
                return True, (GetHighestTemp.GetTemp("burnley", all = True))
            

        elif msg[:10] == "!temp mini":
            if msg[11:] in locations:
                return True, (GetHighestTemp.GetTempMinimum(msg[11:]))
            else:                
                return True, (GetHighestTemp.GetTempMinimum("burnley"))

            
        elif msg[6:] in locations: #"!temp burnley" or "!temp bristol"
            return True, (GetHighestTemp.GetTemp(msg[6:], all = False))
        else:
            return True, (GetHighestTemp.GetTemp("burnley", all = False))
        

    ####################

    if msg[:5] == "!roll":
        if msg[6:].isdigit():
            return True, str(random.randint(1, int(msg[6:])))
        else:
            return True, str(random.randint(1, 6))

    if msg == "!test":
        return True, "hello!"
       
    if makeRegex("blue").search(msg):
        return True, bloo
   
    if makeRegex(cyclemann).search(msg):
        return False, bike

    else: 
        return False, "null"
