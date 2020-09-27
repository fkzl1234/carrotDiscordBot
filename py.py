import discord
import datetime


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("토끼봇 명령어")
    await client.change_presence(status=discord.Status.online,activity=game)







@client.event
async def on_message(message):



    if message.content.startswith("토끼봇 명령어"):
        await message.channel.send(">>> 토끼네 유튜브 : 토끼네 유튜브를 보여준다.\n토끼 봇 내정보:내 정보를 보여준다.(토끼봇 내아이디:내 아이디만 보여준다)\n토끼봇 DM 상대방의아이디 하고싶은말")






    if message.content.startswith("토끼님 유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("토끼유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("토끼 유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("토끼님유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("김토끼님 유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("김토끼유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("김토끼 유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("김토끼님유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("김토끼네 유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("김토끼네유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("토끼네 유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("토끼네유튜브"):
        await message.channel.send("https://www.youtube.com/channel/UCrPomivQeqhOTZKGuP75MQQ")
    if message.content.startswith("토끼 봇 내정보"):





        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) +1420070300000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("토끼봇내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) +1420070300000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("토끼봇 내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) +1420070300000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("토끼봇 내 정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) +1420070300000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith("토끼봇 DM"):
        author = message.guild.get_member(int(message.content[7:25]))
        msg = message.content[26:]
        await author.send(msg)
    if message.content.startswith("토끼봇 내 아이디"):
        await message.channel.send(message.author.id)
    if message.content.startswith("토끼 봇 내아이디"):
        await message.channel.send(message.author.id)
    if message.content.startswith("토끼봇 내아이디"):
        await message.channel.send(message.author.id)
    if message.content.startswith("토끼 봇 내 아이디"):
        await message.channel.send(message.author.id)
    if message.content.startswith("토끼봇내아이디"):
        await message.channel.send(message.author.id)




















client.run("NzU5MjQ2MTUwMzAxMjUzNjMy.X26tFA.NmvUwCHd1UmZ_fqea_hSWadC_Ug")