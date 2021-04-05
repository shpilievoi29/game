"""Import datetime for getting datetime writing"""
from datetime import datetime


class GameOver(Exception):
    """Created GameOver class from Exceptions with
        attributes player_name, scores """

    def __init__(self, player_name, score):
        super().__init__(player_name, score)
        self.player_name = player_name
        self.score = score

    @staticmethod
    def save_score(player_name, score):
        """this method save score to score.txt"""
        with open('scores.txt', 'a+') as file_scores:
            file_scores.write(f'Name:{player_name} Score:{score} Data:{datetime.now()}\n')


class Score:
    """Created class Score fo writing scores to top table 10, and for checking scores"""

    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score

    @staticmethod
    def check_scores():
        """this static method checking scores from file"""
        with open('scores.txt') as scr_file:
            scores = [x for x in scr_file]
            scores_array = [x.split(' ') for x in scores]
            scores_array = sorted(scores_array, key=lambda x: x[-1], reverse=True)
            for score_idx in range(len(scores_array)):
                scores_array[score_idx][-1] = score_idx + 1
            return scores_array


class EnemyDown(Exception):
    """This class is raising that Enemy down"""
