import discord
import openai
from keys import AI_KEY, Token
ai_key = AI_KEY
openai.api_key = ai_key 
my_secret = Token
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        if message.author == self.user:
            return
        print(f'Message from {message.author}: {message.content}')
        if self.user.mentioned_in(message):
            channel = message.channel
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message.content}],
                    temperature=1,
                    max_tokens=50,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                message_content = response.choices[0].message.content  
                print(message_content)
                await channel.send(message_content)
            except Exception as e:
                print(f"Error: {e}")
                await channel.send("Sorry, I couldn't process that request.")
intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(my_secret)