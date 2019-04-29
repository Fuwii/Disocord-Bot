import discord
from discord.ext import commands


class Search(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='search',
                      description='Выводит карту на экран',
                      aliases=['SEARCH'],
                      help='search [target]')
    async def search(self, ctx, target, *args):
        args = (target,) + args
        target = '+'.join(args)
        _embed = discord.Embed(colour=0x90ff86)
        _embed.set_author(name=f'''Поиск по запросу "{" ".join(args)}"''')
        _embed.add_field(name='Веб сайты',
                         value=f'''[перейти](https://www.google.com/search?q={target})''')
        _embed.add_field(name='Картинки',
                         value=f'''[перейти](https://www.google.com/search?q={target}&tbm=isch)''')
        _embed.add_field(name='Видео',
                         value=f'''[перейти](https://www.google.com/search?q={target}&tbm=vid)''')
        await ctx.send(embed=_embed)
        return


def setup(bot):
    bot.add_cog(Search(bot))
