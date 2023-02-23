<h1>Rival Regions Blacklist Bot</h1>
<p>The Rival Regions Blacklist Bot is a Telegram bot that allows users to add their Rival Regions profile to a blacklist to stop receiving messages from the @RRMessage bot. Each Telegram account can only add one profile to the blacklist. The bot only works in private chats and checks if the profile link is in the correct format.</p>
<h2>How It Works</h2>
<p>When a user sends their Rival Regions profile link to the bot in a private chat, the bot checks if the link is valid and has not already been added to the blacklist. If the link is valid and not on the blacklist, the bot adds the profile link to the blacklist and sends a message to a specified group chat. The user is notified that their profile has been added to the blacklist. If the link is not valid or has already been added to the blacklist, the user is notified accordingly.</p>
<h2>Installation</h2>
<ol>
  <li>Clone this repository to your local machine.</li>
  <li>Create a new Telegram bot using the <a href="https://core.telegram.org/bots#creating-a-new-bot">BotFather</a>.</li>
  <li>Copy the bot token provided by BotFather and paste it into the <code>Token</code> variable in the <code>RRMessageBot.py</code> file.</li>
  <li>Run <code>pip install python-telegram-bot</code> to install the Python Telegram Bot library.</li>
  <li>Run <code>python main.py</code> to start the bot.</li>
</ol>
<h2>Usage</h2>
<p>To use the Rival Regions Blacklist Bot, follow these steps:</p>
<ol>
  <li>Start a private chat with the bot.</li>
  <li>Send your Rival Regions profile link to the bot.</li>
  <li>If the link is valid and has not already been added to the blacklist, the bot will add your profile to the blacklist and notify you.</li>
  <li>If the link is not valid or has already been added to the blacklist, the bot will notify you accordingly.</li>
</ol>
<h2>Donations</h2>
<p>If you find this bot useful, you can buy me a coffee:</p>
<a href="https://www.buymeacoffee.com/furkankoykiran"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=furkankoykiran&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff"></a>
