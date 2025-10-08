import vk_api
import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import config

print("🚀 VK Bot запускается...")

def can_respond(chat_id):
    if config.TEST_MODE:
        return chat_id in config.TEST_CHAT_IDS
    return True

try:
    TOKEN = config.VK_GROUP_TOKEN
    GROUP_ID = config.VK_GROUP_ID
    
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    vk = vk_session.get_api()
    
    print("✅ Бот авторизован!")
    print(f"🔧 Тестовый режим: {'ВКЛ' if config.TEST_MODE else 'ВЫКЛ'}")

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            # Фикс двойных сообщений
            if event.object.message.get('from_id') < 0:
                continue
            
            msg = event.object.message['text']
            user_id = event.object.message['from_id']
            chat_id = event.object.message['peer_id']
            
            if not can_respond(chat_id):
                print(f"❌ Пропускаем чат {chat_id}")
                continue
            
            print(f"🔍 [ЧАТ: {chat_id}] [ЮЗЕР: {user_id}]: {msg}")
            
            if msg.lower() == '/help':
                vk.messages.send(
                    peer_id=chat_id,
                    message='🎮 Мои команды:\n/help - помощь\n/жив - проверка\n/id - айди чата\n/stats - статистика',
                    random_id=0
                )
            elif msg.lower() == '/жив':
                vk.messages.send(
                    peer_id=chat_id,
                    message='🔮 Бот активен и готов к работе!',
                    random_id=0
                )
            elif msg.lower() == '/id':
                vk.messages.send(
                    peer_id=chat_id,
                    message=f'📟 Айди этого чата: {chat_id}',
                    random_id=0
                )
            elif msg.lower().startswith('/stats'):
                # Получаем информацию о пользователе
                user_info = vk.users.get(user_ids=user_id, fields='first_name,last_name')[0]
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Формируем статистику ТВОЕГО формата
                stats_text = f"""Информация о {user_info['first_name']} {user_info['last_name']}

Роль: Участник
Блокировок: 0
Общая блокировка в чатах: Нет
Общая блокировка в беседах игроков: Нет
Активные предупреждения: 0
Блокировка чата: Нет
Ник: Нет
Всего сообщений: 0
Последнее сообщение: {current_time} МСК (UTC+3)
""".strip()
                
                vk.messages.send(
                    peer_id=chat_id,
                    message=stats_text,
                    random_id=0
                )
                
except Exception as e:
    print(f"❌ Ошибка: {e}")
