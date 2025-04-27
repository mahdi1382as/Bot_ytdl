
# 📥 ربات دانلود ویدیو از یوتیوب

ربات تلگرامی که به شما این امکان را می‌دهد که ویدیوها و فایل‌های صوتی یوتیوب را به‌طور مستقیم به تلگرام خود دانلود کنید. این ربات از yt-dlp برای دانلود و از ffmpeg برای پردازش فایل‌های صوتی استفاده می‌کند.

## 🛠 ویژگی‌ها
 
- دانلود ویدیوها با بهترین کیفیت موجود.
- دانلود فایل‌های صوتی در فرمت‌های مختلف (MP3).
- ارسال مستقیم فایل‌ها تا حجم ۵۰ مگابایت از طریق تلگرام.
- انتخاب فرمت و کیفیت دلخواه برای دانلود.

## 📦 پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر نصب شده‌اند:

- **[Python](https://www.python.org/downloads/)** (نسخه ۳.۶ یا بالاتر)
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** (برای دانلود ویدیوها)
- **[FFmpeg](https://ffmpeg.org/download.html)** (برای پردازش ویدیوها و تبدیل به فرمت‌های مختلف)
- **[Git](https://git-scm.com/downloads)** (برای کنترل نسخه و همکاری تیمی)
- **[Browser Cookie 3](https://github.com/aviaryan/browser-cookie3)** (برای استفاده از کوکی‌های یوتیوب)

## 🚀 نصب

### ۱. کلون کردن مخزن

مخزن را کلون کنید:
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### ۲. نصب وابستگی‌ها

از pip برای نصب وابستگی‌های مورد نیاز استفاده کنید:
```bash
pip install -r requirements.txt
```

### ۳. تنظیم کوکی‌های یوتیوب

برای دانلود از یوتیوب، به کوکی‌های معتبر نیاز دارید. از [browser-cookie3](https://github.com/aviaryan/browser-cookie3) برای استخراج کوکی‌های یوتیوب خود استفاده کنید. فایل کوکی را در مسیر مشخص‌شده در پروژه ذخیره کنید.

### ۴. پیکربندی FFmpeg

اطمینان حاصل کنید که **FFmpeg** به‌درستی نصب و به **PATH** سیستم شما اضافه شده است. مسیر FFmpeg را در پیکربندی `ffmpeg_location` در کد تنظیم کنید.

## 💻 نحوه استفاده

1. ربات را به تلگرام خود اضافه کنید.
2. دستور `/start` را برای راه‌اندازی ربات ارسال کنید.
3. لینک ویدیو یا پلی‌لیست یوتیوب را ارسال کنید.
4. از منوی انتخاب، فرمت و کیفیت دلخواه خود را انتخاب کنید.
5. منتظر بمانید تا فایل دانلود و برای شما ارسال شود.

## 🛠 نحوه عملکرد کد

### اجرای ربات:

برای اجرای ربات، کافیست دستور زیر را اجرا کنید:
```bash
python bot.py
```

### نحوه عملکرد:

ربات از **yt-dlp** برای پردازش لینک‌های یوتیوب استفاده می‌کند و تمام فرمت‌ها و کیفیت‌های موجود را بازیابی می‌کند. سپس این گزینه‌ها را به کاربر نمایش می‌دهد تا آنها بتوانند فرمت و کیفیت مورد نظر خود را برای دانلود انتخاب کنند.

اگر کاربر انتخاب کند که فایل صوتی (MP3) دانلود کند، ربات به‌طور خودکار از **FFmpeg** برای تبدیل ویدیو به فایل صوتی استفاده می‌کند.

### پیکربندی:

در فایل `bot.py`، شما می‌توانید موارد زیر را پیکربندی کنید:

- **TOKEN**: توکن ربات تلگرام خود را از [BotFather](https://core.telegram.org/bots#botfather) بگیرید و در اینجا قرار دهید.
- **COOKIES_FILE**: مسیر فایل کوکی یوتیوب خود را مشخص کنید.
- **DOWNLOAD_FOLDER**: پوشه‌ای که می‌خواهید فایل‌ها در آن ذخیره شوند را تنظیم کنید.

### فرمت‌ها و کیفیت‌های موجود:

برای هر لینک یوتیوب، ربات تمام فرمت‌ها و کیفیت‌های موجود را بازیابی کرده و به کاربر نمایش می‌دهد. کاربر می‌تواند یکی از این فرمت‌ها را برای دانلود ویدیو یا فایل صوتی انتخاب کند.

## 📝 نکات

- **حجم فایل**: تنها فایل‌هایی که کمتر از ۵۰ مگابایت هستند می‌توانند از طریق تلگرام ارسال شوند.
- **مشکلات رایج**: اگر مشکلی در دانلود ویدیو یا فایل صوتی وجود دارد، ممکن است به دلیل منقضی شدن کوکی‌ها یا محدودیت لینک باشد.

## 📄 مجوز

این پروژه تحت مجوز [MIT License](LICENSE) منتشر شده است.
```bash

### Explanation of Sections:

1. **Features**: Lists the capabilities of the bot and what it can do.
2. **Prerequisites**: Describes the software dependencies you need to install for the project.
3. **Installation**: Provides step-by-step instructions on how to clone the repo and install the necessary dependencies.
4. **Usage**: Instructions on how to use the bot, including sending commands and choosing formats.
5. **How the Code Works**: Details on how the bot works and how to configure it.
6. **Notes**: Provides additional information on file size limits and potential issues.
7. **License**: Information on the software license (MIT).
```



