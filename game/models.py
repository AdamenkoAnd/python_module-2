import random
from game.setting import GAME_LEVELS_CONVERT
from datetime import datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.__score = 0

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            print('Ошибка: счёт должен быть целым числом!')
            return
        self.__score = value 

    def roll_dice(self):
        return random.randint(1, 6)

    def update_score(self, points):
        self.score = self.score + points

class User(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def show_results(self, start_time, rounds):
        print('Результаты игры:')
        print('Время начала иры:', start_time.strftime('%Y-%m-%d %H:%M:%S'))
        print('Игрок:', self.name)
        print('Уровень:', GAME_LEVELS_CONVERT[rounds])
        print('Счёт:', self.score)

        if self.score > 0:
            print('Вы победили!')
        elif self.score < 0:
            print('Компьютер победил!')
        else:
            print('Ничья!')

class Computer(Player):
    def __init__(self):
        Player.__init__(self, 'Компьютер')

