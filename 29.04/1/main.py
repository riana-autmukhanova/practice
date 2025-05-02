import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_field(field):
    print()
    print(f" {field[0]} | {field[1]} | {field[2]}")
    print("---|---|---")
    print(f" {field[3]} | {field[4]} | {field[5]}")
    print("---|---|---")
    print(f" {field[6]} | {field[7]} | {field[8]}")
    print()

def check_win(field, symbol):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
        (0, 4, 8), (2, 4, 6)              # диагонали
    ]
    return any(field[i] == field[j] == field[k] == symbol for i, j, k in win_combinations)

def is_draw(field):
    return all(cell in ['X', 'O'] for cell in field)

def play_game():
    while True:
        field = [str(i) for i in range(1, 10)]
        current_player = 'X'

        while True:
            clear_console()
            print_field(field)

            move = input(f"Игрок {current_player}, выбери ячейку (1-9): ")
            try:
                move = int(move)
                if move < 1 or move > 9:
                    print("Ошибка: введите число от 1 до 9.")
                    input("Нажмите Enter для продолжения...")
                    continue
                if field[move - 1] in ['X', 'O']:
                    print("Ошибка: ячейка уже занята.")
                    input("Нажмите Enter для продолжения...")
                    continue
            except ValueError:
                print("Ошибка: введите корректное число.")
                input("Нажмите Enter для продолжения...")
                continue

            field[move - 1] = current_player

            if check_win(field, current_player):
                clear_console()
                print_field(field)
                print(f"Поздравляем! Игрок {current_player} победил!\n")
                break

            if is_draw(field):
                clear_console()
                print_field(field)
                print("Ничья! Поле заполнено.\n")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        again = input("Сыграть ещё раз? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    play_game()
