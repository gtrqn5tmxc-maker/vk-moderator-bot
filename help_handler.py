# help_handler.py - Красивая команда /help

def get_help_text(is_admin=False):
    """Возвращает форматированный текст помощи"""
    
    public_help = """
🤖 БОТ-МОДЕРАТОР | Команды

👮 МОДЕРАЦИЯ:
/warn [@user] [причина] - выдать предупреждение
/mute [@user] [время] - ограничить чат
/ban [@user] [причина] - заблокировать в чате

📊 СТАТИСТИКА:
/stats [@user] - статистика пользователя  
/mtop - топ активных участников
/id [@user] - информация об аккаунте

🏷️ НИКНЕЙМЫ:
/setnick [@user] [ник] - установить ник
/rnick [@user] - удалить ник
/nlist - список всех ников

🛠️ УТИЛИТЫ:
/help - показать это меню  
/жив - проверить работу бота
"""
    
    admin_help = public_help + """

🛡️ АДМИН-ПАНЕЛЬ:
/staff - команда модераторов
/warns [@user] - список предупреждений  
/banlist - заблокированные
/mutelist - замьюченные
"""
    
    return admin_help if is_admin else public_help

def handle_help_command(user_id, chat_id):
    """Обработчик команды /help"""
    # Здесь будет проверка прав is_admin
    return get_help_text(is_admin=False)
