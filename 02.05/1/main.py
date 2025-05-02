import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень, Ножницы, Бумага!")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (100, 255, 100)

# Варианты
OPTIONS = ['Камень', 'Бумага', 'Ножницы']

# Кнопки
button_width, button_height = 160, 50
rock_button = pygame.Rect(70, 150, button_width, button_height)
paper_button = pygame.Rect(220, 150, button_width, button_height)
scissors_button = pygame.Rect(370, 150, button_width, button_height)

def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def draw_buttons():
    pygame.draw.rect(screen, GRAY, rock_button)
    draw_text("Камень (R)", rock_button.x + 15, rock_button.y + 10)

    pygame.draw.rect(screen, GRAY, paper_button)
    draw_text("Бумага (P)", paper_button.x + 15, paper_button.y + 10)

    pygame.draw.rect(screen, GRAY, scissors_button)
    draw_text("Ножницы (S)", scissors_button.x + 10, scissors_button.y + 10)

def determine_winner(player, computer):
    if player == computer:
        return "Ничья!"
    wins = {
        "Камень": "Ножницы",
        "Ножницы": "Бумага",
        "Бумага": "Камень"
    }
    return "Вы выиграли!" if wins[player] == computer else "Вы проиграли!"

def main():
    running = True
    result = ""
    player_choice = ""
    computer_choice = ""
    waiting_for_restart = False

    while running:
        screen.fill(WHITE)
        draw_text("Камень Ножницы Бумага!", 140, 30)
        draw_buttons()
        draw_text("Выберите свой ход (R, P, S или кнопка мыши)", 80, 100)

        if player_choice:
            draw_text(f"Вы выбрали: {player_choice}", 50, 220)
            draw_text(f"Компьютер выбрал: {computer_choice}", 50, 250)
            draw_text(result, 50, 280)
            draw_text("Нажмите ПРОБЕЛ чтобы сыграть снова", 50, 310)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if waiting_for_restart and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                result = ""
                player_choice = ""
                computer_choice = ""
                waiting_for_restart = False

            if not waiting_for_restart:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player_choice = "Камень"
                    elif event.key == pygame.K_p:
                        player_choice = "Бумага"
                    elif event.key == pygame.K_s:
                        player_choice = "Ножницы"

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    if rock_button.collidepoint(mouse_pos):
                        player_choice = "Камень"
                    elif paper_button.collidepoint(mouse_pos):
                        player_choice = "Бумага"
                    elif scissors_button.collidepoint(mouse_pos):
                        player_choice = "Ножницы"

                if player_choice:
                    computer_choice = random.choice(OPTIONS)
                    result = determine_winner(player_choice, computer_choice)
                    waiting_for_restart = True

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
