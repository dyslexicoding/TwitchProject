from twitchio.client import Client
from twitchio.ext import commands, eventsub
from tokens import *

# initialise the bot wih accesstoken and clientid, to access my channel (dunewalkerz) feel free to change it to your own channel
# prefix is the symbol that will be used to invoke the bot, in this case it is {!}
bot = commands.Bot(
    token = StatueAccessToken,  
    client_id= altAppClentID,
    client_secret=altAppClientSecret,
    nick='statue_sama',
    prefix='!',
    initial_channels=['dunewalkerz'],
)

@bot.event()
async def event_ready(ctx:commands.Context):
    ##will inform if the bot is ready to chat and use commands
    # basicly when it oprational
    
    print(f'Logged in as | {bot.nick}')
    print(f'User id is | {bot.user_id}')
    

@bot.event()
async def event_message(ctx):
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
    await bot.handle_commands(ctx)
    

@bot.command(name='hello')
async def hello(ctx: commands.Context):
    # Send a hello back!
    # Sending a reply back to the channel is easy... Below is an example.
    await ctx.send(f'Hello {ctx.author.name}!')
    
#i want an event reation based on if there is a channel point redemption


if __name__ == "__main__":
    bot.run()