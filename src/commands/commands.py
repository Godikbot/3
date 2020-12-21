from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
bp = Blueprint("COMMANDS")
from prefixs import p
from unit import edit_msg
@bp.on.message_handler(FromMe(), text=[p+'команды', p+'кмд'], lower=True)
async def cms(ans:Message):
    text = f"""
Юзербот by yMoth 🥺
Ваши команды:
Калькулятор: реши 1 + 1
Анимация: аним/анимция
Добовления комментария: +коммент [enter] текст
Инфо: инфо/информация
Лайк авы: лайкнуть/длайк
Рандом: выбери <1> или <2>
Вероятность: вероятность <text>
Вечный онлайн: +онлайн, +оффлайн/+онл,+офл
Время: время/тайм
Википедия: вики <запрос>
Добовления в друзья: +др, вдр
Добовления в чс: +чс, вчс
Шаблоны: +шаб [nameshub] [enter] [text]
АвтоФерма: +автоферма
id: реплей(ид, айди)
"""
    await edit_msg(ans, text)

@bp.on.message_handler(FromMe(), text=[p+'обновления', p+'обновы'], lower=True)
async def update(ans:Message):
    from unit import __updates__
    txt = f"""
Обновление:
{__updates__}"""

    await edit_msg(ans, txt)