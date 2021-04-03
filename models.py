"""Import random and other libraries"""
from enum import IntEnum

from random import randint

from exceptions import EnemyDown, GameOver

import settings


class Enemy:
    """Create class Enemy with its attributes"""
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """With help Random.randint enemy chooses his attacks"""
        return randint(1, 3)

    def decrease_lives(self):
        """this method subtract Enemy lives and raise EnemyDown"""
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()


class Attacks(IntEnum):
    """Create Attacks command"""
    WIZARD = 1
    WARRIOR = 2
    ROBBER = 3


class Player:
    """Created class player. Init his functions and methods """
    allowed_attacks = list(map(int, Attacks))

    def __init__(self, player_name):
        self.player_name = player_name
        self.lives = settings.PLAYER_LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """Attack class descriptions. Hero Points Rules"""
        if attack == defense:
            return 0
        if attack == Attacks.WIZARD.value or defense == Attacks.WARRIOR.value:
            return 1

        if attack == Attacks.WARRIOR.value or defense == Attacks.ROBBER.value:
            return 1

        if attack == Attacks.ROBBER.value or defense == Attacks.WIZARD.value:
            return 1
        return -1

    def decrease_lives(self):
        """Loss of lives and points by the Player"""
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.player_name, self.score)

    def attack(self, enemy_object=None):
        """attacks.Creating enemy_object for attacks, choosing
         weapons for attacks adn gets results of attacks"""
        attack_result = self.fight(
            int(input('Choose your attack:\n1. Wizard\n2. Warrior\n3. Robber\n > ')),
                                   Enemy.select_attack())
        if attack_result == 1:
            self.score += 1
            enemy_object.decrease_lives()
            return "You attacked successfully!"
        elif attack_result:
            return "You missed!"
        return "It's a draw!"

    def defense(self, enemy_object):
        """All doings like in attacks but when player stay in defense"""
        defense_result = self.fight(
            enemy_object.select_attack(),
            int(input('Choose your defender'':\n1. Wizard\n2. Warrior\n3. Robber\n > ')))
        if defense_result == -1:
            return 'You defended successfully!'
        elif defense_result:
            self.decrease_lives()
            return "You were hit!"
        return "It's a draw!"
