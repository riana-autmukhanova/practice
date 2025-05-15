import pygame
import random

# Инициализация
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Traffic Lights")

# Загрузка машины
CAR_IMG = pygame.image.load("15.05/assets/car.jpg")
CAR_IMG = pygame.transform.scale(CAR_IMG, (40, 20))

# Цвета
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Переменные
cars = []  # [x, y, dx, dy]
traffic_light_ns = "green"
traffic_light_ew = "red"
auto_mode = False
last_switch_time = 0
switch_interval = 5000
passed_cars = 0

# Функции
def draw_intersection(win):
    win.fill(GRAY)
    pygame.draw.rect(win, BLACK, (350, 0, 100, HEIGHT))
    pygame.draw.rect(win, BLACK, (0, 250, WIDTH, 100))

def draw_traffic_lights(win, ns, ew):
    pygame.draw.rect(win, GREEN if ns == "green" else RED, (370, 230, 20, 20))
    pygame.draw.rect(win, GREEN if ns == "green" else RED, (410, 350, 20, 20))
    pygame.draw.rect(win, GREEN if ew == "green" else RED, (320, 270, 20, 20))
    pygame.draw.rect(win, GREEN if ew == "green" else RED, (460, 310, 20, 20))

def update_cars(cars, ns, ew):
    global passed_cars
    for car in cars[:]:
        x, y, dx, dy = car
        if dx != 0:
            if (dx > 0 and x < 340) or (dx < 0 and x > 430) or ew == "green":
                car[0] += dx
            if x > WIDTH or x < -40:
                cars.remove(car)
                passed_cars += 1
        else:
            if (dy > 0 and y < 240) or (dy < 0 and y > 360) or ns == "green":
                car[1] += dy
            if y > HEIGHT or y < -20:
                cars.remove(car)
                passed_cars += 1

def draw_cars(win, cars):
    for x, y, dx, dy in cars:
        if dx != 0:
            rotated = pygame.transform.rotate(CAR_IMG, 0 if dx > 0 else 180)
        else:
            rotated = pygame.transform.rotate(CAR_IMG, 90 if dy > 0 else 270)
        win.blit(rotated, (x, y))

def spawn_car():
    direction = random.choice(["north", "south", "east", "west"])
    if direction == "north":
        return [390, -20, 0, 2]
    elif direction == "south":
        return [370, HEIGHT, 0, -2]
    elif direction == "east":
        return [-40, 270, 2, 0]
    else:
        return [WIDTH, 310, -2, 0]

def toggle_lights():
    global traffic_light_ns, traffic_light_ew
    traffic_light_ns, traffic_light_ew = (
        ("green", "red") if traffic_light_ns == "red" else ("red", "green")
    )

def auto_switch():
    global last_switch_time
    now = pygame.time.get_ticks()
    if now - last_switch_time >= switch_interval:
        toggle_lights()
        last_switch_time = now

# Основной цикл
clock = pygame.time.Clock()
run = True
spawn_timer = 0

while run:
    dt = clock.tick(60)
    spawn_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_lights()
            elif event.key == pygame.K_a:
                auto_mode = not auto_mode

    if auto_mode:
        auto_switch()

    if spawn_timer > 1000:
        cars.append(spawn_car())
        spawn_timer = 0

    update_cars(cars, traffic_light_ns, traffic_light_ew)
    draw_intersection(WIN)
    draw_traffic_lights(WIN, traffic_light_ns, traffic_light_ew)
    draw_cars(WIN, cars)

    font = pygame.font.SysFont(None, 28)
    info_text = font.render(f"Проехало машин: {passed_cars}", True, WHITE)
    auto_text = font.render(f"Авто режим: {'ВКЛ' if auto_mode else 'ВЫКЛ'}", True, WHITE)
    WIN.blit(info_text, (10, 10))
    WIN.blit(auto_text, (10, 40))

    pygame.display.update()

pygame.quit()
