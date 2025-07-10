from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import os

from config import (
    PHOTO_PATH,
    WELCOME_TEXT,
    ABOUT_TEXT,
    SERVICES_TEXT,
    PORTFOLIO_TEXT,
    CONTACT_TEXT
)

# Initialize router for handlers
router = Router()

# Create keyboard for main menu
def get_main_keyboard():
    """Create and return main menu inline keyboard."""
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Обо мне", callback_data="about"),
                types.InlineKeyboardButton(text="Мои услуги", callback_data="services")
            ],
            [
                types.InlineKeyboardButton(text="Портфолио", callback_data="portfolio"),
                types.InlineKeyboardButton(text="Связаться со мной", callback_data="contact")
            ]
        ]
    )
    return keyboard

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Handler for the /start command.
    Sends welcome message with photo and main menu keyboard.
    """
    try:
        # Check if photo exists
        if os.path.exists(PHOTO_PATH):
            # Send photo with caption and keyboard
            photo = FSInputFile(PHOTO_PATH)
            await message.answer_photo(
                photo=photo,
                caption=WELCOME_TEXT,
                reply_markup=get_main_keyboard()
            )
        else:
            # If photo doesn't exist, send text only
            await message.answer(
                text=WELCOME_TEXT,
                reply_markup=get_main_keyboard()
            )
    except Exception as e:
        # Handle any errors gracefully
        await message.answer(
            "Извините, произошла ошибка при запуске бота. Попробуйте позже или обратитесь к администратору."
        )
        print(f"Error in start command: {e}")

@router.callback_query(F.data == "about")
async def process_about_press(callback: types.CallbackQuery):
    """Handler for 'About' button press."""
    try:
        await callback.message.answer(
            text=ABOUT_TEXT,
            reply_markup=get_main_keyboard()
        )
        await callback.answer()
    except Exception as e:
        print(f"Error in about callback: {e}")
        await callback.answer("Произошла ошибка. Попробуйте позже.")

@router.callback_query(F.data == "services")
async def process_services_press(callback: types.CallbackQuery):
    """Handler for 'Services' button press."""
    try:
        await callback.message.answer(
            text=SERVICES_TEXT,
            reply_markup=get_main_keyboard()
        )
        await callback.answer()
    except Exception as e:
        print(f"Error in services callback: {e}")
        await callback.answer("Произошла ошибка. Попробуйте позже.")

@router.callback_query(F.data == "portfolio")
async def process_portfolio_press(callback: types.CallbackQuery):
    """Handler for 'Portfolio' button press."""
    try:
        await callback.message.answer(
            text=PORTFOLIO_TEXT,
            reply_markup=get_main_keyboard()
        )
        await callback.answer()
    except Exception as e:
        print(f"Error in portfolio callback: {e}")
        await callback.answer("Произошла ошибка. Попробуйте позже.")

@router.callback_query(F.data == "contact")
async def process_contact_press(callback: types.CallbackQuery):
    """Handler for 'Contact' button press."""
    try:
        await callback.message.answer(
            text=CONTACT_TEXT,
            reply_markup=get_main_keyboard()
        )
        await callback.answer()
    except Exception as e:
        print(f"Error in contact callback: {e}")
        await callback.answer("Произошла ошибка. Попробуйте позже.")
