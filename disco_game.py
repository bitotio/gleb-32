# disco_game.py
import pygame
import random
import time
from all_colors import COLORS

# Инициализация Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Полноэкранный режим
pygame.display.set_caption("Дискотека")

# Загрузка музыки
pygame.mixer.music.load('your_music_file.mp3')  # Укажите свой файл с музыкой здесь
pygame.mixer.music.play(-1)  # Проигрывать музыку в цикле

# Цвет фона
background_color = (0, 0, 0)  # Изначально черный
screen.fill(background_color)

# Функция для рисования кругов
def draw_circles():
    for _ in range(10):
        radius = random.randint(10, 100)
        x = random.randint(radius, screen.get_width() - radius)
        y = random.randint(radius, screen.get_height() - radius)
        color = random.choice(COLORS)
        pygame.draw.circle(screen, color, (x, y), radius)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Случайная смена цвета фона
    background_color = random.choice(COLORS)
    screen.fill(background_color)

    draw_circles()

    pygame.display.flip()  # Обновление экрана
    time.sleep(random.uniform(0.2, 0.8))  # Задержка в диапазоне 200-800 мс

# Завершение работы Pygame
pygame.mixer.music.stop()
pygame.quit()