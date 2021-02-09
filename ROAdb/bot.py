import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(bot.latency * 1000)} ms')

@bot.command(aliases=['小幫手','指令','HELP'])
async def Help(ctx):
    await ctx.send(f'支援指令---- 前面要加[.]: 支語警察,01p,收人,強化,挖礦,釣魚,貨幣,OX,經驗表,賦魔,魔物')

@bot.command(aliases=['支語警察'])
async def _8ball(ctx):
    li = ['屏幕', '菜單' ,'硬件' ,'高清' ,'內存' ,'視頻' ,'信息' ,'優化',
          'U1S1 小夥伴們 把牛逼打在公屏上','酸奶','得勒','默認' ,'老鐵' ,'激活', '緩存'
          '水平', '質量', '小姐姐' ,'打個滴'
          ]
    await ctx.send(f'一日一支語 :{random.choice(li)}')

@bot.command(aliases=['01p'])
async def _01p(ctx):
    await ctx.send(f'https://media1.tenor.com/images/ce441e4f0e6f115e9eb1b321955c1b80/tenor.gif?itemid=5094560')
@bot.command(aliases=['強化'])
async def qiangHua(ctx):
    await ctx.send(f'https://i.ibb.co/K08t7W4/S-17408144.jpg')
@bot.command(aliases=['釣魚'])
async def Fishing(ctx):
    await ctx.send(f'https://i.ibb.co/BwWCpdd/image.jpg')
@bot.command(aliases=['貨幣'])
async def Coin(ctx):
    await ctx.send(f'https://upload.cc/i1/2020/11/06/rwVDPz.png')
@bot.command(aliases=['挖礦'])
async def Mining(ctx):
    await ctx.send(f'https://upload.cc/i1/2020/11/06/SjECxm.jpg')
@bot.command(aliases=['OX','ox'])
async def OXQuestion(ctx):
    await ctx.send(f'http://www.rbtips.com/2020/06/rox-ox.html')
@bot.command(aliases=['經驗表'])
async def ExpTable(ctx):
    await ctx.send(f'https://forum.gamer.com.tw/C.php?bsn=37030&snA=2036')
@bot.command(aliases=['賦魔'])
async def FuMo(ctx):
    await ctx.send(f'https://truth.bahamut.com.tw/s01/202010/84efab434508840118aeede9379ee3c3.JPG')

@bot.command(aliases=['收人'])
async def GoungHuai(ctx):
    li=['虎尾幫公會收人 有discord 有自己寫BOT可以幫助新手 幫解任務 雲林人++++','虎尾幫公會收人 現在進 會長下個月發股利= = 歡迎虎尾人跳槽',
        '虎尾幫公會收人 幫助新手排憂解難 有discord 寫了超過十幾種圖表查詢、指令 妹子++++ ']
    await ctx.send(f'{random.choice(li)}')

@bot.command(aliases=['魔物'])
async def MOWU(ctx):
    await ctx.send(f'http://www.roxng.com/monsterList')

@bot.command(aliases=['妹子'])
async def MeiZi(ctx):
    await ctx.send(f'https://i3.17173cdn.com/2fhnvk/YWxqaGBf/cms3/QTlusEblijjjzxy.png!a-3-480x.png')

@bot.command(aliases=['冷卻'])
async def Cd(ctx):
    await ctx.send(f'https://upload.cc/i1/2020/11/07/8XYhOK.jpg')


@bot.command(aliases=['冶煉'])
async def YeLian(ctx,*,question):
    result = "連字都打不對還想衝裝？"
    item = question.split(' ')[0]
    number = int(question.split(' ')[1])

    if item =='大神':
        result = f"需要{8 * number}個 【神之金屬礦石LV1】 和 {5 * number}個 【煤礦石LV1】"
    elif item =='魔力':
        result = f"需要{8 * number}個 【魔力之石礦石LV1】 和 {5 * number}個 【煤礦石LV1】"
    elif item =='鋁':
        result = f"需要{8 * number}個 【鋁礦石LV1】 和 {5 * number}個 【煤礦石LV1】"
    elif item =='金屬II':
        result = f"需要{9 * number}個 【強化金屬LV2】 ({9 * number*2}個強化LV1.) 和 {2 * number}個 【燼魚】"

    await ctx.send(f'{result}')

@bot.command(aliases=['耗材'])
async def Current(ctx,*,question):
    result = "連字都打不對還想衝裝？"
    item = question.split(' ')[0]
    current_level = int(question.split(' ')[1])

   #0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    if current_level <16 :
        pass
    elif 16 < current_level <26:
        result = f'當前{current_level}階 to 到25階需要---- 6個強化飾品LV2'


    if item == '飾品':
        pass

    # if item =='飾品':
        # result = f"需要{8 * number}個 【神之金屬礦石LV1】 和 {5 * number}個 【煤礦石LV1】"

    await ctx.send(f'{result}')


# @bot.command()
# async def clear(ctx,amount=5):
#     await ctx.channel.purge(limit=amount)

bot.run('Nzc0MTU4Njg5MjYzMDI2MjA2.X6Ttdg.IJz7C4P-c6sKtEBe6QVFIA9Bfp4')