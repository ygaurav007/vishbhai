VishBhai Discord Bot

VishBhai is a Discord bot integrated with Google Gemini AI, capable of generating responses to user messages and keeping track of chat history. The bot stores conversations and can share previous interactions when requested. It can also generate dynamic answers to queries when mentioned.

Features:
Chat history preservation: Keeps track of the chat and allows users to request it.
Integration with Google Gemini API to generate responses based on user inputs.
Responds when mentioned and can handle a variety of topics.
Fully customizable bot name ("VishBhai").

Requirements:
Python 3.7+
Ensure that you have Python 3.7 or higher installed.

Libraries:
discord.py: For interacting with the Discord API.
google-generativeai: For integrating Google Gemini AI.
python-dotenv: To manage environment variables.

Setup
1. Clone the Repository
Clone this repository to your local machine using the following command:

git clone https://github.com/yourusername/vishbhai-discord-bot.git

2. Install Dependencies
Install the required libraries by running:

pip install -r requirements.txt

Alternatively, you can install the dependencies manually using:

pip install discord.py google-generativeai python-dotenv

3. Set Up Environment Variables
Create a .env file in the root of your project and add the following environment variables:

GEMINI_API_KEY=your_google_gemini_api_key_here
SECRET_KEY=your_discord_bot_token_here
GEMINI_API_KEY: Your API key for Google Gemini AI.
SECRET_KEY: Your Discord bot token from the Discord Developer Portal.

4. Run the Bot 
Run the bot with the following command:

python VishBhai.py

If everything is set up correctly, the bot will log in and be ready to start interacting in your Discord server.

5. Invite the Bot to Your Discord Server
Go to the Discord Developer Portal.
Find your application (the bot you created) and navigate to the OAuth2 section.
Under OAuth2 URL Generator, select the following permissions for the bot:
Read Messages
Send Messages
Mention Everyone
Read Message History
Copy the generated URL, paste it into your browser, and invite the bot to your Discord server.

6.Commands
Mention the bot: When you mention VishBhai, the bot will generate a response based on the message.
Example: @VishBhai How does AI work?
View chat history: Ask the bot to show the previous messages.
Example: @VishBhai Show me the previous chats.
Customization
You can change the bot's name and customize the responses by modifying the bot's logic inside the bot.py file. To personalize the bot, change the variable VishBhai to your preferred name.
