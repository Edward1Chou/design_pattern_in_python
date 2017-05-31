#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: external.py
module description: class wanted to be added to adapter
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/31 15:55
"""


class Synthesizer(object):
    """
    has a method: play()
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human(object):
    """
    has a method: speak()
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the human {}'.format(self.name)

    def speak(self):
        return 'says hello!'
