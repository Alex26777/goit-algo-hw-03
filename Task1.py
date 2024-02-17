import os
import shutil
import argparse
from pathlib import Path

def parse_args():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли з однієї директорії в іншу з сортуванням за розширенням")
    parser.add_argument("source_dir", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("--dest_dir", type=str, default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()

def copy_and_sort_files(source_dir, dest_dir):
    # Рекурсивне читання директорій та копіювання файлів
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            try:
                file_path = Path(root) / file
                file_extension = file.split('.')[-1]
                # Створення піддиректорії за розширенням файлу, якщо не існує
                dest_path = Path(dest_dir) / file_extension
                dest_path.mkdir(parents=True, exist_ok=True)
                # Копіювання файлу в відповідну піддиректорію
                shutil.copy(file_path, dest_path / file)
            except Exception as e:
                print(f"Не вдалося скопіювати файл {file_path}: {e}")

def main():
    args = parse_args()
    copy_and_sort_files(args.source_dir, args.dest_dir)
    print("Файли успішно скопійовано та відсортовано.")

if __name__ == "__main__":
    main()