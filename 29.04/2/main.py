import random

class Character:
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def attack_target(self, other):
        damage = max(self.attack - other.defence, 0)
        other.health -= damage
        other.health = max(other.health, 0)
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

def print_status(hero, monster):
    print("\nСостояние персонажей:")
    print(f"{hero.name}: здоровье = {hero.health}, атака = {hero.attack}, защита = {hero.defence}")
    print(f"{monster.name}: здоровье = {monster.health}, атака = {monster.attack}, защита = {monster.defence}")
    print("-" * 40)

def player_turn(hero, monster):
    while True:
        print("\nВыберите действие:")
        print("1 - Атака")
        print("2 - Пропустить ход")
        choice = input("Ваш выбор: ").strip()
        if choice == '1':
            hero.attack_target(monster)
            break
        elif choice == '2':
            print(f"{hero.name} пропускает ход.")
            break
        else:
            print("Ошибка: введите 1 или 2.")

def monster_turn(monster, hero):
    action = random.choice(['attack', 'pass'])
    if action == 'attack':
        monster.attack_target(hero)
    else:
        print(f"{monster.name} пропускает ход.")

def battle():
    hero = Character("Герой", health=100, attack=20, defence=5)
    monster = Character("Монстр", health=80, attack=15, defence=3)

    while hero.health > 0 and monster.health > 0:
        print_status(hero, monster)
        player_turn(hero, monster)
        if monster.health <= 0:
            break
        monster_turn(monster, hero)

    print_status(hero, monster)
    if hero.health <= 0 and monster.health <= 0:
        print("Оба пали в бою. Ничья!")
    elif hero.health <= 0:
        print("Вы проиграли! Монстр победил.")
    elif monster.health <= 0:
        print("Поздравляем! Вы победили монстра!")

def main():
    while True:
        battle()
        again = input("\nСыграть снова? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
