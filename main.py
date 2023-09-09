from twitchio.client import Client
from twitchio.ext import commands, eventsub
from tokens import *

class Bot(commands.Bot):

    def __init__(self):
        # initialise the bot wih accesstoken and clientid, to access my channel (dunewalkerz) feel free to change it to your own channel
        
        # prefix is the symbol that will be used to invoke the bot, in this case it is {!}
        super().__init__(
                        token = StatueAccessToken,
                        client_id= altAppClentID,
                        client_secret=altAppClientSecret,
                        prefix='!',
                        initial_channels=['dunewalkerz'])

    async def event_ready(self):
        ##will inform if the bot is ready to chat and use commands
        # basicly when it oprational
        
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
    
    
    async def event_message(self, ctx ):
        # Messages with echo set to True are messages sent by the bot...
        # basicly disables the bot from responding to itself also has an error if on and stopes theretical infinia loop
        if ctx.echo:
            return

        # Print the contents of our message to console...
        # this mainly is a test to see if the bot is working
        print(ctx.content)
        # print(ctx.author.name)

        # when calling a command this is needed to be able to use the commands
        # Since we have commands and are overriding the default `event_message`
        await self.handle_commands(ctx)
        

    @commands.command(name='hello')
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')
        
    @commands.command(name='who')
    async def get_chatters(self,ctx):
        
        #currently this is not working smadge is looking into it
        chatters = await self.get_chatters('dunewalkerz')
        print(chatters.all)
        all_chatters = ' '.join(chatters.all)
        await ctx.send(f"In chat: {all_chatters}")



if __name__ == "__main__":
    bot = Bot()
    #extra command can be added here but think it is better to have them above

    bot.run()