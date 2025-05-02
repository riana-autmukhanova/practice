import random

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100

    def move(self, direction, size):
        dx, dy = 0, 0
        if direction == 'w':
            dx = -1
        elif direction == 's':
            dx = 1
        elif direction == 'a':
            dy = -1
        elif direction == 'd':
            dy = 1

        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < size and 0 <= new_y < size:
            self.x, self.y = new_x, new_y
            return True
        else:
            print("Вы не можете выйти за границы поля.")
            return False

def generate_field(size):
    field = [['.' for _ in range(size)] for _ in range(size)]

    # Ловушки
    trap_count = random.randint(3, 5)
    for _ in range(trap_count):
        while True:
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            if (x, y) != (0, 0) and field[x][y] == '.':
                field[x][y] = 'T'
                break

    # Выход
    while True:
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        if (x, y) != (0, 0) and field[x][y] == '.':
            field[x][y] = 'X'
            break

    return field

def print_field(field, player):
    size = len(field)
    for i in range(size):
        row = ""
        for j in range(size):
            if (i, j) == (player.x, player.y):
                row += "P "
            else:
                row += field[i][j] + " "
        print(row.strip())
    print(f"\nЗдоровье: {player.health}\n")

def play_game():
    size = 5
    field = generate_field(size)
    player = Player()

    while True:
        print_field(field, player)
        move = input("Ваш ход (w/a/s/d): ").strip().lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Ошибка: используйте только w, a, s или d.")
            continue

        moved = player.move(move, size)
        if not moved:
            continue

        cell = field[player.x][player.y]

        if cell == 'T':
            print("Вы наступили на ловушку! -20 здоровья.")
            player.health -= 20
            field[player.x][player.y] = '.'

        elif cell == 'X':
            print_field(field, player)
            print("Поздравляем! Вы нашли выход и сбежали из лабиринта!")
            break

        if player.health <= 0:
            print("Вы потеряли всё здоровье. Игра окончена.")
            break

def main():
    while True:
        play_game()
        again = input("Сыграть снова? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
