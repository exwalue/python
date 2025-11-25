import turtle
import time

# --- Рекурсивная функция рисования T-square ---
def draw_t_square_recursive(t, x, y, size, depth):
    if depth == 0:
        return

    t.penup()
    t.goto(x - size / 2, y - size / 2)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

    if depth == 1:
        return

    next_size = size / 2
    offset = size / 2  # смещение к углам

    draw_t_square_recursive(t, x - offset, y + offset, next_size, depth - 1)  # TL
    draw_t_square_recursive(t, x + offset, y + offset, next_size, depth - 1)  # TR
    draw_t_square_recursive(t, x - offset, y - offset, next_size, depth - 1)  # BL
    draw_t_square_recursive(t, x + offset, y - offset, next_size, depth - 1)  # BR

# --- Быстрая анимация ---
def animate_t_square():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")
    screen.tracer(0)  # Отключаем автоматическое обновление для мгновенной отрисовки

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("black")
    t.fillcolor("black")

    max_depth = 5  # Максимальная глубина рекурсии
    delay = 0.8    # Задержка между уровнями в секундах

    try:
        print("Запуск быстрой анимации T-square...")
        print("Закройте окно для выхода")
        
        # Анимация от уровня 1 до максимального
        for depth in range(1, max_depth + 1):
            t.clear()
            print(f"Рисуем уровень {depth}")
            draw_t_square_recursive(t, 0, 0, 300, depth)
            screen.update()
            time.sleep(delay)

        print("Анимация завершена!")
        
        # Оставляем финальный рисунок на экране
        screen.exitonclick()
        
    except turtle.Terminator:
        print("Анимация остановлена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# --- Запуск ---
if __name__ == "__main__":
    animate_t_square()





