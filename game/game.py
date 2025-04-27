from game.models import User, Computer
from game.score import ScoreManager
from game.exceptions import InvalidRollError
from datetime import datetime

class Game:
    def __init__(self, player_name, rounds):
        self.player = User(player_name)
        self.computer = Computer()
        self.rounds = rounds
        self.curremt_round = 0
        self.score_manager = ScoreManager()
        self.start_time = datetime.now()
        

    def roll_dice(self):
        while True:
            try:
                user_input = input('Нажми Enter для броска кубика: ')
                if user_input != '':
                    raise InvalidRollError('Нажать надо только Enter')
                return self.player.roll_dice(), self.computer.roll_dice()
            except InvalidRollError as error:
                print(error)

    def play_round(self):
        self.curremt_round += 1
        print('Раунд',self.curremt_round)

        while True:
            player_roll, computer_roll = self.roll_dice()
            print('Ирок бросил:', player_roll)
            print('Компьютер бросил:', computer_roll)

            if player_roll == computer_roll:
                print('Ничья. Бросайте кубик снова.')
                continue

            difference = player_roll - computer_roll
            self.player.update_score(difference)
            print('Разница', difference)
            print('Ваш счёт', self.player.score)
            break 

    def start(self):
        print('Ира началась. Количество раундов:', self.rounds)

        for i in range(self.rounds):
            self.play_round()

        self.player.show_results(self.start_time, self.rounds)
        self.score_manager.save_result(self.player.name, self.rounds, self.player.score)


        