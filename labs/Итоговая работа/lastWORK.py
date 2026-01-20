import random

RACES = {
    1: ("Человек", (90, 110), (10, 14), (6, 9), (12, 16), (165, 185), (65, 85)),
    2: ("Эльф", (75, 95), (11, 15), (4, 7), (16, 20), (175, 195), (55, 75)),
    3: ("Дворф", (100, 120), (12, 16), (8, 11), (8, 12), (140, 160), (70, 90)),
    4: ("Орк", (95, 115), (14, 18), (5, 8), (6, 10), (170, 190), (75, 95))
}

ENEMIES = [
    ("Гоблин", "быстрый, может атаковать дважды", 1.5, 0.8, 0.7),
    ("Скелет", "устойчивый, получает меньше физического урона", 0.8, 1.5, 0.9),
    ("Орк", "сильный, наносит много урона", 1.8, 1.0, 0.5),
    ("Паук", "ядовитый, отравляет противника", 1.0, 0.7, 1.2),
    ("Зомби", "живучий, восстанавливает здоровье", 0.9, 1.2, 0.6),
    ("Варг", "кровожадный, сильнее при низком HP", 1.3, 0.9, 0.8),
    ("Призрак", "неуловимый, имеет высокий шанс уклонения", 1.1, 0.6, 1.5),
    ("Тролль", "регенерирующий, восстанавливает HP каждый ход", 1.4, 1.3, 0.4)
]

ITEMS = [
    "Зелье здоровья", "Зелье силы", "Зелье ловкости",
    "Заточка для оружия", "Ремкомплект", "Антидот",
    "Стальной меч", "Кожаный доспех", "Кольцо защиты",
    "Амулет ловкости", "Эльфийский лук", "Доспех гномов",
    "Посох мага", "Щит воина", "Сапоги скорости"
]

ROOMS = {
    "combat": "Боевая комната",
    "rest": "Комната отдыха",
    "treasure": "Комната с сундуком"
}

class Character:
    def __init__(self):
        self.race = self.level = 1
        self.exp = self.skill_points = 0
        self.exp_to_next = 100
        self.hp = self.max_hp = self.attack = self.defense = self.agility = 0
        self.height = self.weight = 0
        self.inventory = []
        self.equipped = {"weapon": None, "armor": None, "ring": None, "amulet": None}
        self.coins = 0
        self.inventory_size = 10
        self.poisoned = 0
        
    def show_stats(self):
        stats = [
            f"\n=== ХАРАКТЕРИСТИКИ ===",
            f"Раса: {self.race}",
            f"Уровень: {self.level} (Опыт: {self.exp}/{self.exp_to_next})",
            f"Очки прокачки: {self.skill_points}",
            f"HP: {self.hp}/{self.max_hp}",
            f"Атака: {self.attack}",
            f"Защита: {self.defense}",
            f"Ловкость: {self.agility}",
            f"Рост: {self.height} см",
            f"Вес: {self.weight} кг",
            f"Монеты: {self.coins}",
            f"Инвентарь: {len(self.inventory)}/{self.inventory_size}"
        ]
        
        for slot, item in self.equipped.items():
            if item:
                slot_name = {"weapon": "Оружие", "armor": "Броня", "ring": "Кольцо", "amulet": "Амулет"}[slot]
                stats.append(f"{slot_name}: {item}")
        
        print("\n".join(stats))
        
    def calculate_height_weight_bonus(self):
        """Рассчитывает влияние роста и веса на характеристики"""
        
        bmi = self.weight / ((self.height/100) ** 2)
        if bmi < 18.5:
            self.agility += 2
        elif bmi > 25:
            self.agility -= 1
        
        height_ratio = (self.height - 170) / 20
        self.attack += int(height_ratio)
        
        weight_ratio = (self.weight - 70) / 15
        self.defense += int(weight_ratio)
        
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        
    def add_exp(self, amount):
        self.exp += amount
        print(f"Получено опыта: {amount}")
        while self.exp >= self.exp_to_next:
            self.level_up()
            
    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_next
        self.exp_to_next = int(self.exp_to_next * 1.5)
        self.skill_points += 3
        self.max_hp += 15
        self.hp = self.max_hp
        print(f"\n=== УРОВЕНЬ ПОВЫШЕН! ===")
        print(f"Теперь у вас {self.level} уровень!")
        print(f"Очков прокачки: {self.skill_points}")
        
    def use_skill_points(self):
        while self.skill_points > 0:
            print(f"\nОчков прокачки: {self.skill_points}")
            print("1. +15 к HP (стоит 1 очко)")
            print("2. +3 к атаке (стоит 1 очко)")
            print("3. +3 к защите (стоит 1 очко)")
            print("4. +3 к ловкости (стоит 1 очко)")
            print("5. Выйти")
            
            try:
                choice = int(input("Выберите улучшение: "))
                if choice == 1:
                    self.max_hp += 15
                    self.hp += 15
                    self.skill_points -= 1
                    print("HP увеличен!")
                elif choice == 2:
                    self.attack += 3
                    self.skill_points -= 1
                    print("Атака увеличена!")
                elif choice == 3:
                    self.defense += 3
                    self.skill_points -= 1
                    print("Защита увеличена!")
                elif choice == 4:
                    self.agility += 3
                    self.skill_points -= 1
                    print("Ловкость увеличена!")
                elif choice == 5:
                    break
            except ValueError:
                print("Введите число от 1 до 5")

class Enemy:
    def __init__(self, floor):
        self.name, self.ability, self.attack_mod, self.defense_mod, self.agility_mod = random.choice(ENEMIES)
        self.level = random.randint(max(1, floor-1), floor+1)
        self.hp = random.randint(30, 50) + floor * 15
        self.max_hp = self.hp
        self.attack = int((random.randint(8, 15) + floor * 3) * self.attack_mod)
        self.defense = int((random.randint(2, 8) + floor * 2) * self.defense_mod)
        self.agility = int((random.randint(5, 15) + floor) * self.agility_mod)
        self.exp_reward = random.randint(25, 50) + floor * 8
        self.coin_reward = random.randint(10, 30) + floor * 5
        self.turns = 0
        
    def show_stats(self):
        print(f"\nПротивник: {self.name} (Уровень {self.level})")
        print(f"Особенность: {self.ability}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Атака: {self.attack}, Защита: {self.defense}, Ловкость: {self.agility}")

def create_character():
    character = Character()
    
    print("=== СОЗДАНИЕ ПЕРСОНАЖА ===")
    print("Выберите расу:")
    print("1. Человек")
    print("2. Эльф")
    print("3. Дворф")
    print("4. Орк")
    
    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if choice in RACES:
                name, hp_range, atk_range, def_range, agi_range, height_range, weight_range = RACES[choice]
                character.race = name
                character.max_hp = random.randint(*hp_range)
                character.hp = character.max_hp
                character.attack = random.randint(*atk_range)
                character.defense = random.randint(*def_range)
                character.agility = random.randint(*agi_range)
                character.height = random.randint(*height_range)
                character.weight = random.randint(*weight_range)
                character.calculate_height_weight_bonus()
                break
        except ValueError:
            print("Введите число от 1 до 4")
    
    print(f"\nПерсонаж создан!")
    character.show_stats()
    return character

def generate_room():
    room_type = random.choice(list(ROOMS.keys()))
    return {"type": room_type, "name": ROOMS[room_type]}

def show_inventory_during_combat(player):
    usable_items = [item for item in player.inventory 
                   if "Зелье" in item or "Антидот" in item]
    
    if not usable_items:
        print("У вас нет предметов для использования в бою!")
        return False
    
    print("\n=== ИНВЕНТАРЬ (только для использования) ===")
    print("Вы можете использовать только зелья и антидоты:")
    
    for i, item in enumerate(usable_items, 1):
        print(f"{i}. {item}")
    print(f"{len(usable_items) + 1}. Отмена")
    
    try:
        choice = int(input("Выберите предмет: "))
        if choice == len(usable_items) + 1:
            return False
        
        if 1 <= choice <= len(usable_items):
            item = usable_items[choice-1]
            effects = {
                "здоровья": lambda: player.heal(50),
                "силы": lambda: setattr(player, 'attack', player.attack + 5),
                "ловкости": lambda: setattr(player, 'agility', player.agility + 5)
            }
            
            if "Антидот" in item:
                player.poisoned = 0
                print("Вы вылечились от отравления!")
            else:
                for effect, action in effects.items():
                    if effect in item.lower():
                        action()
                        print(f"{effect.capitalize()} увеличена на 5 на этот бой!")
                        break
            
            player.inventory.remove(item)
            return True
    except ValueError:
        print("Введите номер предмета")
    
    return False

def combat_room(player):
    print("\n=== БОЕВАЯ КОМНАТА ===")
    enemy = Enemy(player.level)
    print(f"На вас напал {enemy.name}!")
    print(f"Особенность: {enemy.ability}")
    
    player_turn = extra_attack = True
    
    while enemy.hp > 0 and player.hp > 0:
        print("\n" + "="*30)
        enemy.show_stats()
        print(f"Ваше HP: {player.hp}/{player.max_hp}")
        
        if player.poisoned > 0:
            poison_damage = player.max_hp // 20 + 1
            player.hp -= poison_damage
            player.poisoned -= 1
            print(f"Яд наносит {poison_damage} урона!")
            if player.hp <= 0:
                break
        
        if player_turn:
            print("\nВаш ход:")
            print("1. Атаковать")
            print("2. Использовать предмет")
            print("3. Увернуться и контратаковать")
            
            try:
                choice = int(input("Выберите действие: "))
                
                if choice == 1:
                    damage = max(1, player.attack + random.randint(-2, 4))
                    if random.random() < 0.1:
                        damage *= 2
                        print("Критический удар!")
                    
                    enemy.hp -= damage
                    print(f"Вы нанесли {damage} урона!")
                    player_turn = False
                    
                elif choice == 2:
                    if show_inventory_during_combat(player):
                        player_turn = False
                    
                elif choice == 3:
                    dodge_chance = player.agility/150 + 0.1
                    if random.random() < dodge_chance:
                        print("Вы успешно уклонились и контратаковали!")
                        counter_damage = max(1, player.attack + random.randint(0, 2))
                        enemy.hp -= counter_damage
                        print(f"Контратака наносит {counter_damage} урона!")
                        extra_attack = True
                    else:
                        print("Уклонение не удалось!")
                        enemy_damage = max(1, int((enemy.attack - player.defense) * 1.5))
                        player.hp -= enemy_damage
                        print(f"Враг наносит усиленный удар {enemy_damage} урона!")
                    player_turn = False
                    
            except ValueError:
                print("Введите число от 1 до 3")
        else:
            print(f"\nХод {enemy.name}:")
            enemy.turns += 1
           
            if enemy.name == "Гоблин" and random.random() < 0.3:
                print(f"{enemy.name} атакует дважды!")
                for i in range(2):
                    if random.random() < player.agility/200:
                        print(f"Вы уклонились!")
                    else:
                        damage = max(1, (enemy.attack if i == 0 else enemy.attack // 2) - player.defense)
                        player.hp -= damage
                        print(f"Наносит {damage} урона!")
            else:
                if random.random() < player.agility/200:
                    print(f"Вы уклонились!")
                else:
                    damage = max(1, enemy.attack - player.defense)
                    player.hp -= damage
                    print(f"Наносит {damage} урона!")
            
            player_turn = True
            
            if extra_attack:
                print("Вы получаете дополнительную атаку за успешное уклонение!")
                extra_attack = False
                player_turn = True
    
    if enemy.hp <= 0:
        print(f"\nВы победили {enemy.name}!")
        player.add_exp(enemy.exp_reward)
        player.coins += enemy.coin_reward
        print(f"Получено монет: {enemy.coin_reward}")
        
        if random.random() < 0.4:
            item = random.choice(ITEMS)
            
            if len(player.inventory) < player.inventory_size:
                player.inventory.append(item)
                print(f"Найдено: {item}")
            else:
                print(f"Найдено: {item}, но инвентарь полон!")
        
        return True
    else:
        print("\nВы проиграли...")
        return False

def treasure_room(player):
    print("\n=== КОМНАТА С СУНДУКОМ ===")
    print("Вы нашли сундук!")
    
    for _ in range(random.randint(1, 3)):
        if random.choice([True, False]):
            coins = random.randint(25, 75) + player.level * 15
            player.coins += coins
            print(f"Найдено монет: {coins}")
        
        if random.choice([True, False]):
            item = random.choice(ITEMS)
            
            if len(player.inventory) < player.inventory_size:
                player.inventory.append(item)
                print(f"Найдено: {item}")
            else:
                print(f"Найдено: {item}, но инвентарь полон!")
    
    print(f"Ваши монеты: {player.coins}")

def rest_room(player):
    print("\n=== КОМНАТА ОТДЫХА ===")
    heal_amount = int(player.max_hp * 0.4)
    player.heal(heal_amount)
    print(f"Вы восстановили {heal_amount} HP")
    
    if player.skill_points > 0 and input("Использовать очки прокачки? (да/нет): ").lower() == "да":
        player.use_skill_points()

def manage_inventory(player, forced=False):
    while True:
        print(f"\n=== ИНВЕНТАРЬ ({len(player.inventory)}/{player.inventory_size}) ===")
        print(f"Монеты: {player.coins}")
        
        if player.inventory:
            for i, item in enumerate(player.inventory, 1):
                print(f"{i}. {item}")
        else:
            print("Инвентарь пуст")
        
        print("\n1. Использовать")
        print("2. Выбросить")
        print("3. Экипировать")
        print("4. Снять")
        if not forced:
            print("5. Выйти")
        
        try:
            if forced:
                choice = int(input("Выберите действие (1-4): "))
            else:
                choice = int(input("Выберите действие: "))
            
            if choice == 1 and player.inventory:
                idx = int(input("Номер предмета: ")) - 1
                if 0 <= idx < len(player.inventory):
                    item = player.inventory[idx]
                    
                    if "Заточка" in item:
                        player.attack += 3
                        print("Атака +3!")
                    elif "Ремкомплект" in item:
                        player.defense += 3
                        print("Защита +3!")
                    elif "Антидот" in item:
                        player.poisoned = 0
                        print("Отравление вылечено!")
                    elif "Зелье" in item:
                        player.heal(50)
                        print("Восстановлено 50 HP!")
                    
                    player.inventory.pop(idx)
                    
            elif choice == 2 and player.inventory:
                idx = int(input("Номер предмета: ")) - 1
                if 0 <= idx < len(player.inventory):
                    print(f"Выброшено: {player.inventory.pop(idx)}")
                    
            elif choice == 3 and player.inventory:
                idx = int(input("Номер предмета: ")) - 1
                if 0 <= idx < len(player.inventory):
                    item = player.inventory[idx]
                    slot_bonus = {"weapon": ("attack", 5), "armor": ("defense", 5), 
                                 "ring": ("defense", 2), "amulet": ("agility", 3)}
                    
                    for slot, (stat, bonus) in slot_bonus.items():
                        if slot in ["weapon", "armor"] and any(x in item.lower() for x in 
                            (["меч", "лук", "посох"] if slot == "weapon" else ["доспех", "броня", "щит"])):
                            if player.equipped[slot]:
                                player.inventory.append(player.equipped[slot])
                                setattr(player, stat, getattr(player, stat) - bonus)
                            player.equipped[slot] = item
                            setattr(player, stat, getattr(player, stat) + bonus)
                            player.inventory.pop(idx)
                            print(f"Экипировано: {item}")
                            break
                    
            elif choice == 4:
                slot = input("Что снять? (оружие/броня/кольцо/амулет): ").lower()
                slot_map = {"оружие": "weapon", "броня": "armor", "кольцо": "ring", "амулет": "amulet"}
                
                if slot in slot_map and player.equipped[slot_map[slot]]:
                    if len(player.inventory) < player.inventory_size:
                        player.inventory.append(player.equipped[slot_map[slot]])
                        player.equipped[slot_map[slot]] = None
                        print(f"Снято: {player.inventory[-1]}")
                    else:
                        print("Инвентарь полон!")
                        
            elif choice == 5 and not forced:
                break
                
        except ValueError:
            print("Введите число")

def main_game():
    print("=== ТЕКСТОВАЯ RPG ===")
    print("Добро пожаловать в подземелье!\n")
    
    player = create_character()
    current_floor = rooms_cleared = 0
    
    player.inventory.extend(["Зелье здоровья", "Антидот"])
    
    while player.hp > 0:
        print(f"\n=== ЭТАЖ {current_floor + 1} ===")
        print(f"Комнат пройдено: {rooms_cleared}")
        
        left_room = generate_room()
        right_room = generate_room()
        
        left_visible = random.choice([True, False])
        right_visible = random.choice([True, False])
        
        print("\nПеред вами развилка:")
        print(f"1. Слева: {left_room['name'] if left_visible else '???'}")
        print(f"2. Справа: {right_room['name'] if right_visible else '???'}")
        print("3. Открыть инвентарь")
        print("4. Показать характеристики")
        print("5. Выйти из игры")
        
        try:
            choice = int(input("Куда пойти? "))
            
            if choice == 1:
                selected_room = left_room
                print(f"\nВы идете налево...")
            elif choice == 2:
                selected_room = right_room
                print(f"\nВы идете направо...")
            elif choice == 3:
                manage_inventory(player)
                continue
            elif choice == 4:
                player.show_stats()
                continue
            elif choice == 5:
                print("Спасибо за игру!")
                break
            else:
                print("Неверный выбор")
                continue
         
            if selected_room["type"] == "combat":
                if not combat_room(player):
                    break
            elif selected_room["type"] == "treasure":
                treasure_room(player)
            elif selected_room["type"] == "rest":
                rest_room(player)
            
            rooms_cleared += 1
            
            if rooms_cleared % 5 == 0:
                current_floor += 1
                player.heal(player.max_hp)
                print(f"\n=== ВЫ СПУСТИЛИСЬ НА ЭТАЖ {current_floor + 1}! ===")
                print("Враги стали сильнее!")
                print(f"Вы полностью восстановили здоровье!")
                
        except ValueError:
            print("Введите число от 1 до 5")
    
    print(f"\n=== ИГРА ОКОНЧЕНА ===")
    print(f"Ваш результат:")
    print(f"Уровень: {player.level}")
    print(f"Пройдено комнат: {rooms_cleared}")
    print(f"Достигнутый этаж: {current_floor + 1}")
    print(f"Всего монет: {player.coins}")

if __name__ == "__main__":
    try:
        main_game()
    except KeyboardInterrupt:
        print("\n\nИгра прервана")
    except Exception as e:
        print(f"Произошла ошибка: {e}")