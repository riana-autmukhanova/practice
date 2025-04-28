import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts_left = 10  # Например, даём 10 попыток
    attempts_used = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")
    
    while attempts_left > 0:
        try:
            guess = int(input(f"\nОсталось попыток: {attempts_left}. Ваш вариант: "))
            
            if not 1 <= guess <= 100:
                print("Пожалуйста, введите число в диапазоне от 1 до 100.")
                continue

            attempts_used += 1
            attempts_left -= 1

            if guess < number_to_guess:
                print("Загаданное число больше.")
            elif guess > number_to_guess:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts_used} попыток!")
                break
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите целое число.")
    else:
        print(f"\nК сожалению, попытки закончились. Загаданное число было {number_to_guess}.")

def main():
    while True:
        play_game()
        replay = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if replay != 'да':
            print("Спасибо за игру! До встречи!")
            break

if __name__ == "__main__":
    main()
