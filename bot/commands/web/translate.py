from discord.ext import commands
import _translate
import discord


class Translate(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='translate',
                      description='Выводит карту на экран',
                      aliases=['TRANSLATE'],
                      help='translate [text] <lang=[КОД ЯЗЫКА]>')
    async def search(self, ctx, text, *args, lang='en'):
        args = (text,) + args
        text = ' '.join(args)
        if '-lang=' in text.split()[-1]:
            lang = text.split()[-1][6:]
            text = ' '.join(text.split()[:-1])
        try:
            case = _translate.translate(text, lang=lang)
        except ValueError as TranslateError:
            raise TranslateError
        _embed = discord.Embed(colour=0x91bbff)
        _embed.set_author(name='Перевод')
        _embed.description = f'''```{text}```'''
        _embed.add_field(name=f'''`{case['lang']}`''', value=f'''```{case['text'][0]}```''')
        await ctx.send(embed=_embed)
        return


def setup(bot):
    bot.add_cog(Translate(bot))
