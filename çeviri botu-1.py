import discord
from discord.ext import commands
from translate import Translator
from itertools import cycle
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

presences = [
    "Translating!",
    "Translating Languages!",
    "Use Me As Translator!",
    "I'm Here To Translate!",
    "Why Don't You Check Translations Skills?",
    "Looking For Translations!",
    "Do You Help With Translations?",
    "I Can Help You With Trasnlations!",
    "I’m looking for a way to help you understand other languages!",
    "I’m trying to help with your translation needs!",
]


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    invite_link = discord.utils.oauth_url(
        bot.user.id,
        permissions=discord.Permissions(),
        scopes=("bot", "applications.commands")
    )
    print(f"Invite link: {invite_link}")

    presences_cycle = cycle(presences)
    while True:
        presence = next(presences_cycle)
        presence_with_count = presence.replace("{guild_count}", str(len(bot.guilds)))
        delay = 30  # Delay in seconds, adjust as needed
        await bot.change_presence(activity=discord.Game(name=presence_with_count))
        await asyncio.sleep(delay)


@bot.command()
async def translate(ctx, target_lang: str, *, text: str):
    # Check if the target language is valid
    valid_languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn',
                       'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka',
                       'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it',
                       'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms',
                       'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru',
                       'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta',
                       'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']  # Add more valid language codes as needed
    if target_lang.lower() not in valid_languages:
        await ctx.send("Invalid target language. Please provide a valid language code.")
        return

    # Translate the text
    translator = Translator(to_lang=target_lang.lower())
    translation = translator.translate(text)

    # Format the translated text
    translated_message = f'Original: {text}\nTranslated ({target_lang}): {translation}'

    await ctx.send(translated_message)
    
# Replace 'YOUR_TOKEN' with your Discord bot token
bot.run('your-token-here')
