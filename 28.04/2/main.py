import random

def initialize_data():
    heroes = [
        "смелый рыцарь",
        "хитрый вор",
        "волшебник",
        "отважный пират",
        "дерзкий исследователь"
    ]
    places = [
        "в далёком королевстве",
        "на заброшенной фабрике",
        "в густом лесу",
        "на просторах космоса",
        "у подножия гор"
    ]
    events = [
        "победил дракона",
        "обнаружил сокровища",
        "выиграл битву",
        "устроил бал",
        "раскрыл древнюю тайну"
    ]
    details = [
        "с волшебным мечом",
        "на летающем ковре",
        "под звуки волшебной музыки",
        "с удивительной силой",
        "в сопровождении магического существа"
    ]
    return heroes, places, events, details

def generate_story(heroes, places, events, details):
    hero = random.choice(heroes)
    place = random.choice(places)
    event = random.choice(events)
    detail = random.choice(details)
    
    story = f"\n{'-'*50}\n{hero.capitalize()} {place} {event} {detail}.\n{'-'*50}"
    return story

def save_story(story):
    try:
        with open("stories.txt", "a", encoding="utf-8") as file:
            file.write(story + "\n")
        print("История успешно сохранена в файл stories.txt!")
    except IOError:
        print("Ошибка при сохранении истории в файл.")

def ask_play_again():
    while True:
        choice = input("\nХотите сгенерировать ещё одну историю? (да/нет): ").strip().lower()
        if choice in ["да", "нет"]:
            return choice == "да"
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

def main():
    heroes, places, events, details = initialize_data()
    
    print("Добро пожаловать в Генератор Историй!")
    
    while True:
        story = generate_story(heroes, places, events, details)
        print(story)
        
        save = input("\nХотите сохранить эту историю в файл? (да/нет): ").strip().lower()
        if save == "да":
            save_story(story)
        
        if not ask_play_again():
            print("\nСпасибо за использование Генератора Историй! До новых встреч!")
            break

if __name__ == "__main__":
    main()
