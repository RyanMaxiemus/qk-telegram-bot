#!/usr/bin/env python3
"""
Telegram Bot with Custom Dark-Themed Keyboard
Provides 8 specialized commands for file operations, cloud storage, and media downloading
"""

import os
import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'your_bot_token_here')

class TelegramBot:
    def __init__(self):
        """Initialize the Telegram bot with custom keyboard"""
        self.application = None
        self.setup_keyboard()
    
    def setup_keyboard(self):
        """Setup the custom dark-themed keyboard with 8 specialized buttons"""
        # Create keyboard buttons with emoji-only layout - arranged in 2 rows of 4
        # Row 1: File operations and Telegram operations
        row1 = [
            KeyboardButton("🔒"),    # Encrypt File
            KeyboardButton("🔓"),    # Decrypt File
            KeyboardButton("📤"),    # Telegram Upload
            KeyboardButton("📥")     # Telegram Download
        ]
        
        # Row 2: Cloud operations and media downloading
        row2 = [
            KeyboardButton("⛅"),    # Cloud Upload
            KeyboardButton("☁"),     # Cloud Download
            KeyboardButton("🌐"),    # Web Scraper
            KeyboardButton("📱")     # Social Media Download
        ]
        
        # Create keyboard markup that will appear as a persistent custom keyboard
        # This replaces the user's regular keyboard with our custom button layout
        self.custom_keyboard = ReplyKeyboardMarkup(
            keyboard=[row1, row2],
            resize_keyboard=True,        # Fits screen size
            one_time_keyboard=False,     # Stays visible after button press
            input_field_placeholder="💎 Choose a command..."
        )
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command - Display welcome message and custom keyboard"""
        user = update.effective_user
        welcome_message = (
            f"🌟 Welcome to the Dark Ops Bot, {user.first_name}! 🌟\n\n"
            "💎 Your premium file operations center is ready!\n"
            "🔹 Choose from 8 specialized commands below:\n\n"
            "🔒 File Security: Encrypt/Decrypt files\n"
            "📤 Telegram Ops: Upload/Download via Telegram\n" 
            "☁️ Cloud Storage: Manage cloud files\n"
            "🌐 Media Tools: Web scraping & social downloads\n\n"
            "✨ Select any button to get started!"
        )
        
        await update.message.reply_text(
            welcome_message,
            reply_markup=self.custom_keyboard
        )
        logger.info(f"User {user.id} started the bot")
    
    async def encrypt_file_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle encrypt file command"""
        response = (
            "🔒 **Encrypt File Command Activated!**\n\n"
            "💎 File encryption service is ready!\n"
            "🔹 Send me a file to encrypt with AES-256 encryption\n"
            "🔹 Your files will be secured with military-grade encryption\n\n"
            "⚡ Feature coming soon! Stay tuned for secure file operations."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested file encryption")
    
    async def decrypt_file_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle decrypt file command"""
        response = (
            "🔓 **Decrypt File Command Activated!**\n\n"
            "💎 File decryption service is ready!\n"
            "🔹 Send me an encrypted file to decrypt\n"
            "🔹 Supports all major encryption formats\n\n"
            "⚡ Feature coming soon! Your secure vault awaits."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested file decryption")
    
    async def telegram_upload_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle Telegram upload command"""
        response = (
            "⬆️ **Telegram Upload Command Activated!**\n\n"
            "💎 Direct Telegram upload service is ready!\n"
            "🔹 Upload files directly to Telegram servers\n"
            "🔹 Supports all file types up to 2GB\n\n"
            "⚡ Feature coming soon! Lightning-fast uploads await."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested Telegram upload")
    
    async def telegram_download_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle Telegram download command"""
        response = (
            "⬇️ **Telegram Download Command Activated!**\n\n"
            "💎 Telegram download service is ready!\n"
            "🔹 Download files from Telegram channels/chats\n"
            "🔹 Batch download capabilities available\n\n"
            "⚡ Feature coming soon! Mass download power incoming."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested Telegram download")
    
    async def cloud_upload_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle cloud upload command"""
        response = (
            "☁️⬆️ **Cloud Upload Command Activated!**\n\n"
            "💎 Multi-cloud upload service is ready!\n"
            "🔹 Upload to Google Drive, Dropbox, OneDrive\n"
            "🔹 Automatic backup and sync capabilities\n\n"
            "⚡ Feature coming soon! Your cloud empire awaits."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested cloud upload")
    
    async def cloud_download_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle cloud download command"""
        response = (
            "☁️⬇️ **Cloud Download Command Activated!**\n\n"
            "💎 Multi-cloud download service is ready!\n"
            "🔹 Download from all major cloud providers\n"
            "🔹 Smart file organization and management\n\n"
            "⚡ Feature coming soon! Cloud mastery unlocked."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested cloud download")
    
    async def scrape_media_download_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle web scraping media download command"""
        response = (
            "🌐⬇️ **Web Scrape Command Activated!**\n\n"
            "💎 Advanced web scraping service is ready!\n"
            "🔹 Extract media from any website\n"
            "🔹 Smart content detection and filtering\n\n"
            "⚡ Feature coming soon! Web harvesting powers loading."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested web scraping")
    
    async def social_download_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle social media download command"""
        response = (
            "📱⬇️ **Social Download Command Activated!**\n\n"
            "💎 Social media download service is ready!\n"
            "🔹 Download from Instagram, TikTok, YouTube, Twitter\n"
            "🔹 High-quality media extraction guaranteed\n\n"
            "⚡ Feature coming soon! Social media domination incoming."
        )
        await update.message.reply_text(response, parse_mode='Markdown')
        logger.info(f"User {update.effective_user.id} requested social download")
    
    async def handle_keyboard_buttons(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button presses from the custom keyboard"""
        text = update.message.text
        
        # Map button text to command functions
        button_mapping = {
            "🔒": self.encrypt_file_command,
            "🔓": self.decrypt_file_command,
            "📤": self.telegram_upload_command,
            "📥": self.telegram_download_command,
            "⛅": self.cloud_upload_command,
            "☁": self.cloud_download_command,
            "🌐": self.scrape_media_download_command,
            "📱": self.social_download_command
        }
        
        if text in button_mapping:
            await button_mapping[text](update, context)
        else:
            # Handle unknown messages
            await update.message.reply_text(
                "🤖 I didn't understand that command.\n"
                "💎 Please use the keyboard buttons below or send /start to see all options!",
                reply_markup=self.custom_keyboard
            )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = (
            "🌟 **Dark Ops Bot - Command Reference** 🌟\n\n"
            "**Available Commands:**\n"
            "• `/start` - Display main menu with custom keyboard\n"
            "• `/help` - Show this help message\n\n"
            "**Keyboard Functions:**\n"
            "🔒 **Encrypt File** - Secure file encryption\n"
            "🔓 **Decrypt File** - File decryption service\n"
            "⬆️ **Upload to Telegram** - Direct Telegram uploads\n"
            "⬇️ **Download from Telegram** - Telegram file downloads\n"
            "☁️⬆️ **Upload to Cloud** - Multi-cloud upload service\n"
            "☁️⬇️ **Download from Cloud** - Cloud file downloads\n"
            "🌐⬇️ **Scrape Web** - Web media extraction\n"
            "📱⬇️ **Download from Socials** - Social media downloads\n\n"
            "💎 All features are currently in development!"
        )
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.error(f"Exception while handling an update: {context.error}")
        
        if isinstance(update, Update) and update.effective_message:
            await update.effective_message.reply_text(
                "⚠️ An error occurred while processing your request.\n"
                "🔧 Please try again or contact support if the problem persists."
            )
    
    def setup_handlers(self):
        """Setup all command and message handlers"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("encrypt_file", self.encrypt_file_command))
        self.application.add_handler(CommandHandler("decrypt_file", self.decrypt_file_command))
        self.application.add_handler(CommandHandler("telegram_upload", self.telegram_upload_command))
        self.application.add_handler(CommandHandler("telegram_download", self.telegram_download_command))
        self.application.add_handler(CommandHandler("cloud_upload", self.cloud_upload_command))
        self.application.add_handler(CommandHandler("cloud_download", self.cloud_download_command))
        self.application.add_handler(CommandHandler("scrape_media_download", self.scrape_media_download_command))
        self.application.add_handler(CommandHandler("social_download", self.social_download_command))
        
        # Message handler for keyboard buttons
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_keyboard_buttons))
        
        # Error handler
        self.application.add_error_handler(self.error_handler)
    
    def run(self):
        """Run the bot"""
        try:
            # Create application
            self.application = Application.builder().token(BOT_TOKEN).build()
            
            # Setup handlers
            self.setup_handlers()
            
            logger.info("🚀 Dark Ops Bot is starting...")
            logger.info("💎 Custom keyboard with 8 specialized commands loaded")
            
            # Start the bot
            self.application.run_polling()
            
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")
            raise

def main():
    """Main function to run the bot"""
    if not BOT_TOKEN or BOT_TOKEN == 'your_bot_token_here':
        logger.error("❌ TELEGRAM_BOT_TOKEN environment variable is not set!")
        logger.error("💡 Please set your bot token: export TELEGRAM_BOT_TOKEN='your_actual_token'")
        return
    
    try:
        bot = TelegramBot()
        bot.run()
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Bot crashed: {e}")

if __name__ == '__main__':
    main()
