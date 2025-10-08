# main.py - VK Bot
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

print("🚀 VK Bot запускается...")

try:
    import config
    TOKEN = config.VK_GROUP_TOKEN
    GROUP_ID = config.VK_GROUP_ID
    
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    vk = vk_session.get_api()
    
    print("✅ Бот авторизован!")
    
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.object.message['text']
            peer_id = event.object.message['peer_id']
            
            if msg.lower() == '/help':
                vk.messages.send(
                    peer_id=peer_id,
                    message='🤖 Бот работает! /help /жив',
                    random_id=0
                )
            elif msg.lower() == '/жив':
                vk.messages.send(
                    peer_id=peer_id,
                    message='✅ Я жив!',
                    elif msg.lower() == '/id':
    vk.messages.send(
        peer_id=chat_id,
        message=f'🆔 ID этой беседы: `{chat_id}`',
        random_id=0
    )
                    random_id=0
                )
                
except Exception as e:
    print(f"❌ Ошибка: {e}")
