[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/MMproBump_bot?start=ref_6597427426)

#### Подписывайтесь на наш [телеграм канал](https://t.me/scriptron). Там будут новости о новый ботах
> 🇪🇳 README in English available [here](README-EN.md)
## Важно

- **Python Version:** Программное обеспечение работает на Python 3.10, Python 3.11. Использование другой версии может привести к ошибкам.
- НЕ ИСПОЛЬЗУЙТЕ ОСНОВНОЙ АККАУНТ, ПОТОМУ ЧТО ВСЕГДА ЕСТЬ ШАНС ПОЛУЧИТЬ БАН В TELEGRAM

## Функционал
| Функция                                                        | Поддерживается  |
|----------------------------------------------------------------|:---------------:|
| Многопоточность                                                |        ✅       |
| Привязка прокси к сессии                                       |        ✅       |
| Получение ежедневной награды                                   |        ✅       |
| Автоматический фарминг                                         |        ✅       |
| Поддержка tdata и pyrogram .session                            |        ✅       |

## Настройки .env файла
| Опция                   | Описание                                                                |
|-------------------------|-------------------------------------------------------------------------|
| **API_ID / API_HASH**   | Данные платформы, с которой запускать сессию Telegram (сток - Android)  |
| **SLEEP_BEFORE_CLAIM** | Задержка перед сбором прибыли по умолчанию [3600, 5600] секунд          |
| **USE_PROXY_FROM_FILE** | Использовать-ли прокси из файла `bot/config/proxies.txt` (True / False) |

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Получение API ключей
1. Перейдите на сайт [my.telegram.org](https://my.telegram.org) и войдите в систему, используя свой номер телефона.
2. Выберите **"API development tools"** и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `data/config.py`, предоставленные после регистрации вашего приложения.


## Быстрый старт
### Windows
1. Убедитесь, что у вас установлен **Python 3.10** или более новая версия.
2. Используйте `INSTALL.bat` для установки, затем укажите ваши API_ID и API_HASH в .env
3. Используйте `START.bat` для запуска бота (или в консоли: `python main.py`)

### Linux
1. Клонируйте репозиторий: `git clone https://github.com/Re-Diss/MMProBumpBot && cd MMProBumpBot`
2. Выполните установку: `chmod +x INSTALL.sh START.sh && ./INSTALL.sh`, затем укажите ваши API_ID и API_HASH в .env
3. Используйте `./START.sh` для запуска бота (или в консоли: `python3 main.py`)

## Ручная установка
Вы можете скачать [**Репозиторий**](https://github.com/Re-Diss/MMProBumpBot) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
~ >>> git clone https://github.com/Re-Diss/MMProBumpBot.git
~ >>> cd MMProBumpBot

# Linux
~/MMProBumpBot >>> python3 -m venv venv
~/MMProBumpBot >>> source venv/bin/activate
~/MMProBumpBot >>> pip3 install -r requirements.txt
~/MMProBumpBot >>> cp .env-example .env
~/MMProBumpBot >>> nano .env # укажите ваши API_ID и API_HASH, остальное можно оставить по умолчанию
~/MMProBumpBot >>> python3 main.py

# Windows 
~/MMProBumpBot >>> python -m venv venv
~/MMProBumpBot >>> venv\Scripts\activate
~/MMProBumpBot >>> pip install -r requirements.txt
~/MMProBumpBot >>> copy .env-example .env
~/MMProBumpBot >>> nano .env # укажите ваши API_ID и API_HASH, остальное можно оставить по умолчанию
~/MMProBumpBot >>> python main.py
```

Также для быстрого запуска вы можете использовать аргументы:
```shell
~/MMProBumpBot >>> python3 main.py --action (1/2)
# или
~/MMProBumpBot >>> python3 main.py -a (1/2)

# 1 - создать сессию
# 2 - запустить бот
```
