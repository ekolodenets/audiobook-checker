import time
import os
from dotenv import load_dotenv
from config import get_all_series, save_series_data
from parser import get_last_book_from_site
from telegram import send_telegram_message

# Загружаем .env файл
load_dotenv()


def main():
    print("🔍 Scanning for audiobook updates...")

    series_list = get_all_series()
    if not series_list:
        print("No series to track.")
        return

    updates_found = []
    total_series = len(series_list)

    for i, series in enumerate(series_list, 1):
        series_name = series['series_name']
        stored_last_book = series['last_book']

        actual_last_book = get_last_book_from_site(series['url'])

        if actual_last_book:
            if actual_last_book != stored_last_book:
                print(f"📦 Update found: {series_name}")
                series['last_book'] = actual_last_book
                updates_found.append({
                    "series_name": series_name,
                    "series_url": series['url'],
                    "new_book": actual_last_book
                })
            # else: Убрали вывод "No changes" для каждой серии

        if i < total_series:
            time.sleep(2)

    if updates_found:
        save_series_data(series_list)

        # Format Telegram message
        message = "🎯 <b>New audiobooks found!</b>\n\n"
        for update in updates_found:
            message += f"📚 <a href='{update['series_url']}'><b>{update['series_name']}</b></a>\n"
            message += f"   🆕 {update['new_book']}\n\n"

        message += f"⏰ Checked: {time.strftime('%Y-%m-%d %H:%M')}"

        # Send to Telegram
        send_telegram_message(message)

        print(f"✅ Found {len(updates_found)} updates! Telegram notification sent.")

    else:
        print("📭 No new updates found.")

        # Send empty notification if configured
        if os.environ.get('TELEGRAM_BOT_TOKEN') and os.environ.get('TELEGRAM_CHAT_ID'):
            message = "📋 No new audiobooks found\n"
            message += f"⏰ Checked: {time.strftime('%Y-%m-%d %H:%M')}"
            send_telegram_message(message)

    print("✅ Scanning complete.")


if __name__ == "__main__":
    main()