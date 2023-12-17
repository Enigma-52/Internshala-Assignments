import discord
from discord.ext import commands
import mysql.connector

# Connecting to DB
db = mysql.connector.connect(
    host="your-hostname", user="username", password="password", database="your-database-name"
)
cursor = db.cursor()

intents = discord.Intents.all()
intents.messages = True

# Bot prefix
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("------")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "!authenticate" in message.content.lower():
        auth_token = message.content.split()[1]

        # Check if the provided auth_token exists in the database
        cursor.execute(
            "SELECT id FROM discord_servers WHERE auth_token = %s", (auth_token,)
        )
        result = cursor.fetchone()

        if result:
            # If authenticated, update the database with the server ID
            server_id = str(message.guild.id)
            cursor.execute(
                "UPDATE discord_servers SET id = %s WHERE auth_token = %s",
                (server_id, auth_token),
            )
            db.commit()

            await message.channel.send(
                "Authentication successful. This server is now authenticated."
            )
        else:
            await message.channel.send(
                "Authentication failed. The provided auth_token is not valid."
            )

    if "!hello" in message.content.lower():
        # Check if the server is authenticated
        cursor.execute(
            "SELECT id FROM discord_servers WHERE id = %s", (str(message.guild.id),)
        )
        result = cursor.fetchone()

        if result:
            await message.channel.send(
                f"Hello, World! This is the {message.guild.name} server."
            )
        else:
            await message.channel.send("This server is not authenticated.")


bot.run("BOT-TOKEN")
