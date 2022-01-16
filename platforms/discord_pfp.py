import discord
import sys
from discord.ext.commands import Bot

#############################################################################################################################
# USAGE:                                                                                                                    #
# 0. Make sure you have python 3.5 + installed and have discord.py installed (pip3 install discord)                         #
# 1. Download the python file                                                                                               #
# 2. Change the token variable to hold your bots token and the pfp variable to hold the path to your desired pfp            #
# 3. Run your file using `python3 path/to/file.py                                                                           #
# 3. That's it, you can keep the file or delete it again!                                                                   #
#############################################################################################################################

client = discord.Client()

token = sys.argv[1]
password = sys.argv[2]
pfp_path = sys.argv[3]


@client.event
async def on_ready():
    with open(pfp_path, 'rb') as fp:
        await client.user.edit(avatar=fp.read(), password=password)
        await client.close()

client.run(token, bot=False)
