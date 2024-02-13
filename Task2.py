from collections import deque

def is_palindrome(sequence):
    """
    Функція перевірки рядка на паліндром.
    
    :param sequence: Рядок для перевірки
    :return: Булеве значення, що вказує чи є рядок паліндромом
    """
    # Видалення пробілів і перетворення на нижній регістр
    sequence = sequence.replace(" ", "").lower()
    # Створення deque з символів послідовності
    char_deque = deque(sequence)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання:
palindrome_test_cases = ["Мадам", "Я несу гусеня", "Привіт"]

# Перевірка кожного випадку
test_results = {test_case: is_palindrome(test_case) for test_case in palindrome_test_cases}

for test_case, result in test_results.items():
    print(f"'{test_case}' є паліндромом: {result}")
