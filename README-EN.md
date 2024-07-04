[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/MMproBump_bot?start=ref_6597427426)

> 🇷🇺#### Join my [Telegram channel](https://t.me/scriptron). I will be posting news about new bots and scripts there.
## Important Notes

> 🇪🇳 README на русском [тут](README-RU.md)

- **Python Version:** The software runs on Python 3.10, Python 3.11. Using a different version may cause errors.
- DONT USE MAIN ACCOUNT BECAUSE THERE IS ALWAYS A CHANCE TO GET BANNED IN TELEGRAM

## Functionality
| Feature                                                        | Supported  |
|----------------------------------------------------------------|:----------:|
| Multithreading                                                 |     ✅     |
| Binding a proxy to a session                                   |     ✅     |
| Auto-claim daily grant                                         |     ✅     |
| Automatic farming                                              |     ✅     |
| Support tdata and pyrogram .session                            |     ✅     |

## [Options](https://github.com/Re-Diss/MMProBumpBot/blob/main/.env-example)
| Option                  | Description                                                                |
|-------------------------|----------------------------------------------------------------------------|
| **API_ID / API_HASH**   | Platform data from which to launch a Telegram session (stock - Android)    |
| **SLEEP_BEFORE_CLAIM**   | Sleep before claiming the reward, by default: [3600, 5600] seconds         |
| **USE_PROXY_FROM_FILE** | Whether to use proxy from the `bot/config/proxies.txt` file (True / False) |

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the `data/config.py` file.


## Quick start
### Windows
1. Ensure you have **Python 3.10** or a newer version installed.
2. Use `INSTALL.bat` to install, then specify your API_ID and API_HASH in the .env file.
3. Use `START.bat` to launch the bot (or in the console: `python main.py`).

### Linux
1. Clone the repository: `git clone https://github.com/Re-Diss/MMProBumpBot.git && cd MMProBumpBot`
2. Run the installation: `chmod +x INSTALL.sh START.sh && ./INSTALL.sh`, then specify your API_ID and API_HASH in the .env file.
3. Use `./START.sh` to run the bot (or in the console: `python3 main.py`).

## Manual installation
You can download [**Repository**](https://github.com/Re-Diss/MMProBumpBot) by cloning it to your system and installing the necessary dependencies:
```shell
~ >>> git clone https://github.com/Re-Diss/MMProBumpBot.git
~ >>> cd MMProBumpBot

# Linux
~/MMProBumpBot >>> python3 -m venv venv
~/MMProBumpBot >>> source venv/bin/activate
~/MMProBumpBot >>> pip3 install -r requirements.txt
~/MMProBumpBot >>> cp .env-example .env
~/MMProBumpBot >>> nano .env # specify your API_ID and API_HASH, the rest can be left as default
~/MMProBumpBot >>> python3 main.py

# Windows
~/MMProBumpBot >>> python -m venv venv
~/MMProBumpBot >>> venv\Scripts\activate
~/MMProBumpBot >>> pip install -r requirements.txt
~/MMProBumpBot >>> copy .env-example .env
~/MMProBumpBot >>> # open .env file and specify your API_ID and API_HASH, the rest can be left as default
~/MMProBumpBot >>> python main.py
```

Also for quick launch you can use arguments:
```shell
~/MMProBumpBot >>> python3 main.py --action (1/2)
# or
~/MMProBumpBot >>> python3 main.py -a (1/2)

# 1 - Create session
# 2 - Run bot
```
