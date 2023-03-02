import discord
import logging
import random


# Logging to make my life not hell, should probably change to log to a text document
logging.basicConfig(level=logging.INFO)
client = discord.Client()

numbers = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
# Informs when bot has logged in
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(roll):
    numtorollencoded = []
    decodednumroll = []
    maxencoded = []
    maximumreal = 0
    numreal = 0
    if roll.content.startswith("🎰"):
        callremoved = roll.content.replace("🎰", "")
        num, maximum = callremoved.split("🅱")
        numtoroll = [x for x in num]
        for x in numtoroll:
            try:
                decodednumroll.append(int(x))
            except:
                pass
        maximum = [x for x in maximum]
        for x in maximum:
            try:
                maxencoded.append(int(x))
            except:
                pass
        for x in maxencoded:
            maximumreal = int(str(maximumreal) + str(x))
        for x in decodednumroll:
            numreal = int(str(numreal) + str(x))
        rolls = [random.randint(1, int(maximumreal)) for x in range(int(numreal))]
        total = str(sum(rolls))
        total = [int(x) for x in str(total)]
        output = []
        for x in total:
            output.append(numbers[int(x)])
        await roll.channel.send("".join(output))


# Runs bot
key = input("Input Bot Key:")
client.run(key)
