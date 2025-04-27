import telebot
import yt_dlp
import logging
import os
import re
from telebot import types
 
# تنظیمات
TOKEN = "TOKEN_BOT"
COOKIES_FILE = r"C:\Users\mahdi\OneDrive\Desktop\BOT\cookies.txt"  # مسیر کوکی
DOWNLOAD_FOLDER = os.path.abspath("downloads")

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

bot = telebot.TeleBot(TOKEN)

# لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

user_data = {}

# چک کردن لینک یوتیوب
def is_valid_youtube_url(url):
    pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return re.match(pattern, url) is not None

# گرفتن کیفیت‌های ویدیو
def get_formats(url):
    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'cookiefile': COOKIES_FILE,   # اضافه کردن کوکی برای دور زدن کپچا
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = []
            for f in info['formats']:
                if f.get('vcodec') != 'none' and f.get('acodec') != 'none':
                    formats.append({
                        'format_id': f['format_id'],
                        'resolution': f.get('format_note') or f.get('height'),
                        'ext': f['ext'],
                        'filesize': f.get('filesize') or 0
                    })
            return formats
    except Exception as e:
        logger.error(f"Error fetching formats: {e}")
        return None

# دانلود ویدیو بر اساس فرمت
def download_video(url, format_id, chat_id, msg_id):
    try:
        def hook(d):
            if d['status'] == 'downloading':
                percent = d.get('_percent_str', '').strip()
                try:
                    bot.edit_message_text(f"⬇️ در حال دانلود... {percent}", chat_id, msg_id)
                except:
                    pass

        ydl_opts = {
            'format': format_id,
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'quiet': True,
            'progress_hooks': [hook],
            'cookiefile': COOKIES_FILE,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        logger.error(f"Error in download: {e}")
        return None

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 سلام! لینک یوتیوبتو بفرست تا دانلود رو شروع کنیم.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text.strip()
    if is_valid_youtube_url(url):
        formats = get_formats(url)
        if formats:
            user_data[message.chat.id] = {'url': url, 'formats': formats}

            markup = types.InlineKeyboardMarkup()
            for fmt in formats:
                label = f"{fmt['resolution']} - {fmt['ext']} - {round(fmt['filesize']/1024/1024,2) if fmt['filesize'] else '؟'}MB"
                markup.add(types.InlineKeyboardButton(text=label, callback_data=fmt['format_id']))

            bot.send_message(message.chat.id, "✅ کیفیت دلخواهتو انتخاب کن:", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "❌ کیفیت‌های ویدیو قابل دریافت نیست.\nممکنه کوکی قدیمی شده باشه یا لینک محدود باشه.")
    else:
        bot.send_message(message.chat.id, "❌ لطفاً یک لینک معتبر یوتیوب بفرست!")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    format_id = call.data
    if chat_id in user_data:
        url = user_data[chat_id]['url']

        msg = bot.send_message(chat_id, "⏳ دانلود شروع شد، لطفاً صبر کنید...")

        filename = download_video(url, format_id, chat_id, msg.message_id)

        if filename and os.path.exists(filename):
            size = os.path.getsize(filename)
            if size < 50 * 1024 * 1024:  # محدودیت تلگرام
                with open(filename, 'rb') as f:
                    bot.send_document(chat_id, f)
                bot.send_message(chat_id, "✅ ویدیو با موفقیت ارسال شد.")
            else:
                bot.send_message(chat_id, "⚠️ فایل بزرگتر از ۵۰MB است و قابل ارسال در تلگرام نیست.")
            os.remove(filename)
        else:
            bot.send_message(chat_id, "❌ خطا در ذخیره یا ارسال فایل.")

def start_bot():
    logger.info("Bot is running...")
    bot.infinity_polling()

if __name__ == "__main__":
    start_bot()
