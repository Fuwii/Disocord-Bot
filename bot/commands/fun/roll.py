import discord
from discord.ext import commands
import random


class Roll(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='roll',
                      description='Выводит случайное число',
                      aliases=['ROLL'],
                      help='roll <-r=n> - где n число от 10 до 10000')
    async def roll(self, ctx, *args, r=100):
        if args:
            if '-r=' in args[0]:
                try:
                    r = int(args[0][3:])
                    if r > 10000 or r < 10:
                        raise ValueError
                except ValueError as RollError:
                    raise RollError

        num = str(random.randint(0, r))
        _l = [i for i in num[::-1]]
        while len(_l) != 5:
            _l.append('-')
        _embed = discord.Embed(colour=0x90ff86)
        _embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        _embed.description = f'```css\n[{_l[4]}][{_l[3]}][{_l[2]}][{_l[1]}][{_l[0]}]```'
        await ctx.send(embed=_embed)
        return


def setup(bot):
    bot.add_cog(Roll(bot))
