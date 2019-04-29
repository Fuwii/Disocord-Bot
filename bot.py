from discord.ext import commands
import traceback
import discord
import random
import json


class PythonBot(commands.Bot):
    def __init__(self, config: dict, commands: dict):
        super().__init__(config["prefix"])
        self.cfg = config
        self.cfd = commands
        self.steps = {"ignore": {}, "start": [], "step_1": [], "step_2": []}
        self.fake_name = {}
        self.id = None
        self.display_name = None
        with open('bot/assets/dialogs.json', encoding='utf8') as djf:
            self.dialogs = json.load(djf)

        for cog in commands["commands"]:
            try:
                print('[Python]: Loading {}...'.format(cog))
                self.load_extension(cog)
                print('[Python]: Loaded {}!'.format(cog))
            except Exception as LoadingError:
                print('[Python]: An error has occurred while loading cog {}:'.format(cog))
                print(traceback.format_exc())

    async def on_ready(self):
        self.id = self.user.id
        self.display_name = self.user.display_name
        print('[Python]: Python has logged in!')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f'''```css\n~{ctx.command.help}```''')

        elif isinstance(error, commands.errors.CommandInvokeError):
            if type(error.original) == IndexError:
                await ctx.send(f'''```yaml\n{self.cfd["errors"]["IndexError"][str(ctx.command)]}```''')
            elif type(error.original) == ValueError:
                _embed = discord.Embed(colour=0xfc5f6a)
                _embed.set_author(name=self.cfd["errors"]["ValueError"][str(ctx.command)])
                _embed.add_field(name=f'Помощь в использовании ~`{ctx.command}`',
                                 value=f'''```css\n~{self.cfd["examples"][str(ctx.command)]}```''')
                await ctx.send(embed=_embed)
        else:
            print(ctx.command, error)

    async def on_message(self, message):
        if not self.display_name or not self.id:
            return
        if message.author.id == self.id:
            return

        msg = message.content.lower()
        atr = str(message.author)
        if self.display_name.lower() in msg:

            if atr in self.steps["ignore"]:
                num = self.steps["ignore"][atr]
                self.steps["ignore"][atr] = num - 1
                if self.steps["ignore"][atr] == 0:
                    self.steps["ignore"].pop(atr)
                    first = random.choice([f'{message.author.mention} ', ''])
                    if atr in self.fake_name:
                        first = self.fake_name[atr] + ' '
                    second = random.choice(self.dialogs["random_sr"])
                    await message.channel.send(first + second)
                    return
                first = random.choice([f'{message.author.mention} ', ''])
                if atr in self.fake_name:
                    first = self.fake_name[atr] + ' '
                second = random.choice(self.dialogs["random_s"])
                await message.channel.send(first + second)
                return

            elif ('зови' in msg or 'называй') and 'меня' in msg:
                self.fake_name[atr] = ' '.join(message.content.split()[3:])
                await message.channel.send(f'Есть! {self.fake_name[atr]}')

            elif 'ты' in msg:
                for i in self.dialogs["insult"]:
                    if i in msg:
                        self.steps["ignore"][atr] = 3
                        first = random.choice([f'{message.author.mention} ', ''])
                        if atr in self.fake_name:
                            first = self.fake_name[atr] + ' '
                        second = random.choice(self.dialogs["random_i"])
                        await message.channel.send(first + second)
                        return

            else:
                self.steps['start'].append(message.author.id)
                first = random.choice([f'{message.author.mention} ', ''])
                if atr in self.fake_name:
                    first = self.fake_name[atr] + ' '
                second = random.choice(self.dialogs["random_1"])
                await message.channel.send(first + second)
                return
        else:
            await self.process_commands(message)


with open('bot/assets/config.json', encoding='utf8') as jf:
    cfg = json.load(jf)
with open('bot/assets/commands.json', encoding='utf8') as cf:
    cfd = json.load(cf)
bot = PythonBot(config=cfg, commands=cfd)
bot.run(cfg["token"])
