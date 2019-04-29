from discord.ext import commands


class Say(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='say',
                      description='Пишет переданный текст, но удаляет оригинал',
                      aliases=['SAY'],
                      help='say [text]')
    async def say(self, ctx, text):
        try:
            await ctx.send(text)
        except ValueError as SayError:
            raise SayError
        return


def setup(bot):
    bot.add_cog(Say(bot))
