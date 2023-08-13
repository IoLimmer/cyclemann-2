import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import responses
import asyncio
from utils import CALL_TIME, channel_temp_scarf
import GetHighestTemp


def run_discord_bot():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    specialboy = discord.Intents.default()  
    specialboy.message_content = True
    client = discord.Client(intents = specialboy)


    @tasks.loop(time = CALL_TIME) #Create the task
    async def getReading():
        channel = client.get_channel(channel_temp_scarf)
        await channel.send(GetHighestTemp.GetTempMinimum("bristol"))
        print("Getting readings from day")


    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        if not getReading.is_running():
            getReading.start() #If the task is not already running, start it.
            print("Readings task started")

   

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        response = responses.handle_response_2(message)
        if response[1] == "null":
            pass
        elif response[0]: # True = response message. False = emoji reaction
            await message.channel.send(response[1])
        else:
            await message.add_reaction(response[1])




    client.run(TOKEN)
