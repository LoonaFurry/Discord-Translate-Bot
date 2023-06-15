import discord
from discord.ext import commands
from translate import Translator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready.')

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
bot.run('MTA2NzYyNTc1ODUwNTMxMjMyNg.GivMub.DhJxQtNpp59_d-xbmq80h6bREIErDmknACoRpo')
