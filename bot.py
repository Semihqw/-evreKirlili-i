import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')

@bot.command()
async def hakkında(ctx):
    bilgi = (
        "Çevre kirliliği, hava, su ve toprak gibi doğal bileşenlerin zararlı maddelerle bozulmasıdır. "
        "Bu zararlı maddeler genellikle insan faaliyetleri sonucu ortaya çıkar ve doğal çevreye, canlılara ve insan sağlığına zarar verebilir. "
        "Kirlilik türleri: hava kirliliği, su kirliliği, toprak kirliliği, gürültü kirliliği ve ışık kirliliğidir."
    )
    await ctx.send(bilgi)

@bot.command()
async def havadurumu(ctx):
    bilgi = (
        "Hava kirliliği, atmosferde insan sağlığına ve çevreye zarar veren zararlı maddelerin (gazlar, partiküller) bulunmasıdır. "
        "Kaynaklar: Sanayi tesisleri, motorlu taşıtlar, enerji üretim tesisleri, tarım ilaçları."
    )
    await ctx.send(bilgi)

@bot.command()
async def sukirliligi(ctx):
    bilgi = (
        "Su kirliliği, su kaynaklarının zararlı maddelerle (kimyasallar, atıklar, patojenler) kirlenmesidir. "
        "Kaynaklar: Endüstriyel atıklar, tarım ilaçları, kanalizasyon, plastik atıklar."
    )
    await ctx.send(bilgi)

@bot.command()
async def toprakkirliligi(ctx):
    bilgi = (
        "Toprak kirliliği, toprakta bulunan zararlı maddelerin miktarının artmasıdır. "
        "Kaynaklar: Sanayi atıkları, tarım ilaçları, kimyasal gübreler, petrol sızıntıları."
    )
    await ctx.send(bilgi)

@bot.command()
async def gurultukirliligi(ctx):
    bilgi = (
        "Gürültü kirliliği, yüksek ses düzeylerinin istenmeyen etkilerine verilen isimdir. "
        "Kaynaklar: Trafik, inşaat, endüstriyel tesisler, havaalanları."
    )
    await ctx.send(bilgi)

@bot.command()
async def isikkirliligi(ctx):
    bilgi = (
        "Işık kirliliği, gece gökyüzünün yapay ışıklarla kirlenmesidir. "
        "Kaynaklar: Sokak lambaları, reklam panoları, aydınlatılan binalar."
    )
    await ctx.send(bilgi)

# Hatalı komut durumunda geri bildirim
@bot.event
async def on_command_error(ctxerror):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Böyle bir komut bulunamadı. Lütfen geçerli bir komut girin.")

# Botun token'ını buraya ekleyin
bot.run('MTI0ODcwOTkzNjMzNTE2MzUyMw.GjGzhX.GrSfiOeSASvlU2FHgdOAasGoYsoBel6CgGfrGE'), 