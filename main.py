import vk_api

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import Config
from bot import Bot

#Get settings
config = Config()
token = config.get_token() #group token
timeout = config.get_timeout() #time of pauses between api queries
chats = config.get_chats() #dict with string keys and values = chat_id
active_chat = config.get_active_chat() #string key from 'chats' dictionary

settings = {'timeout': timeout, 'chats': chats, 'active_chat': active_chat}

#Need for bot
vk_session = vk_api.VkApi(token = token)
api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 182872536)

#Start bot working
bot = Bot(vk_session, api, longpoll, settings)
bot.start()