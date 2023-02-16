# Python Keylogging to Telegram

This is a Python script that logs all the keystrokes from a keyboard and sends the data to a Telegram bot. This script can be useful for monitoring the activities of a computer or for debugging purposes.

## Getting Started

1. Clone the repository:

```sh
git clone https://github.com/ankit-pn/python-keylogging-to-telegram
```


2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

3. Create a new Telegram bot and get the bot token.
4. Create a new Telegram channel or group and add your bot to it.
5. Get the channel or group ID. You can do this by sending a message to the channel or group and then visiting the following URL:

```sh
https://api.telegram.org/bot<your-bot-token>/getUpdates
```

6. Edit config.json file with your bot_token and chat_id. You can also set time after which you recieve the message

```json
{
    "bot_token": "YOUR ACCESS ID",
    "chat_id": "YOUR CHAT ID",
    "timer": 30
}
```

## Usage

1. Activate your virtual environment (if you are using one).

2. Run the script:
```sh
python3 keylogger.py
```
3. Press any key on the keyboard.
4. Check the Telegram channel or group. You should receive a message containing the keystrokes you typed.


## Author

👤 **Ankit Kumar**

* Website: https://ankit2003.netlify.app
* Github: [@ankit-pn](https://github.com/ankit-pn)
* LinkedIn: [@ankit-pn](https://linkedin.com/in/ankit-pn)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/ankit-pn/random-wordpair-generator/issues). 

## Security

Keylogging can be a serious security concern, as it can be used to capture sensitive information such as passwords. Therefore, it is important to use this script responsibly and only on machines that you own or have permission to monitor.

