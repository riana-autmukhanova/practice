import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Пиццерия")
font = pygame.font.SysFont("arial", 24)
clock = pygame.time.Clock()


# --- Классы меню ---
class MenuItem:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def calculate_price(self):
        return self.base_price

    def display(self, surface, x, y):
        text = font.render(f"{self.name} - {self.base_price}₽", True, (0, 0, 0))
        surface.blit(text, (x, y))


class Pizza(MenuItem):
    pass


class Drink(MenuItem):
    pass


class SideDish(MenuItem):
    pass


class Topping(MenuItem):
    pass


# --- Кнопка ---
class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        pygame.draw.rect(surface, (100, 100, 100), self.rect, 2)
        text = font.render(self.text, True, (0, 0, 0))
        surface.blit(text, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


# --- Заказ ---
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.calculate_price() for item in self.items)

    def display(self, surface, x, y):
        surface.blit(font.render("Текущий заказ:", True, (0, 0, 0)), (x, y))
        y += 30
        for item in self.items:
            item.display(surface, x + 20, y)
            y += 30
        total = self.calculate_total()
        surface.blit(font.render(f"Итого: {total}₽", True, (0, 0, 0)), (x, y + 10))


# --- Данные ---
order = Order()

menu_pizzas = [
    Pizza("Маргарита", 300),
    Pizza("Пепперони", 350),
    Pizza("Четыре сыра", 400)
]

menu_drinks = [
    Drink("Кола", 100),
    Drink("Сок", 120)
]

menu_sides = [
    SideDish("Картошка", 150),
    SideDish("Крылышки", 180)
]


# --- UI кнопки ---
buttons = []

y = 20
for item in menu_pizzas + menu_drinks + menu_sides:
    def make_callback(i=item):
        return lambda: order.add_item(i)
    buttons.append(Button(20, y, 250, 40, f"{item.name} - {item.base_price}₽", make_callback()))
    y += 50

def confirm_order():
    print("Заказ оформлен!")
    for item in order.items:
        print(f"- {item.name} ({item.base_price}₽)")
    print(f"Итого: {order.calculate_total()}₽")
    order.items.clear()

buttons.append(Button(20, 500, 250, 50, "Оформить заказ", confirm_order))


# --- Главный цикл ---
def main():
    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for btn in buttons:
                btn.handle_event(event)

        for btn in buttons:
            btn.draw(screen)

        order.display(screen, 300, 20)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
