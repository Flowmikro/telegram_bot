import asyncio

from aiogram import F, Router, html
from aiogram.types import Message
from src.apps.places.utils import random_generate_pose_and_location

router = Router()


@router.message(F.text == "🎲 Выбрать позу и место")
async def handle_choose_pose_and_location(message: Message) -> None:
    location, pose, description = await random_generate_pose_and_location()

    await message.answer_dice(emoji="🎲")

    text = (
        f"{html.bold('🛏️ Место:')} {html.quote(location)}\n"
        f"{html.bold('💋 Поза:')} {html.quote(pose)}\n"
        f"{html.bold('🔥 Описание:')} {html.quote(description)}"
    )
    await asyncio.sleep(4)
    await message.answer(text)
