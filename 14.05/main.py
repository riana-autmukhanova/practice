import pygame
import random

pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Автоматизированная парковка")

# Шрифты
font = pygame.font.SysFont(None, 24)

# Парковка
parking_slots = [None] * 20  # 20 мест

# Параметры парковки
SLOT_SIZE = 40
SLOT_MARGIN = 5
ROWS = 4
COLS = 5

# Кнопки
buttons = {
    "in": pygame.Rect(600, 100, 150, 40),
    "out": pygame.Rect(600, 160, 150, 40)
}

# Текущая машина на въезде
current_car = None

# Типы машин
car_types = {
    "легковая": {"size": 1, "color": (255, 0, 0)},
    "грузовая": {"size": 2, "color": (0, 0, 255)},
    "электромобиль": {"size": 1, "color": (0, 255, 0)}
}

# Загрузка изображения машины
car_image = pygame.image.load("14.05/assets/car.jpg").convert_alpha()
car_image = pygame.transform.scale(car_image, (SLOT_SIZE, SLOT_SIZE))

def generate_car():
    plate = f"{random.choice('ABCEHKMOPTXY')}{random.randint(100, 999)}{random.choice('ABCEHKMOPTXY')}"
    car_type = random.choice(list(car_types.keys()))
    car = {
        "plate": plate,
        "type": car_type,
        "size": car_types[car_type]["size"],
        "color": car_types[car_type]["color"]
    }
    return car

def draw_parking(surface, slots):
    for i, slot in enumerate(slots):
        row = i // COLS
        col = i % COLS
        x = col * (SLOT_SIZE + SLOT_MARGIN) + 50
        y = row * (SLOT_SIZE + SLOT_MARGIN) + 50

        if slot is None:
            pygame.draw.rect(surface, (0, 255, 0), (x, y, SLOT_SIZE, SLOT_SIZE))  # свободное место
        else:
            surface.blit(car_image, (x, y))  # машина — рисуем картинку

def park_car(car):
    size = car["size"]
    for i in range(len(parking_slots) - size + 1):
        if all(parking_slots[j] is None for j in range(i, i + size)):
            for j in range(i, i + size):
                parking_slots[j] = car
            return True
    return False

def remove_random_car():
    indices = [i for i, slot in enumerate(parking_slots) if slot is not None]
    if not indices:
        return "Парковка пуста"
    index = random.choice(indices)
    car = parking_slots[index]
    for i in range(len(parking_slots)):
        if parking_slots[i] == car:
            parking_slots[i] = None
    return f"Машина {car['plate']} уехала"

def draw_ui():
    pygame.draw.rect(screen, (200, 200, 200), buttons["in"])
    pygame.draw.rect(screen, (200, 200, 200), buttons["out"])
    screen.blit(font.render("Впустить", True, (0, 0, 0)), (buttons["in"].x + 30, buttons["in"].y + 10))
    screen.blit(font.render("Выпустить", True, (0, 0, 0)), (buttons["out"].x + 30, buttons["out"].y + 10))

    occupied = sum(1 for slot in parking_slots if slot is not None)
    free = len(parking_slots) - occupied
    screen.blit(font.render(f"Занято: {occupied}  Свободно: {free}", True, (255, 255, 255)), (600, 50))

    if current_car:
        screen.blit(font.render(f"На въезде: {current_car['plate']} ({current_car['type']})", True, (255, 255, 255)), (600, 220))

def handle_click(pos):
    global current_car
    if buttons["in"].collidepoint(pos):
        if not current_car:
            current_car = generate_car()
        else:
            if park_car(current_car):
                current_car = None
            else:
                print("Нет места для этой машины")
    elif buttons["out"].collidepoint(pos):
        message = remove_random_car()
        print(message)

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))
    draw_parking(screen, parking_slots)
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event.pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
