import vk_api

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import Config
from bot import Bot

#Get settings
properties = ['token', 'timeout', 'chats', 'active_chat']
config = Config(properties)

#Need for bot
settings = config.get_settings()
vk_session = vk_api.VkApi(token = settings['token'])
api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 182872536)

#Start bot working
bot = Bot(vk_session, api, longpoll, settings)
bot.start()