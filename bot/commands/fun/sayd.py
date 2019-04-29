from discord.ext import commands


class Sayd(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='sayd',
                      description='Пишет переданный текст, не удаляя оригинал',
                      aliases=['SAYD'],
                      help='sayd [text]')
    async def sayd(self, ctx, text):
        try:
            await ctx.send(text)
            await ctx.message.delete()
        except ValueError as SayError:
            raise SayError
        return


def setup(bot):
    bot.add_cog(Sayd(bot))
