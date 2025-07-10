import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers.user_handlers import router
from config import BOT_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Register routers
dp.include_router(router)

async def main():
    """
    Main function to start the bot.
    """
    try:
        # Delete webhook before polling
        await bot.delete_webhook(drop_pending_updates=True)
        
        # Start polling
        logging.info("Starting bot...")
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Critical error: {e}")
    finally:
        # Close bot session
        logging.info("Shutting down...")
        await bot.session.close()

if __name__ == '__main__':
    try:
        # Run the bot
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
