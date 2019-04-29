from discord.ext import commands
from _geo import *
import discord
import os


class Map(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='map',
                      description='Выполняет поиск в интернете',
                      aliases=['MAP'],
                      help='''map [target] <'-z=n'> - где n число от 2 до 19''')
    async def map(self, ctx, target, *args, z='z=10'):
        args = (target,) + args
        target = ' '.join(args)
        if '-z=' in target.split()[-1]:
            z = target.split()[-1][1:]
            target = ' '.join(target.split()[:-1])
        try:
            coordinates = get_geo_info(target)
            map_image(coordinates, add_params=z)
        except ValueError as MapError:
            raise MapError

        _embed = discord.Embed(colour=0x90ff86)
        _embed.set_author(name=f'''Карта по запросу "{target.title()}"''')
        _embed.set_image(url='attachment://map.png')
        _embed.set_footer(text=f'''Координаты {coordinates[::-1]}''')
        await ctx.send(file=discord.File('map.png'), embed=_embed)
        os.remove('map.png')
        return


def setup(bot):
    bot.add_cog(Map(bot))
