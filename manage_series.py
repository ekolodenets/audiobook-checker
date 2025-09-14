import argparse
import sys
from config import get_all_series, add_series, remove_series


def list_series():
    """Выводит список всех серий"""
    series = get_all_series()
    if not series:
        print("Нет серий для отслеживания")
        return

    print("\n📚 Список отслеживаемых серий:")
    print("=" * 60)
    for i, item in enumerate(series, 1):
        print(f"{i}. {item['series_name']}")
        print(f"   URL: {item['url']}")
        print(f"   Последняя книга: {item['last_book']}")
        print("-" * 40)


def add_new_series():
    """Интерактивное добавление серии"""
    print("\n➕ Добавление новой серии")
    print("=" * 30)

    name = input("Название серии: ").strip()
    url = input("URL страницы серии: ").strip()
    last_book = input("Последняя известная книга (опционально): ").strip()

    if add_series(name, url, last_book):
        print("✅ Серия успешно добавлена!")
    else:
        print("❌ Серия уже существует или ошибка добавления")


def remove_series_interactive():
    """Интерактивное удаление серии"""
    series = get_all_series()
    if not series:
        print("Нет серий для удаления")
        return

    print("\n🗑️ Удаление серии")
    print("=" * 30)

    for i, item in enumerate(series, 1):
        print(f"{i}. {item['series_name']}")

    try:
        choice = int(input("\nВыберите номер для удаления: "))
        if 1 <= choice <= len(series):
            series_name = series[choice - 1]['series_name']
            if remove_series(series_name):
                print(f"✅ Серия '{series_name}' удалена!")
            else:
                print("❌ Ошибка удаления")
        else:
            print("❌ Неверный выбор")
    except ValueError:
        print("❌ Введите число")


def main():
    parser = argparse.ArgumentParser(description="Управление отслеживаемыми сериями")
    parser.add_argument('action', choices=['list', 'add', 'remove'], help='Действие')

    args = parser.parse_args()

    if args.action == 'list':
        list_series()
    elif args.action == 'add':
        add_new_series()
    elif args.action == 'remove':
        remove_series_interactive()


if __name__ == "__main__":
    main()