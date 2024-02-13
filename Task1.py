from queue import Queue
import time
import random

# Створення екземпляру черги
q = Queue()

def generate_request():
    """Функція для генерації нової заявки."""
    request_number = random.randint(100, 999)
    q.put(f"Запит {request_number}")
    print(f"Створено нову заявку: Запит {request_number}")

def process_request():
    """Функція для обробки заявки."""
    if not q.empty():
        request = q.get()
        print(f"Обробляємо {request}")
    else:
        print("Черга порожня. Чекаємо на нові заявки...")

# Головний цикл програми
try:
    while True:
        # Імітація випадковості у створенні заявок
        if random.random() < 0.5:
            generate_request()
        else:
            process_request()
        time.sleep(1)  # Затримка для імітації часу обробки
except KeyboardInterrupt:
    print("Програма зупинена користувачем.")
