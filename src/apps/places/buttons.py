from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choose_pose_and_location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎲 Выбрать позу и место")]
    ],
    resize_keyboard=True
)
