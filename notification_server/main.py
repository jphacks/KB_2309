import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
# from flask import Flask, request, jsonify
import threading
from quart import Quart, request, jsonify
# from cog import sample
import asyncio
app = Quart(__name__)
load_dotenv()
env_token = os.getenv('TOKEN')
channel_id = int(os.getenv('CHANNEL_ID'))
intent = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intent)

@app.route('/discord_command')
async def discord_command():
    print("discord_command called")
    asyncio.run_coroutine_threadsafe(hello(), bot.loop)
    return jsonify({'result': 'success'}),200
@bot.event
async def hello():
    channel = bot.get_channel(channel_id)
    await channel.send('そんな姿勢してると後で痛い目見るぞ！')


def run_bot():
    bot.run(env_token)

bot_thread = threading.Thread(target=run_bot)
bot_thread.start()


if __name__ == '__main__':
    app.run(debug=True)


