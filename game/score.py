import json
import os
from datetime import datetime

class ScoreManager:
    def __init__(self):
        self.file = 'game_results.json'

    def save_result(self, name, rounds, score):
        
        result = {
            'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Player': name,
            'Rounds': rounds,
            'Score': score
        }

        results = []
        if os.path.exists(self.file):
            with open(self.file, 'r', encoding='utf-8') as file:
                try:
                    results = json.load(file)
                except:
                    print('Ошибка чтения файла!')
        results.append(result)

        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(results, file, indent=4, ensure_ascii=False)
            

    def get_results(self):  
        if not os.path.exists(self.file):
            print('Результатов нет!')
            return  

        with open(self.file, 'r', encoding='utf-8') as file:
            results = json.load(file)
            for result in results:
                print('----------')
                date = result.get('Date', result.get)
                player = result.get('Player', result.get)
                rounds = result.get('Rounds', result.get)
                score = result.get('Score', result.get)
                
                print('Date:', date)
                print('Player:', player)
                print('Rounds:', rounds)
                print('Score:', score)    