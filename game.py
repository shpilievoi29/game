"""
Export from exceptions.py our exceptions
"""
from exceptions import EnemyDown, GameOver, Score
from models import Player, Enemy


def play():
    """Start game, input Player, attack and defense """
    player_name = input("Lets play!\nPlease enter your name:\n > ")
    while not player_name.isalpha():
        if not player_name.isalpha():
            player_name = input("You entered wrong name")
        return player_name
    player = Player(player_name)
    enemy = Enemy(1)
    print(f'score table {Score.check_scores()}')
    while True:
        try:
            print(player.attack(enemy))
            print(player.defense(enemy))
            print(f'You have {player.lives} lives')
            print(f'Enemy has {enemy.lives} lives')
        except EnemyDown:
            enemy = Enemy(enemy.level + 1)
            print(f'!!! ENEMY DOWN !!!\nAnother enemy appears! (level {enemy.level}).')
            player.score += 5


if __name__ == '__main__':
    try:
        play()
    except GameOver as err:
        print(f"Game Over! \n {err.player_name} has got {err.score} scores")
    except KeyboardInterrupt:
        pass
    finally:
        print('Goodbye!')
