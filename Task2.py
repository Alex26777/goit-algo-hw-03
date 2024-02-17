import turtle

def koch_snowflake(t, order, size):
    """
    Функція для малювання сніжинки Коха.
    t: об'єкт Turtle для малювання
    order: рівень рекурсії
    size: довжина сторони сніжинки
    """
    if order == 0:  # базовий випадок рекурсії
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]: # кути для створення фігури
            koch_snowflake(t, order-1, size/3) 
            t.left(angle)

# Налаштування вікна
window = turtle.Screen()
window.bgcolor("white")

# Налаштування черепашки
flake = turtle.Turtle()
flake.speed(0)  # максимальна швидкість

# Встановлення початкової позиції
flake.penup()
flake.goto(-150, 90)
flake.pendown()

# Отримання рівня рекурсії від користувача
level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

# Малювання трьох сторін сніжинки, щоб створити повну фігуру
for i in range(3):
    koch_snowflake(flake, level, 300)
    flake.right(120)

# Завершення
window.mainloop()