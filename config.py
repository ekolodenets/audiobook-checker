import json
from pathlib import Path

# Используем текущую директорию вместо домашней
CONFIG_DIR = Path.cwd()  # Текущая папка где запускается скрипт
SERIES_FILE = CONFIG_DIR / "series.json"


def ensure_config_dir():
    """Создает файл series.json если не существует"""
    if not SERIES_FILE.exists():
        print(f"Creating new {SERIES_FILE}...")
        with open(SERIES_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def get_all_series():
    """Возвращает все серии"""
    ensure_config_dir()
    try:
        with open(SERIES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {SERIES_FILE} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: File {SERIES_FILE} is corrupted.")
        return []


def save_series_data(data):
    """Сохраняет данные серий"""
    with open(SERIES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_series(series_name, url, last_book=""):
    """Добавляет новую серию"""
    series = get_all_series()

    # Проверяем нет ли уже такой серии
    for item in series:
        if item['series_name'] == series_name or item['url'] == url:
            return False

    series.append({
        "series_name": series_name,
        "url": url,
        "last_book": last_book
    })

    save_series_data(series)
    return True


def remove_series(series_name):
    """Удаляет серию по имени"""
    series = get_all_series()
    initial_length = len(series)

    series = [item for item in series if item['series_name'] != series_name]

    if len(series) < initial_length:
        save_series_data(series)
        return True
    return False
