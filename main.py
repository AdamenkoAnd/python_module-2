from game.game import Game
from game.score import ScoreManager
from game.setting import GAME_LEVELS


def main():
    score_manager = ScoreManager()

    while True:
        print('Муню игры')
        print('1-Приступим к ире.')
        print('2-Показать результаты')
        print('3-Выйти из игры')
        choice = input('Выбери 1-3.')

        if choice == '1':
            name = input('Введите ваше имя:')
            if not name:
                print('Имя не может быть пустым')
                continue

            print('Выберити уровень иры:')
            print('1. Short 5-раундов')
            print("2. Medium (8 раундов)")
            print("3. Long (10 раундов)")
            level = input('Выберите уровень игры (1-3):')

            try:
                if level in GAME_LEVELS:
                    game = Game(name, GAME_LEVELS[level])
                    game.start()
                else:
                    print('Ошибка! Неверный уровень.')
            except ValueError as error:
                print('Ошибка')

        elif choice == '2':
            score_manager.get_results()

        elif choice == '3':
            print('Игра окончена.')
            break
        else:
            print('Неверный выбор! Попробуйте снова.')

if __name__ == "__main__":
    main()            


        




