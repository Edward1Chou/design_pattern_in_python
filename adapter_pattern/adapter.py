#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: adapter.py
module description: implement of adapter pattern
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/31
"""
from external import Synthesizer
from external import Human


class Computer(object):
    """
    old version,only has method: execute()
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Adapter(object):
    """
    implement of adapter
    """
    def __init__(self, obj, adapted_method):
        """
        add other method in __dict__
        :param obj: 
        :param adapted_method: 
        """
        self.obj = obj
        self.__dict__.update(adapted_method)

    def __str__(self):
        return str(self.obj)


if __name__ == '__main__':
    objects = []
    objects.append(Computer('EdwardChou'))
    syth = Synthesizer('Dreamer')
    objects.append(Adapter(syth, dict(execute=syth.play)))
    human = Human('Birdman')
    objects.append(Adapter(human, dict(execute=human.speak)))
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))