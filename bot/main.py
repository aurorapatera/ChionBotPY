import os
from discord.ext import commands
import random
import discord

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

pit_words = [
    "buttplug", "dildo", "titties", "titty", "pit", "porn", "dong",
    "hand holding", "peen", "boob", "dick", "salami", "wizard tower",
    "Biggus Dickus", "bite me", "eggplant", "peepee", "sword of the frontier",
    "vlaakith", "shar preserve me", "horny", "Haedir"
]

prompts_list = [
    "a cuddle", "a campfire", "the fireplace", "the Elf Song", "a meet cute"
]

vibes_list = [
    "a fluffy", "an angsty", "a smutty", "a hurt/comfort",
    "a fluffy and smutty"
]

characters_list = ["Astarion", "Gale", "Lae'zel", "Shadowheart", "Wyll"]

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    #If one of the pit words is mentioned, send them to the pit
    if any(word in msg for word in pit_words):
        await message.channel.send('<:pit:831859849343401998>')

    #If asked for prompt gives an idea from the lists

    if "prompts" in db.keys():
        options = options + db["prompts"]

    if msg.startswith("$add"):
        prompts_list = msg.split("$add ", 1)[1]
        update_prompts(prompts_list)
        await message.channel.send("New prompt added.")

    if msg.startswith("$del"):
        prompts = []
        if "prompts" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragment(index)
            prompts = db["prompts"]
        await message.channel.send(prompts)

    if msg.startswith("$prompt"):
        await message.channel.send('Tell me ' + random.choice(vibes_list) +
                                   ' story about ' +
                                   random.choice(characters_list) + ' and ' +
                                   random.choice(prompts_list))

if __name__ == "__main__":
    bot.run(TOKEN)
