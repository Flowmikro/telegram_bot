import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup

from src.core.settings import settings
from src.apps.places.routers import router as places_router
from src.apps.places.buttons import choose_pose_and_location_button
from src.apps.sex_poses.buttons import choose_pose_button
from src.apps.sex_poses.routers import router as sex_poses_router

dp = Dispatcher()

dp.include_router(places_router)
dp.include_router(sex_poses_router)

kb = ReplyKeyboardMarkup(
    keyboard=[
        [choose_pose_button],
        [choose_pose_and_location_button],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"👋 Привет! Этот бот подскажет интересные позы и идеи для близости с партнёром.\n"
        f"👇 Выбери, что попробовать первым",
        reply_markup=kb,

    )


async def main() -> None:
    bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
