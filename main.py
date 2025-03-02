# main.py
import pygame
import random
from all_colors import COLORS

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Анимация прямоугольников")
background_color = (255, 255, 255)  # Белый
screen.fill(background_color)

# Настройка параметров анимации
x, y = 640, 360  # Центр экрана
rect_size = 190  # Начальный размер
fps = 60         # Количество кадров в секунду
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)  # Очистка экрана

    # Отрисовка вложенных прямоугольников
    current_size = rect_size
    for i in range(19):
        color = random.choice(COLORS)  # Случайный выбор цвета
        pygame.draw.rect(screen, color, (x - current_size // 2, y - current_size // 2, current_size, current_size))
        current_size -= 10  # Уменьшение размера прямоугольника

    pygame.display.flip()  # Обновление экрана
    clock.tick(fps)  # Установка частоты обновлений

# Завершение работы Pygame
pygame.quit()
