# Discord Python Bot Template
## A simple starting point for creating your very own Discord bot using the discord.py API.

Included is a starter Python bot source code file, an environment file, a Dockerfile, and a requirements file. After that, it's all you buddy - [here's the excellent documentation](https://discordpy.readthedocs.io/en/latest/index.html) for the API. No, I will not help you write your bot.

You can opt to use a Docker container (recommended) or create your own environment. You will obviously need Docker installed for the container environment, or a version of Python 3 and pip. Virtual environments strongly reccommended for non-container setups.

Either way, you'll need a Discord API key to get started. You can acquire one [here](https://discord.com/developers/applications) - create an application, then click bot in the application settings and choose to make the app a bot. Place the given token in the provided .env file. (No, your client key will not work!)

**UNDER NO CIRCUMSTANCES SHOULD THE .ENV FILE W/ KEY BE COMMITED TO YOUR REPOSITORY.** Use a .gitignore file to accomplish this. Discord *will* yell at you and shut off your key if you do by accident, but it's not worth the risk or hassle.