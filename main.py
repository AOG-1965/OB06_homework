# Этап 1: Подготовка и проектирование

# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20

# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`

# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
#
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random

# Этап 2: Реализация класса Hero
class Hero:
    def __init__(self, name):   # Конструктор для инициализации объекта
        self.name = name        # Имя героя
        self.health = 100       # Начальное здоровье героя, инициализируется по умолчанию
        self.attack_power = 20  # Сила удара героя, инициализируется по умолчанию

    def attack(self, other):    # Метод атаки (кто, на кого)
        if self.health > 0:     # Атаковать можно только, если герой жив
            # Добавляем случайность в силу удара
            attack_value = random.randint(self.attack_power - 5, self.attack_power + 5)
            print(f"{self.name} атакует {other.name} и наносит {attack_value} урона!")
            other.take_damage(attack_value)  # Вызов метода нанесения урона противнику
        else:
            print(f"{self.name} мертв и не может атаковать.")  # Если текущее здоровье равно "0"

    def take_damage(self, damage):  # Метод уменьшения здоровья
        self.health -= damage       # Уменьшение здоровья на величину нанесенного  урона
        if self.health < 0:         # У здоровья не может быть отрицательного значения
            self.health = 0         # в таком случае оно равно "0"

    def is_alive(self):             # Проверка, жив ли герой (здоровье больше "0")
        return self.health > 0      # Возвращает True, если жив и False, если здоровье меньше "0"

# Этап 3: Реализация класса Game
class Game:
    def __init__(self, player_name, computer_name):  # Конструктор принимает имена для героев
        self.player = Hero(player_name)              # Герой - имя игрока
        self.computer = Hero(computer_name)          # Герой - компьютер

    def start(self):  # Метод запуска игры
        # # Информирование о начале игры и кто против кого (VS) играет
        print("Игра началась!")
        print(f"{self.player.name} (Игрок) VS {self.computer.name} (Компьютер)\n")

        # Цикл проверки результатов атак: живы герои или нет
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)                                   # Ход игрока
            print(f"{self.computer.name}: Здоровье = {self.computer.health}")   # Уровень текущего здоровья компьютера

            if not self.computer.is_alive():                    # Если компьютер умер (здоровье равно "0")
                print(f"{self.computer.name} побежден!")        # фиксируется соответствующий результат
                if self.player.is_alive():                      # Проверяем, жив ли при этом игрок,
                    print(f"{self.player.name} выиграл бой!")   # если да, то ему присуждается победа в игре
                else:                                           # если нет, то объявляется ничья
                    print("Ничья! Оба героя погибли одновременно.")
                break                                           # Цикл прерывается, игра заканчивается

            self.computer.attack(self.player)                                   # Ход компьютера
            print(f"{self.player.name}: Здоровье = {self.player.health}")       # Уровень текущего здоровья игрока

            if not self.player.is_alive():                      # Если игрок умер (здоровье равно "0")
                print(f"{self.player.name} побежден!")          # фиксируется соответствующий результат
                if self.computer.is_alive():                    # Проверяем, жив ли при этом компьютер
                    print(f"{self.computer.name} выиграл бой!") # если да, то ему присуждается победа в игре
                else:                                           # если нет, то объявляется ничья
                    print("Ничья! Оба героя погибли одновременно.")
                break                                           # Цикл прерывается, игра заканчивается

        # Проверка цикла на ничью
        if not self.player.is_alive() and not self.computer.is_alive():
            print("Ничья! Оба героя погибли одновременно.")

# Этап 4: Тестирование и отладка
game = Game("Игрок", "Компьютер")
game.start()