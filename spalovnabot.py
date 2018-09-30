#how did u get dis file

import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import os
import random

bot = commands.Bot(command_prefix="!")

#Events

@bot.event
async def on_ready():
	await bot.change_presence(game=Game(name="Zeman x Ovčáček"))
	print ("Starting this shit. V2")
	print ("user.name: " + bot.user.name)
	print ("user.id: " + bot.user.id)
	print ("directory is: " + os.getcwd())
	print ("--------------------------------------")
	print ("bot made by: bitran")
	
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if "jerusalem" in message.content.lower():
		await bot.send_message(message.channel, "<:holy:495684177480646656> " + message.author.mention)
	else:
		if "babiš" in message.content.lower():
			await bot.send_message(message.channel, "**Čapí Hnízdo Intensifies**")
		else:
			if "deus vult" in message.content.lower():
				await bot.send_message(message.channel, "<:holy:495684177480646656> " + message.author.mention)
			else:
				if "spd" in message.content.lower():
					await bot.send_message(message.channel, "*Úsvit příme demokracie, Tomio Okamury!* <:Tomio:495688510318182400>")
				else:
					if "sjw" in message.content.lower():
						await bot.send_message(message.channel, ":flag_us: Social Justice POWER! :flag_us:")
		
@bot.command(pass_context = True)
async def info(ctx, target: discord.Member = None):
	if target is None:
		target = ctx.message.author
		await bot.say("Zobrazuji info o: *{}*".format(target))
		await bot.say("Discord ID: *{}*".format(target.id))
		await bot.say("Nejvyšší role: *{}*".format(target.top_role))
		await bot.say("Datum připojení na server: *{}*".format(target.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")))
		print ("!info given")
	else:
		await bot.say("Zobrazuji info o: *{}*".format(target))
		await bot.say("Discord ID: *{}*".format(target.id))
		await bot.say("Nejvyšší role: *{}*".format(target.top_role))
		await bot.say("Datum připojení na server: *{}*".format(target.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")))
		print ("!info given")
		
@bot.command(pass_context = True)
async def roll(ctx):
		await bot.say(random.randint(1,100))
		
@bot.command(pass_context = True)
async def holy(ctx):
		await bot.say("<:holy:495684177480646656>")
		
bot.run(os.getenv('TOKEN'))
