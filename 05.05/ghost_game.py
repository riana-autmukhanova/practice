import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# --- Настройки окна ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Поймай Призрака!")

# --- Цвета ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Шрифты ---
font = pygame.font.SysFont("Arial", 32)

# --- Загрузка призрака из файла ---
ghost_image = pygame.image.load("05.05/assets/ghost.png").convert_alpha()
ghost_image = pygame.transform.scale(ghost_image, (80, 80))


# --- Звук (опционально) ---
# catch_sound = pygame.mixer.Sound("assets/catch.wav")

# --- Таймеры ---
GHOST_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GHOST_EVENT, random.randint(1000, 2000))

# --- Время игры ---
GAME_DURATION = 30_000  # 30 секунд
start_ticks = None

# --- Игровые переменные ---
ghost_rect = ghost_image.get_rect()
ghost_visible = False
ghost_timer = 0
score = 0
game_over = False

clock = pygame.time.Clock()

def draw_text(text, pos, align="left"):
    render = font.render(text, True, BLACK)
    rect = render.get_rect()
    if align == "right":
        rect.topright = pos
    else:
        rect.topleft = pos
    screen.blit(render, rect)

def reset_game():
    global score, start_ticks, game_over, ghost_visible
    score = 0
    game_over = False
    start_ticks = pygame.time.get_ticks()
    ghost_visible = False
    pygame.time.set_timer(GHOST_EVENT, random.randint(1000, 2000))

# --- Старт игры ---
reset_game()

# --- Игровой цикл ---
running = True
while running:
    dt = clock.tick(60)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Клик мышью
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if ghost_visible and ghost_rect.collidepoint(event.pos):
                score += 1
                ghost_visible = False
                # catch_sound.play()

        # Появление призрака
        if event.type == GHOST_EVENT and not game_over:
            ghost_rect.topleft = (
                random.randint(0, WIDTH - ghost_rect.width),
                random.randint(50, HEIGHT - ghost_rect.height)
            )
            ghost_visible = True
            ghost_timer = current_time
            pygame.time.set_timer(GHOST_EVENT, random.randint(1000, 2000))

        # Перезапуск
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                reset_game()

    # Проверка таймера исчезновения призрака
    if ghost_visible and current_time - ghost_timer > 700:
        ghost_visible = False

    # Проверка окончания игры
    if not game_over and current_time - start_ticks >= GAME_DURATION:
        game_over = True

    # --- Рисование ---
    screen.fill(WHITE)

    if ghost_visible:
        screen.blit(ghost_image, ghost_rect)

    draw_text(f"Счёт: {score}", (10, 10))
    if not game_over:
        time_left = max(0, (GAME_DURATION - (current_time - start_ticks)) // 1000)
        draw_text(f"Время: {time_left}", (WIDTH - 10, 10), align="right")
        draw_text("Кликай по призраку, пока не закончится время!", (10, HEIGHT - 40))
    else:
        draw_text(f"Время вышло! Ваш счёт: {score}", (WIDTH // 2 - 200, HEIGHT // 2 - 30))
        draw_text("Нажмите ПРОБЕЛ, чтобы начать заново.", (WIDTH // 2 - 200, HEIGHT // 2 + 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
