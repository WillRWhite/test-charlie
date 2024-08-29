import discord
from discord.ext import commands 
import json

bot = commands.Bot(command_prefix = "." , intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("CHAZZA IS HERE!")

with open("anime_titles.json", "r") as file:
    anime_titles = json.load(file)

with open("anime_details.json", "r") as file:
    anime_details = json.load(file)

anime_dict = {anime['title']: anime for anime in anime_details}

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello weeb, {ctx.author.mention}!")

@bot.command(name = "gm")
async def goodmorning(ctx):
    await ctx.send(f"morning weeb, {ctx.author.mention}!")

@bot.command()
async def sendembed(ctx):
    embeded_msg = discord.Embed(title = "title of embed", description = "description of embed", color = discord.Color.red())
    embeded_msg.set_author(name = "footer text" , icon_url = ctx.author.avatar)
    embeded_msg.set_thumbnail(url = ctx.author.avatar)
    embeded_msg.add_field(name = "name of field", value = "value of field", inline = False)
    embeded_msg.set_image(url = ctx.guild.icon)
    embeded_msg.set_footer(text = "footer text", icon_url = ctx.author.avatar)
    await ctx.send(embed = embeded_msg)

@bot.command(name="anime")
async def anime(ctx, *, query: str):
    if query in anime_dict:
        anime = anime_dict[query]
        response = (
            f"**Title**: {anime['title']}\n"
            f"**Rating**: {anime['rating']}\n"
            f"**Synopsis**: {anime['synopsis']}\n"
            f"**Similar Anime**: {', '.join(anime['similar_anime']) or 'None'}"
        )
        await ctx.send(response)
    else:
        await ctx.send("Anime not found.")


with open("token.txt") as file:
    token = file.read()

bot.run(token)

#embeded_msg.set_author(name = "footer text" , icon_url = ctx.author.avatar)







