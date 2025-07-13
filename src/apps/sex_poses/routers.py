from aiogram import F, Router, html, Bot
from aiogram.types import Message
from src.apps.sex_poses.utils import get_random_pose

router = Router()


@router.message(F.text == "🎲 Выбрать позу")
async def handle_choose_pose(message: Message) -> None:
    name, image, dignity, tip = await get_random_pose()

    await message.answer_dice(emoji="🎲")
    await message.bot.send_photo(chat_id=message.chat.id, photo=image)

    text = (
        f"{html.bold('🔥 Поза:')} {html.quote(name)}\n\n"
        f"{html.bold('✨ Достоинство:')}\n{html.quote(dignity)}\n\n"
        f"{html.bold('💡 Совет:')}\n{html.quote(tip)}"
    )

    await message.reply(text)
