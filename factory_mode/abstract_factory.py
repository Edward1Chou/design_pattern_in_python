#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: abstract_factory.py
module description: a game sample about abstract factory
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/18 16:31
"""


class Frog(object):
    """
    Kids' game master
    :return:
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encouters {} and {}'.format(self,
                                                       obstacle,
                                                       obstacle.action()))


class Bug(object):
    """
    obstacle: Bug
    :return:
    """
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld(object):
    """
    abstract factory
    :return:
    """
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t-------- Frog World ---------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard(object):
    """
    adults' game master
    :return:
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self,
                                                                obstacle,
                                                                obstacle.action()))


class Ork(object):
    """
    obstacle: Ork
    :return:
    """
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kill it'


class WizardWorld(object):
    """
    abstract factory
    :return:
    """
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------- Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEvironmemt(object):
    """
    entrance for game kinds
    :return:
    """
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    """
    :param name: 
    :return: 
    """
    age = 0
    try:
        age = input('Welcome {}. How old are you?'.format(name))
        age = int(age)
    except ValueError as ve:
        print('Age {} is invalid, please try again...'.format(age))
        return (False, age)
    return (True, age)


if __name__ == '__main__':
    name = input("Hello. What's your name? ")
    valid_input = False
    age = 0
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld  # 条件限制的还不严格，比如负数
    environmet = GameEvironmemt(game(name))
    environmet.play()


