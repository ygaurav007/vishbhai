import discord
import os
import google.generativeai as genai

# Configuring the Gemini API 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Discord bot token
token = os.getenv("SECRET_KEY")

# Variable to preserve chats to use in future to use in the bot
chat_history = []

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        global chat_history 

        # Ignore messages from the bot itself as we only want to answer to user messages
        if message.author == self.user:
            return

        # Preserve the chat in the history for future use
        chat_history.append({"author": message.author.name, "content": message.content})

        # Check if the bot is mentioned in the message or not as it answer only when it is mentioned 
        if self.user in message.mentions:
            try:
                # Handle specific requests for chat history by searching for keywords
                if "previous chats" in message.content.lower():
                    history = "\n".join(
                        [f"{chat['author']}: {chat['content']}" for chat in chat_history]
                    )
                    await message.channel.send(f"Here is the chat history:\n{history}")
                    return

                # Generate a response using Gemini API , Here I am using the gemini-1.5-flash model 
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(message.content)
                message_to_send = response.text

                # Append or add the response of the bot to the history
                chat_history.append({"author": "VishBhai", "content": message_to_send})

                await message.channel.send(message_to_send)
            except Exception as e:
                print(f"Error generating response: {e}")
                await message.channel.send("Sorry, I couldn't process your message.")

# Initialize bot intents
intents = discord.Intents.default()
intents.message_content = True

# Create and run the bot client
client = MyClient(intents=intents)
client.run(token)
